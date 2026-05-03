

# YOLO 手势识别 (Gesture Recognition) 🤟

本项目是一个基于 YOLO (涵盖 v8-v12 架构) 的手势识别开源模型库。包含了从数据采集、自动抽帧、数据集划分到多模型对比训练与推理的完整工作流。

### 🌟 支持的识别类别
目前模型支持实时检测以下 5 种手势：
- `gesture_one` (数字 1)
- `gesture_two` (数字 2)
- `gesture_five` (数字 5)
- `gesture_ok` (OK 手势)
- `gesture_rock` (石头手势)

### 📊 模型库与性能基准 (Model Zoo & Benchmarks)

我们在相同的手势数据集上，对 YOLOv8 到 YOLOv12 多个版本的模型进行了平行训练与评估。你可以根据部署设备的算力需求（如边缘设备极速推理 vs 高端显卡高精度）下载对应的权重文件。

| 模型版本 | 适用场景 | mAP@0.5 | 模型大小 | 下载链接 (Releases) |
| :--- | :--- | :---: | :---: | :--- |
| **YOLOv12n** | **最佳综合表现 (推荐)** | **0.987** | 5.24 MB | [[best_12n.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_12n.pt)]  |
| **YOLOv8s** | 算力充足设备的平衡选择 | 0.983 | 21.5 MB | [[best_v8s.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_v8s.pt)] |
| **YOLOv8n** | 边缘设备极速推理 | 0.980 | 5.96 MB | [[best_v8n.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_v8n.pt)] |
| **YOLOv8m** | 高精需求，无视显卡压力 | 0.976 | 49.6 MB | [[best_v8m.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_v8m.pt)] |
| **YOLOv9t** | 极小体积的轻量级尝试 | 0.967 | 4.40 MB | [[best_v9t.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_v8n.pt)]|
| **YOLOv10n** | 无 NMS 架构的端到端测试 | 0.954 | 5.46 MB | [[best_v10n.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_v10n.pt)]|
| **YOLOv11n** | 兼顾速度与较新架构优势 | 0.953 | 5.19 MB | [[best_11n.pt](https://github.com/paofue119/YOLO-Gesture-Recognition/releases/download/v1.0.0/best_11n.pt)] |

> 💡 **提示**：以上模型均在相同验证集上测试。其中 **YOLOv12n** 在保持 5.24MB 极小体积的同时，达到了最高的 0.987 mAP，是本项目推荐的首选部署模型。完整数据集下载请访问：
> [通过网盘分享的文件：gesture
链接: https://pan.baidu.com/s/1w4zfHSS6Sh9uez3O7u5XbQ?pwd=gkh6 提取码: gkh6 
--来自百度网盘超级会员v4的分享]

### 📈 纵向与横向性能对比分析

通过对比不同架构（v8-v12）与不同规模（n/s/m）的模型，我们发现最新的 v12 架构在轻量化模型中优势显著，而适当增加模型参数规模（如 v8s）也能有效保证识别的高下限。

| 纵向对比：不同框架 | 横向对比：模型规模 |
| :---: | :---: |
|<img width="960" height="540" alt="幻灯片7" src="https://github.com/user-attachments/assets/8eb5d76e-0296-4dbc-b72a-2f5c3b819007" />|<img width="960" height="540" alt="幻灯片8" src="https://github.com/user-attachments/assets/9c81da9f-dca0-4c4a-a460-40ee7f8baa08" />|


### 🔬 训练过程与指标评估 (Training Evaluation)

我们完整记录了模型在 100 个 Epoch 中的训练过程。从混淆矩阵可以看出，模型对不同手势的特征区分度极高，整体 Loss 曲线收敛平稳。

| 模型版本 (Model) | 训练评估曲线 (Results) | 归一化混淆矩阵 (Matrix) |
| :---: | :---: | :---: |
| **YOLOv12n (最佳)** |<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/9fcfcf43-2615-4666-b11e-cd9921c303c0" />| <img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/dabeb07e-2789-4ae4-9780-5f4436c99b39" />|
| **YOLOv8s** | <img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/4bd5fb83-97dd-41df-bfb4-1629fd343227" />| <img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/9febaf6f-f2f0-4eee-8806-68e5b5c6f6df" />|
| **YOLOv8n** | !<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/6e7bbd0e-a62c-461f-a393-08fb7d2ce70c" /> |<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/f6bb8758-8573-4aa5-be96-0cff16dc5921" />|
| **YOLOv8m** |<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/19de36d8-eaf6-44fe-93ac-9edc0f457076" />|<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/49c6be42-5d7c-468f-8866-58802148139a" />|
| **YOLOv9t** |<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/cc716f9f-01b5-4942-8404-107f47b1a7a4" />|<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/3140b605-c563-46f3-8e2e-e285fe83eb77" />|
| **YOLOv10n** |<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/7d788507-403e-4c53-85d0-05f9b67644f9" />|<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/ac7bb00e-bc4b-4e04-aa52-016d6fb74c30" />|
| **YOLOv11n (最差)** |<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/b607b3ae-97eb-443e-ade9-b3b3685a3156" />|<img width="3000" height="2250" alt="confusion_matrix_normalized" src="https://github.com/user-attachments/assets/ebbe54de-3bea-4ff6-8432-2ca57a1cffbb" />|

### 预测效果对比 (Val Predictions)

为了直观展示模型架构对最终画框效果的影响，我们提取了综合表现最佳的 `YOLOv12n` 与表现最差的 `YOLOv11n` 在验证集上的实际预测结果进行对比：

| 最佳表现：YOLOv12n | 较差表现：YOLOv11n |
| :---: | :---: |
|<img width="1920" height="1920" alt="val_batch0_pred" src="https://github.com/user-attachments/assets/34e33f92-c43e-4cc8-a328-39924af3ad2e" />|<img width="1920" height="1920" alt="val_batch0_pred" src="https://github.com/user-attachments/assets/80715fa4-217d-4d51-97d6-e7b6d7831595" />|

> **观察结论**：相比于 YOLOv11n，YOLOv12n 在复杂背景下对边缘手势的漏检率更低，且置信度分数（Confidence Score）整体更高。

### 🎥 实时推理演示 (Real-time Demo)

在实际的摄像头与复杂背景视频流测试中，模型展现出了极高的鲁棒性，能够精准、稳定地捕捉移动手势。
<img width="720" height="405" alt="video" src="https://github.com/user-attachments/assets/e2249d0b-992f-43ae-bb70-d6e49f25719d" />

## 🚀 快速开始

### 1. 配置环境
建议使用 Python 3.8+，并在虚拟环境中安装依赖：
```bash
pip install -r requirements.txt
```
### 2. 数据集打标签 (Labeling Workflow)
本项目在构建数据集时，采用了**“人工预标注 + AI 自动预推理 + 手动修改”**的高效半自动标注策略，大幅降低了人工成本（也可以直接手动打）：

1. **安装 LabelImg 标注工具：**
   ```bash
   conda create -n labelimg python=3.8
   conda activate labelimg
   pip install labelimg
   ```
2. **人工标注初始数据：** 随机抽取约 20% 的图片（如 `extract_frames.py` 抽帧后的图片），使用 `labelImg` 绘制 YOLO 格式标签。
3. **训练初始小模型：（选做）** 用这 20% 的数据训练一个初始模型。
4. **AI 自动打标签：（选做）** 编写脚本利用初始小模型预测剩余的 80% 图片，并开启 `save_txt=True` 自动生成标签文件，最后通过人工快速微调即可完成全量数据集制作。

### 3. 获取模型权重
前往本仓库的 Releases 页面下载你需要的 `.pt` 模型权重，并将其放置于项目根目录的 `weights/` 文件夹下。

### 4. 运行预测
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
  
## 📚 参考资料
非常感谢以下优秀的文档与视频资源对本项目的启发：
* **模型推理与配置**：[Ultralytics 官方Predict文档](https://docs.ultralytics.com/modes/predict/)
* **官方预训练权重**：[Ultralytics Assets Releases](https://github.com/ultralytics/assets/releases)
* **YOLO 系列学习教程**：[B站-林亿饼YOLO系列视频](https://www.bilibili.com/video/BV1oehbz6Em5?spm_id_from=333.788.videopod.sections&vd_source=ae4449b06e81010a73310fce7b23c655)
* **自动标注工具拓展**：[AutoTag自动化辅助脚本](https://github.com/ALwtg/AutoTag)
