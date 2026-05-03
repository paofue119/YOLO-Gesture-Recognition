import cv2
import os
from tqdm import tqdm

# ================= 配置区域 =================
# 1. 视频存放的文件夹路径
INPUT_DIR = r"D:\yolo\make_dataset\videos"

# 2. 图片保存的文件夹路径
OUTPUT_DIR = r"D:\yolo\make_dataset\images"

# 3. 核心参数：每秒提取几张图片？(你可以随时修改这个数字)
TARGET_FPS = 2  # 比如这里设置为2，代表视频里的每一秒，我们只抽2张图出来


# ============================================

def main():
    # 如果保存图片的文件夹不存在，程序会自动帮你创建一个
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"已创建输出文件夹: {OUTPUT_DIR}")

    # 获取视频文件夹下所有的 .mp4 文件
    # 遍历 INPUT_DIR，找出所有以 .mp4 结尾的文件（忽略大小写）
    video_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.mp4')]

    if not video_files:
        print("没有找到任何.mp4 视频，请检查一下路径！")
        return

    print(f"总共找到 {len(video_files)} 个视频文件，准备开始提取...\n")

    # 开始挨个处理视频
    for video_file in video_files:
        # 拼接出视频的完整路径，例如 E:\practice\yolo_data\video\001.mp4
        video_path = os.path.join(INPUT_DIR, video_file)

        # 获取视频的名字（不要后缀），比如 "001.mp4" 变成 "001"
        video_name = os.path.splitext(video_file)[0]

        # 使用 OpenCV 打开视频
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"警告：无法打开视频 {video_file}，已跳过。")
            continue

        # 获取这个视频原本的帧率（比如一般视频是 30帧/秒 或 60帧/秒）
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        # 获取这个视频总共有多少帧
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 计算提取间隔（核心逻辑）
        # 如果原视频是30帧/秒，你想提2帧/秒，那么 30/2 = 15，也就是每隔15帧保存一张图
        if TARGET_FPS >= original_fps:
            frame_interval = 1  # 如果你要求的帧率比原视频还高，那就全提取
        else:
            frame_interval = int(round(original_fps / TARGET_FPS))

        # 用于给图片命名的序号（每个视频从1开始算）
        saved_count = 1

        # 使用 tqdm 创建一个进度条，total 是总帧数，desc 是进度条前面的文字说明
        with tqdm(total=total_frames, desc=f"正在处理: {video_file}") as pbar:
            # 循环读取视频的每一帧
            for current_frame_index in range(total_frames):
                # ret 是个布尔值(True/False)表示是否成功读取，frame 就是这一张图片的数据
                ret, frame = cap.read()

                # 如果视频读完了，或者中途出错了，就退出循环
                if not ret:
                    break

                # 判断当前帧的索引是不是间隔的倍数，如果是，就保存！
                if current_frame_index % frame_interval == 0:
                    # 组装图片名字： {video_name}_{saved_count:05d}.jpg
                    # :05d 的意思是，数字补齐到 5 位，比如 1 变成 00001
                    img_name = f"{video_name}_{saved_count:05d}.jpg"

                    # 组装图片的完整保存路径
                    save_path = os.path.join(OUTPUT_DIR, img_name)

                    # 使用 OpenCV 把图片写入硬盘
                    cv2.imwrite(save_path, frame)

                    # 保存成功后，序号 +1
                    saved_count += 1

                # 读完一帧，进度条往前走一格
                pbar.update(1)

        # 一个视频处理完后，一定要释放资源
        cap.release()

    print("\n🎉 全部视频处理完毕！图片已成功保存到:", OUTPUT_DIR)


# 程序的入口
if __name__ == "__main__":
    main()