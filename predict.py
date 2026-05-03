from ultralytics import YOLO

def main():
    # 1. 加载你训练好的模型权重 (请确保你把 best.pt 放到了 weights 文件夹下)
    # 这里以 yolov11n 为例，可以根据实际情况修改名称
    model = YOLO("weights/best.pt")

    # 2. 设置你要预测的素材路径
    # source 可以是:
    # - 单张图片: "datasets/sample/test.jpg"
    # - 文件夹: "datasets/sample/"
    # - 视频文件: "test_video.mp4"
    # - 电脑摄像头: "0"
    source_path = "datasets/sample/" 

    # 3. 执行预测
    results = model.predict(
        source=source_path,
        save=True,      # 自动将画好框的预测结果保存下来
        show=False,     # 预测时是否弹出窗口实时显示 (如果在服务器跑请保持False)
        conf=0.5        # 置信度阈值：低于 50% 把握的预测框会被过滤掉，防止误判
    )

    print("\n🎉 预测完成！请去项目目录下的 runs/detect/predict 文件夹查看结果。")

if __name__ == "__main__":
    main()