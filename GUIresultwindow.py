import os
import csv
import numpy as np
from PySide6.QtWidgets import QWidget, QFileDialog, QAbstractItemView, QTableWidgetItem
from PySide6.QtCore import Qt

# 导入从 .ui 文件生成的类
from Ui_GUIresultwindow import Ui_ResultsWindow

# 创建一个新类，它既是 QWidget 也是 Ui_ResultsWindow
class ResultsWindow(QWidget, Ui_ResultsWindow):
    """
    一个用于显示检测结果的窗口。
    这个类加载由Qt Designer创建的UI，并实现其功能。
    """
    def __init__(self):
        super().__init__()
        # 使用 Ui_ResultsWindow 中的 setupUi 方法来构建界面
        self.setupUi(self)

        # 设置表格的选择行为为选择整行
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # 连接按钮信号到槽函数
        self.save_button.clicked.connect(self.save_results)
        self.clear_button.clicked.connect(self.clear_table)
        self.remove_button.clicked.connect(self.remove_selected_rows)

    def add_result(self, image_path, result, is_obb=False):
        """
        向表格中添加一行新的检测结果。
        is_obb: 一个布尔标志，指示结果是否来自OBB模型。
        """
        image_name = os.path.basename(image_path)
        h, w = result.orig_shape
        img_size = f"{w}x{h}"
        inference_speed = f"{result.speed.get('inference', 0):.2f}"

        # 根据模型类型使用正确的属性（boxes或obb）
        boxes_or_obb = result.obb if is_obb else result.boxes

        detection_content = ""
        if boxes_or_obb is not None and len(boxes_or_obb) > 0:
            class_ids = boxes_or_obb.cls.cpu().numpy().astype(int)
            class_names = result.names
            unique_classes, counts = np.unique(class_ids, return_counts=True)
            
            content_parts = [f"{class_names.get(cid, f'Class_{cid}')}:{count}" 
                             for cid, count in zip(unique_classes, counts)]
            detection_content = "; ".join(content_parts)
        else:
            detection_content = "未检测到目标"

        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(image_name))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(img_size))
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(detection_content))
        self.table_widget.setItem(row_position, 3, QTableWidgetItem(inference_speed))

    def clear_table(self):
        """
        清空表格中的所有行。
        """
        self.table_widget.setRowCount(0)

    def remove_selected_rows(self):
        """
        从表格中移除当前选中的行。
        """
        selected_indexes = self.table_widget.selectionModel().selectedRows()
        for index in sorted(selected_indexes, reverse=True):
            self.table_widget.removeRow(index.row())

    def save_results(self):
        """
        将表格数据保存到CSV文件。
        """
        if self.table_widget.rowCount() == 0:
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "保存结果", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                header = [self.table_widget.horizontalHeaderItem(i).text() for i in range(self.table_widget.columnCount())]
                writer.writerow(header)
                for row in range(self.table_widget.rowCount()):
                    row_data = [self.table_widget.item(row, col).text() for col in range(self.table_widget.columnCount())]
                    writer.writerow(row_data)
        except Exception as e:
            print(f"保存文件时出错: {e}")