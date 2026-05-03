```markdown
# YOLO 手势识别 (Gesture Recognition) 🤟

本项目是一个基于 YOLO (兼容 v8-v12) 的手势识别开源模型。包含了从数据采集、自动抽帧、数据集划分到多模型对比训练与推理的完整工作流。

## 🌟 支持的识别类别
目前模型支持实时检测以下 5 种手势：
- `gesture_one` (数字 1)
- `gesture_two` (数字 2)
- `gesture_five` (数字 5)
- `gesture_ok` (OK 手势)
- `gesture_rock` (摇滚/石头手势)

## 🚀 快速开始

### 1. 配置环境
建议使用 Python 3.8+，并在虚拟环境中安装依赖：
```bash
pip install -r requirements.txt
```

### 2. 获取模型权重
为了避免仓库体积过大，训练好的模型权重 `.pt` 文件托管在 GitHub Releases 中。
1. 前往本仓库右侧的 [Releases](#) 页面。
2. 下载 `best.pt`。
3. 将下载的模型文件放置于项目根目录的 `weights/` 文件夹下。

### 3. 运行预测
准备几张测试图片放入 `datasets/sample/` 文件夹，然后运行推理脚本：
```bash
python predict.py
```
预测结果将自动保存在 `runs/detect/predict` 目录下。

## 📁 核心目录说明
- `scripts/`: 存放各种自动化小工具（如：`extract_frames.py` 视频抽帧, `split_dataset.py` 数据集划分）。
- `train.py`: 核心训练脚本，支持一键遍历训练不同版本的 YOLO 模型。
- `predict.py`: 推理脚本，支持图片、视频和摄像头实时检测。
- `gesture.yaml`: YOLO 格式的数据集路径与类别配置文件。
```

