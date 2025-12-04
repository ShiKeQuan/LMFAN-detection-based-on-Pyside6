# LMFAN-detection-based-on-Pyside6

一个基于 PySide6 的多模型检测平台，主要面向 SAR 舰船目标检测任务，提供可视化的模型推理与结果分析界面。

2025.8.22 本软件已取得软件著作权。后续将视情况逐步开源更多相关代码与模型配置。

## 功能特性

- **多模型支持**：集成 YOLO 等多种目标检测模型，便于对比和切换。
- **多种输入源**：支持本地图像/视频、网络 RTSP 流以及本地摄像头。
- **可视化界面**：基于 PySide6 的桌面 GUI，包含主控制窗口、结果展示窗口与 YOLO 专用展示窗口。
- **结果展示**：在图像上叠加检测框、类别与置信度，并以表格形式展示检测结果。
- **统计与分析**：提供如 Wilcoxon 检验等基础统计工具，对不同模型/方案结果进行对比分析。
- **易用性与美观性**：自定义控件、亚克力飞出面板、拖拽缩放等 UI 交互设计，方便非专业用户使用。

## 环境与依赖

建议环境（供参考）：

- Python 3.9+
- PySide6
- Ultralytics YOLO（如 `ultralytics` 或其他 YOLO 实现）
- 常用科学计算与图像处理库（如 `numpy`、`opencv-python` 等）

你可以使用 `pip` 安装所需依赖，例如：

```bash
pip install -r requirements.txt
```

> 说明：如暂无完整的 `requirements.txt`，请根据实际使用的库手动安装，或后续补充本文件。

## 快速开始

1. 克隆本仓库：

	```bash
	git clone https://github.com/ShiKeQuan/LMFAN-detection-based-on-Pyside6.git
	cd LMFAN-detection-based-on-Pyside6/Mywindow
	```

2. 创建并激活虚拟环境（可选但推荐）：

	```bash
	python -m venv .venv
	.venv\Scripts\activate
	```

3. 安装依赖：

	```bash
	pip install -r requirements.txt
	```

4. 运行主界面（以 `GUImywindow.py` 为例）：

	```bash
	python GUImywindow.py
	```

	根据界面提示，选择检测模型与输入数据源即可开始使用。

## 目录结构（节选）

```text
Mywindow/
  GUImywindow.py           # 主界面入口
  GUImywindow_50.py        # 其他版本/配置的主界面
  GUIresultwindow.py       # 检测结果展示窗口
  GuiYOLOSHOW.py           # YOLO 检测结果展示窗口
  utils/                   # 工具模块（摄像头、RTSP、绘图等）
	 webCamera.py
	 rtspDialog.py
	 drawFigure.py
	 UpdateFrame.py
	 AcrylicFlyout.py
	 MouseLabel.py
	 TableView.py
	 customGrips.py
	 ...
  images/                  # 图标与界面图片资源
  fonts/                   # 字体资源
  *.ui                     # Qt Designer 设计文件
  Ui_*.py                  # 自动生成的 UI Python 文件
```

## 版权与开源说明

- 本项目相关软件已于 2025 年 8 月 22 日取得软件著作权。
- 当前仓库主要提供 GUI 框架与部分实现示例，完整模型与更多功能将视情况分阶段开源。
- 如需学术合作或商业授权，请联系作者。
