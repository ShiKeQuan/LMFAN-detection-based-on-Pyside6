import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QDialog, 
                               QLineEdit, QPushButton, QVBoxLayout, QFormLayout, 
                               QMessageBox, QHBoxLayout, QLabel, QWidget)
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import Qt
from ultralytics import YOLO
from ultralytics import RTDETR
import cv2
import numpy as np
import os
import datetime # 导入datetime模块
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from functools import partial
from timm.models.layers import DropPath, to_2tuple, trunc_normal_
import math


from Ui_GUImywindow import Ui_MainWindow
from GUIresultwindow import ResultsWindow

# --- 添加这个辅助函数 ---
def resource_path(relative_path):
    """ 获取资源的绝对路径，适用于开发环境和PyInstaller打包环境 """
    try:
        # PyInstaller 创建一个临时文件夹，并把路径存储在 _MEIPASS 中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class LoginDialog(QDialog):
    """
    登录对话框
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("登录界面-面向SAR图像舰船目标的多尺度轻量化检测研究")
        self.setFixedSize(380, 160)

        # --- 修改这里 ---
        # 设置窗口图标，使用辅助函数确保路径正确
        icon_path = resource_path('Mywindow/images/physics2.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Warning: Icon not found at {icon_path}")


        # 布局
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        buttons_layout = QHBoxLayout()

        # 控件
        self.username_le = QLineEdit()
        self.username_le.setPlaceholderText("请输入用户名")
        self.password_le = QLineEdit()
        self.password_le.setPlaceholderText("请输入密码")
        self.password_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("登录")
        self.cancel_button = QPushButton("取消")
        self.cancel_button.setObjectName("cancel_button") # 为取消按钮设置对象名以应用特定样式

        # 将控件添加到布局
        form_layout.addRow("用户名:", self.username_le)
        form_layout.addRow("密   码:", self.password_le)
        form_layout.setSpacing(15)
        
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.cancel_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addStretch() # 将所有内容推到顶部，减少中间的间距

        # 连接信号
        self.login_button.clicked.connect(self.handle_login)
        self.cancel_button.clicked.connect(self.reject)

        # 应用美化样式
        self.apply_stylesheet()

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #F5F7FA;
                border-radius: 8px;
            }
            QFormLayout {
                margin: 10px;
            }
            QLabel {
                font-size: 11pt;
                font-family: "Microsoft YaHei UI";
                color: #495057;
            }
            QLineEdit {
                font-size: 11pt;
                padding: 8px;
                background-color: #FFFFFF;
                border: 1px solid #CED4DA;
                border-radius: 4px;
            }
            QLineEdit:focus {
                border: 1px solid #80BDFF;
            }
            QPushButton {
                font-size: 11pt;
                font-weight: bold;
                color: white;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #007BFF, stop:1 #0056B3);
                border: 1px solid #006FE6;
                border-radius: 4px;
                padding: 8px 16px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0069D9, stop:1 #0056B3);
                border-color: #0062CC;
            }
            QPushButton:pressed {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #0056B3, stop:1 #004A99);
                border-color: #004A99;
            }
            QPushButton#cancel_button {
                color: #212529;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #F8F9FA, stop:1 #E2E6EA);
                border: 1px solid #DAE0E5;
            }
            QPushButton#cancel_button:hover {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #E2E6EA, stop:1 #D3D9DF);
                border-color: #C8CFD5;
            }
            QPushButton#cancel_button:pressed {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #D3D9DF, stop:1 #C8CFD5);
                border-color: #BCC5CC;
            }
        """)

    def handle_login(self):
        # 为演示方便，使用硬编码的凭据
        # 真实应用中应使用更安全的方式
        if self.username_le.text() == 'skq' and self.password_le.text() == '123456':
            self.accept()
        else:
            QMessageBox.warning(self, '错误', '用户名或密码错误。')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model_path = None
        self.image_path = None
        
        # 创建我们新定义的 ResultsWindow 类的实例
        self.results_window = ResultsWindow()

        # Connect signals to slots
        self.btn_select_model.clicked.connect(self.select_model)
        self.btn_select_image.clicked.connect(self.select_image)
        self.btn_detect.clicked.connect(self.detect)
        # Connect the new button to show the results table
        self.src_Result_tab.clicked.connect(self.show_results_window)

        # 设置“关于”页面
        self.setup_about_tab()

    def setup_about_tab(self):
        """设置“关于”选项卡的内容和样式，采用圆润的淡蓝色渐变设计。"""
        about_tab_widget = self.tab_2
        # 为选项卡设置对象名，以便在样式表中精确定位
        about_tab_widget.setObjectName("about_tab_container")
        
        about_layout = QVBoxLayout(about_tab_widget)
        about_layout.setContentsMargins(25, 20, 25, 20) # 增加内边距
        about_layout.setSpacing(5) # 修复：减小主布局的控件间距
        about_tab_widget.setLayout(about_layout)

        # --- 创建并配置控件 ---
        title_label = QLabel("面向SAR图像舰船目标的多尺度轻量化检测研究-可视化操作平台")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(True)

        version_title = QLabel("版本信息")
        version_title.setProperty("class", "sectionTitle")
        version_content = QLabel("Version 1.0 (2025.6.27)")
        version_content.setProperty("class", "content")

        tech_title = QLabel("技术栈")
        tech_title.setProperty("class", "sectionTitle")
        
        tech_container = QWidget()
        tech_container.setProperty("class", "content")
        tech_layout = QVBoxLayout(tech_container)
        # 关键修复：为布局设置内边距，确保内容和边框有间距
        tech_layout.setContentsMargins(15, 15, 15, 15)
        tech_layout.setSpacing(5)
        
        tech_line1 = QLabel("•    <b>推理引擎:</b> <span class='techHighlight'>PyTorch-CUDA（支持批量）</span>")
        tech_line2 = QLabel("•    <b>GUI 框架:</b> <span class='techHighlight'>PySide6</span>")
        tech_line3 = QLabel("•    <b>核心库:</b> <span class='techHighlight'>Ultralytics, OpenCV, Numpy, Pytorch</span>")
        for label in [tech_line1, tech_line2, tech_line3]:
            label.setTextFormat(Qt.TextFormat.RichText)
            tech_layout.addWidget(label)

        feedback_title = QLabel("反馈与支持")
        feedback_title.setProperty("class", "sectionTitle")
        feedback_label = QLabel(
            '如有任何问题或建议，请访问 '
            '<a href="https://github.com/ShiKeQuan/LMFAN-detection-based-on-Pyside6" class="hyperlink">项目GitHub仓库</a> '
            '或发送邮件至 '
            '<a href="mailto:shikequan@my.swjtu.edu.cn" class="hyperlink">shikequan@my.swjtu.edu.cn</a>'
        )
        feedback_label.setProperty("class", "content")
        feedback_label.setTextFormat(Qt.TextFormat.RichText)
        feedback_label.setOpenExternalLinks(True)
        feedback_label.setWordWrap(True)

        copyright_title = QLabel("开发与版权")
        copyright_title.setProperty("class", "sectionTitle")

        copyright_container = QWidget()
        copyright_container.setProperty("class", "content")
        copyright_layout = QVBoxLayout(copyright_container)
        # 关键修复：为布局设置内边距
        copyright_layout.setContentsMargins(15, 15, 15, 15)
        copyright_layout.setSpacing(5)

        copyright_line1 = QLabel("•    <b>开发者:</b> 施克权 (个人)")
        copyright_line2 = QLabel("•    <b>版权所有:</b> © 2025-2075")
        copyright_line3 = QLabel("•    <b>许可证:</b> MIT License")
        for label in [copyright_line1, copyright_line2, copyright_line3]:
            label.setTextFormat(Qt.TextFormat.RichText)
            copyright_layout.addWidget(label)

        footer_label = QLabel("© 2025 Shi Kequan. All Rights Reserved.")
        footer_label.setProperty("class", "footer")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- 将控件添加到布局 ---
        about_layout.addWidget(title_label)
        about_layout.addWidget(version_title)
        about_layout.addWidget(version_content)
        about_layout.addWidget(tech_title)
        about_layout.addWidget(tech_container)
        about_layout.addWidget(feedback_title)
        about_layout.addWidget(feedback_label)
        about_layout.addWidget(copyright_title)
        about_layout.addWidget(copyright_container)
        about_layout.addStretch()
        about_layout.addWidget(footer_label)
        
        # --- 应用全新的美化样式表 ---
        stylesheet = """
            #about_tab_container {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #EAF6FF, stop:1 #D1ECFF
                );
                border-radius: 8px;
                font-family: 'Microsoft YaHei UI', 'Segoe UI', sans-serif;
            }
            
            QLabel { background: transparent; }

            #titleLabel {
                color: #003366;
                font-size: 19px;
                font-weight: bold;
                padding-bottom: 10px;
                margin-bottom: 10px; /* 修复：减小标题下方的外边距 */
                border-bottom: 1px solid rgba(0, 89, 167, 0.2);
            }
            
            .sectionTitle {
                color: #0059A7;
                font-size: 15px;
                font-weight: bold;
                margin-top: 12px; /* 调整分区标题的上外边距 */
            }
            
            .content {
                color: #333;
                font-size: 13px;
                padding: 15px;
                margin-top: 5px;
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 8px;
            }

            /* 关键修复：为容器内的标签增加垂直内边距，解决截断问题 */
            QWidget[class="content"] QLabel {
                background: transparent;

            }
            
            .hyperlink {
                color: #007BFF;
                text-decoration: none;
                font-weight: 600;
            }
            .hyperlink:hover {
                text-decoration: underline;
            }
            
            .techHighlight {
                color: #0059A7;
                font-weight: bold;
            }

            .footer {
                color: #667;
                font-size: 11px;
                padding-top: 10px;
                border-top: 1px solid rgba(0, 89, 167, 0.2);
            }
        """
        about_tab_widget.setStyleSheet(stylesheet)

    def show_results_window(self):
        """
        Shows the results window.
        """
        self.results_window.show()

    def select_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Model", "", "PyTorch Model Files (*.pt)")
        if file_path:
            self.model_path = file_path
            model_name = os.path.basename(file_path)
            self.status_label.setText(f"Status: Model selected - {model_name}")
            self.Model_label.setText(model_name)

            # 根据文件名自动检查是否为OBB模型
            if 'obb' in model_name:
                self.checkBox_obb.setChecked(True)
            else:
                self.checkBox_obb.setChecked(False)

            # Clear previous results when a new model is selected
            self.image_label_output.clear()
            self.Class_num.setText("")
            self.Target_num.setText("")
            self.fps_label.setText("")


    def select_image(self):
        # 修改为getOpenFileNames以支持多文件选择
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Image(s)", "", "Image Files (*.png *.jpg *.jpeg)")
        
        if file_paths:
            self.image_path = file_paths # 保存为路径列表
            
            # 清空之前的显示和结果
            self.image_label_input.clear()
            self.image_label_output.clear()
            self.Class_num.setText("")
            self.Target_num.setText("")
            self.fps_label.setText("")

            if len(file_paths) == 1:
                # 如果只选择一张图片，行为和以前一样
                pixmap = QPixmap(file_paths[0])
                self.image_label_input.setPixmap(pixmap.scaled(self.image_label_input.size(), Qt.AspectRatioMode.KeepAspectRatio))
                self.status_label.setText(f"Status: Image selected - {os.path.basename(file_paths[0])}")
            else:
                # 如果选择多张图片，提示批量处理
                # 并显示第一张作为预览
                pixmap = QPixmap(file_paths[0])
                self.image_label_input.setPixmap(pixmap.scaled(self.image_label_input.size(), Qt.AspectRatioMode.KeepAspectRatio))
                self.status_label.setText(f"Status: {len(file_paths)} images selected for batch detection.")


    def detect(self):
        if not self.model_path or not self.image_path:
            self.status_label.setText("Status: Please select a model and image(s) first.")
            return

        try:
            self.status_label.setText("Status: Loading model...")
            QApplication.processEvents() 

            # 动态选择设备，并提供CPU回退
            device = 'cpu'
            if torch.cuda.is_available():
                gpu_name = torch.cuda.get_device_name(0)
                # 检查是否为50系列显卡 (例如 "NVIDIA GeForce RTX 5090")
                # 这是一个临时解决方案，因为当前打包的PyTorch/CUDA版本可能不完全支持50系显卡
                if any(series in gpu_name for series in [" 5090", " 5080", " 5070", " 5060"]):
                    print(f"NVIDIA 50-series GPU ({gpu_name}) detected. Forcing CPU mode due to potential incompatibility.")
                    self.status_label.setText(f"Status: 50-series GPU detected. Forcing CPU mode.")
                    device = 'cpu'
                else:
                    try:
                        # 对于非50系显卡，尝试使用GPU
                        torch.tensor([1.0]).cuda()
                        device = 'cuda'
                        self.status_label.setText(f"Status: CUDA device ({gpu_name}) found. Loading model on GPU...")
                    except Exception as e:
                        # 如果CUDA可用但初始化失败，则回退到CPU
                        print(f"CUDA available but failed to initialize on {gpu_name}. Error: {e}. Falling back to CPU.")
                        self.status_label.setText("Status: CUDA error. Falling back to CPU mode...")
                        device = 'cpu'
            else:
                self.status_label.setText("Status: No CUDA device found. Loading model on CPU...")
            QApplication.processEvents()

            task_name = self.comboBox_choose_task.currentText()
            model = None
            if task_name == "CNN-LMFAN":
                model = YOLO(self.model_path)
            elif task_name == "ViT-LMFAN":
                model = RTDETR(self.model_path)
            else:
                self.status_label.setText(f"Status: Error - Unknown task type '{task_name}'")
                return
            
            # 将模型移动到选定的设备
            model.to(device)

            iou_threshold = self.doubleSpinBox_IOU.value()
            conf_threshold = self.doubleSpinBox_Conf.value()

            # --- 批量检测逻辑 ---
            if len(self.image_path) > 1:
                # 1. 创建结果文件夹 (保存在第一张图片的同级目录下)
                first_image_dir = os.path.dirname(self.image_path[0])
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                results_folder_name = f"detect_results_{timestamp}"
                results_dir = os.path.join(first_image_dir, results_folder_name)
                os.makedirs(results_dir, exist_ok=True)
                
                self.status_label.setText(f"Status: Starting batch detection... Saving to {results_dir}")
                QApplication.processEvents()

                # 2. 循环处理每张图片
                for i, single_image_path in enumerate(self.image_path):
                    # 更新状态和输入图像显示
                    self.status_label.setText(f"Status: Processing {i+1}/{len(self.image_path)}: {os.path.basename(single_image_path)}")
                    pixmap_in = QPixmap(single_image_path)
                    self.image_label_input.setPixmap(pixmap_in.scaled(self.image_label_input.size(), Qt.AspectRatioMode.KeepAspectRatio))
                    QApplication.processEvents()

                    # 执行检测
                    results = model(single_image_path, conf=conf_threshold, iou=iou_threshold)
                    result = results[0]
                    res_plotted = result.plot()

                    # 保存结果图片
                    save_path = os.path.join(results_dir, os.path.basename(single_image_path))
                    cv2.imwrite(save_path, res_plotted)

                    # 更新UI显示
                    self.update_ui_with_result(result, res_plotted, single_image_path)
                    QApplication.processEvents()

                self.status_label.setText(f"Status: Batch detection complete. {len(self.image_path)} images saved.")

            # --- 单张图片检测逻辑 ---
            else:
                single_image_path = self.image_path[0]
                self.status_label.setText(f"Status: Detecting with IoU={iou_threshold}, Conf={conf_threshold} on {device.upper()}...")
                QApplication.processEvents() 
                # 在模型调用时也指定设备
                results = model(single_image_path, conf=conf_threshold, iou=iou_threshold, device=device)
                
                result = results[0]
                res_plotted = result.plot()
                
                self.update_ui_with_result(result, res_plotted, single_image_path)
                self.status_label.setText("Status: Detection complete.")

        except Exception as e:
            self.status_label.setText(f"Status: Error - {e}")

    def update_ui_with_result(self, result, res_plotted, image_path):
        """
        一个辅助函数，用检测结果更新所有相关的UI组件，避免代码重复。
        """
        # 修复：直接通过检查result对象来判断是否为OBB模型，而不是依赖UI复选框
        # 标准模型的 result.obb 为 None，OBB模型的 result.obb 是一个有效的对象
        is_obb = result.obb is not None

        # (可选但建议) 根据实际结果同步UI复选框的状态，为用户提供正确反馈
        self.checkBox_obb.setChecked(is_obb)

        # 将结果和OBB标志添加到结果表格窗口
        self.results_window.add_result(image_path, result, is_obb)

        # 根据模型类型使用正确的属性（boxes或obb）
        boxes_or_obb = result.obb if is_obb else result.boxes

        # 更新结果标签
        target_num = 0
        if boxes_or_obb is not None:
            target_num = len(boxes_or_obb)
        self.Target_num.setText(str(target_num))

        if target_num > 0:
            class_num = len(np.unique(boxes_or_obb.cls.cpu().numpy()))
            self.Class_num.setText(str(class_num))
        else:
            self.Class_num.setText("0")
        
        # 计算并显示FPS
        inference_time_ms = result.speed.get('inference', 0)
        fps = 1000 / inference_time_ms if inference_time_ms > 0 else 0
        self.fps_label.setText(f"{fps:.2f}")
        
        # 转换图像格式并显示在输出标签中
        res_plotted_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
        h, w, ch = res_plotted_rgb.shape
        bytes_per_line = ch * w
        q_image = QImage(res_plotted_rgb.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap_out = QPixmap.fromImage(q_image)
        self.image_label_output.setPixmap(pixmap_out.scaled(self.image_label_output.size(), Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    login_dialog = LoginDialog()
    # 使用 .exec() 以模态方式显示对话框
    if login_dialog.exec() == QDialog.DialogCode.Accepted:
        # 如果登录成功，则显示主窗口
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    # 如果对话框被取消或关闭，应用程序将自动退出
