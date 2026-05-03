

# YOLO 手势识别 (Gesture Recognition) 🤟

本项目是一个基于 YOLO (涵盖 v8-v12 架构) 的手势识别开源模型库。包含了从数据采集、自动抽帧、数据集划分到多模型对比训练与推理的完整工作流。

### 🌟 支持的识别类别
目前模型支持实时检测以下 5 种手势：
- `gesture_one` (数字 1)
- `gesture_two` (数字 2)
- `gesture_five` (数字 5)
- `gesture_ok` (OK 手势)
- `gesture_rock` (摇滚/石头手势)

### 📊 模型库与性能基准 (Model Zoo & Benchmarks)

我们在相同的手势数据集上，对 YOLOv8 到 YOLOv12 多个版本的模型进行了平行训练与评估。你可以根据部署设备的算力需求（如边缘设备极速推理 vs 高端显卡高精度）下载对应的权重文件。

| 模型版本 | 适用场景 | mAP@0.5 | 模型大小 | 下载链接 (Releases) |
| :--- | :--- | :---: | :---: | :--- |
| **YOLOv12n** | **最佳综合表现 (推荐)** | **0.987** | 5.24 MB | [best_12n.pt](#) |
| **YOLOv8s** | 算力充足设备的平衡选择 | 0.983 | 21.5 MB | [best_v8s.pt](#) |
| **YOLOv8n** | 边缘设备极速推理 | 0.980 | 5.96 MB | [best_v8n.pt](#) |
| **YOLOv8m** | 高精需求，无视显卡压力 | 0.976 | 49.6 MB | [best_v8m.pt](#) |
| **YOLOv9t** | 极小体积的轻量级尝试 | 0.967 | 4.40 MB | [best_v9t.pt](#) |
| **YOLOv10n** | 无 NMS 架构的端到端测试 | 0.954 | 5.46 MB | [best_v10n.pt](#) |
| **YOLOv11n** | 兼顾速度与较新架构优势 | 0.953 | 5.19 MB | [best_11n.pt](#) |

> 💡 **提示**：以上模型均在相同验证集上测试。其中 **YOLOv12n** 在保持 5.24MB 极小体积的同时，达到了最高的 0.987 mAP，是本项目推荐的首选部署模型。完整数据集下载请访问：[填写你的网盘链接] (提取码: xxxx)

### 📈 纵向与横向性能对比分析

通过对比不同架构（v8-v12）与不同规模（n/s/m）的模型，我们发现最新的 v12 架构在轻量化模型中优势显著，而适当增加模型参数规模（如 v8s）也能有效保证识别的高下限。

*(👇 请将你的【纵向对比图】和【横向对比图】直接拖拽到这行文字下方替换 👇)*
<img width="960" height="540" alt="幻灯片8" src="https://github.com/user-attachments/assets/93686b1c-3ec0-4128-a327-8f03df4fb5bb" />
<img width="960" height="540" alt="幻灯片7" src="https://github.com/user-attachments/assets/92ab3982-6d85-4c3d-806c-f35cdf362618" />


### 🎥 实时推理演示 (Real-time Demo)

在实际的摄像头与复杂背景视频流测试中，模型展现出了极高的鲁棒性，能够精准、稳定地捕捉移动手势。

*(👇 请将你的【实时识别 GIF 动图】直接拖拽到这行文字下方替换 👇)*
[拖拽图片到这里]

### 🔬 训练过程与指标评估 (Training Evaluation)

我们完整记录了模型在 100 个 Epoch 中的训练过程。从混淆矩阵可以看出，模型对不同手势的特征区分度极高，整体 Loss 曲线收敛平稳。

*(👇 请依次将【results.png】、【confusion_matrix_normalized.png】、【val_batch0_pred.jpg】拖拽到这行文字下方替换 👇)*
[拖拽图片到这里]
<img width="1920" height="1920" alt="val_batch0_pred" src="https://github.com/user-attachments/assets/aa36326f-5e66-4876-b962-57dca5125128" />
<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/92d34ddd-a914-48b1-87fd-837f98951e63" />
<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/1d16466b-7caf-4fc6-b994-f85e6e5d84e4" />


## 🚀 快速开始

### 1. 配置环境
建议使用 Python 3.8+，并在虚拟环境中安装依赖：
```bash
pip install -r requirements.txt
```

### 2. 获取模型权重
前往本仓库的 Releases 页面下载你需要的 `.pt` 模型权重，并将其放置于项目根目录的 `weights/` 文件夹下。

### 3. 运行预测
准备几张测试图片或视频放入 `datasets/sample/` 文件夹，修改 `predict.py` 中的模型路径后运行推理脚本：
```bash
python predict.py
```
预测结果将自动保存在 `runs/detect/predict` 目录下。

## 📁 核心目录说明
- `scripts/`: 存放数据处理工具（`extract_frames.py` 视频抽帧, `split_dataset.py` 数据集划分）。
- `train.py`: 核心训练脚本，支持一键遍历训练不同版本的 YOLO 模型。
- `predict.py`: 推理脚本，支持图片、视频和摄像头实时检测。
- `gesture.yaml`: YOLO 数据集路径与类别配置文件。
