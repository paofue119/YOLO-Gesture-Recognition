import torch
from ultralytics import YOLO

ms = [
    'yolov8n', 'yolov8s', 'yolov8m',
    'yolov9t', 'yolov9s', 'yolov9m',
    'yolov10n', 'yolov10s', 'yolov10m',
    'yolo11n', 'yolo11s', 'yolo11m',
    'yolo12n', 'yolo12s', 'yolo12m',
]

if __name__ == "__main__":
    for m in ms:
        # 加载预训练权重模型
        model = YOLO(m + ".pt")
        # 开始模型训练
        model.train(
            data=r"gesture.yaml",  # 数据集配置文件路径
            epochs=300,           # 训练总轮数
            imgsz=640,            # 输入图片尺寸大小
            patience=20,
            batch=-1,             # 自动适配最大可用batch size
            cache="ram",          # 将数据缓存到内存，加速训练
            workers=1,            # 数据加载线程数
            project="results",    # 训练结果保存的总文件夹
            name=m,               # 每个模型单独新建子文件夹命名
        )
        del model
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
print("DONE")