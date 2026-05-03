import os
import shutil
import random
from tqdm import tqdm

# ================= 配置区域 =================
# 1. 原始数据路径
SRC_IMAGES = r"D:\yolo\make_dataset\images"  # 你之前保存图片的路径
SRC_LABELS = r"D:\yolo\make_dataset\labels"  # 你打好标签的路径

# 2. 目标根目录
ROOT_DIR = r"D:\yolo\ultralytics-8.3.163\datasets\gesture"

# 3. 划分比例 (训练集:验证集:测试集)
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1


# ============================================

def split_data():
    # 第一步：创建文件夹结构
    sets = ['train', 'val', 'test']
    folders = ['images', 'labels']

    for s in sets:
        for f in folders:
            path = os.path.join(ROOT_DIR, f, s)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"已创建文件夹: {path}")

    # 第二步：获取所有图片文件（以 .jpg 结尾）
    image_files = [f for f in os.listdir(SRC_IMAGES) if f.lower().endswith('.jpg')]

    # 筛选出那些既有图片又有标签的“成对”文件名（去除后缀）
    valid_names = []
    for img_file in image_files:
        name_no_ext = os.path.splitext(img_file)[0]
        label_file = name_no_ext + ".txt"
        if os.path.exists(os.path.join(SRC_LABELS, label_file)):
            valid_names.append(name_no_ext)
        else:
            print(f"跳过：图片 {img_file} 没有对应的标签文件。")

    # 第三步：打乱顺序（随机化）
    random.seed(42)  # 设置随机种子，保证每次运行结果一致（如果想完全随机可以删掉这行）
    random.shuffle(valid_names)

    # 第四步：计算每个集合应该分多少张图
    total_count = len(valid_names)
    train_end = int(total_count * TRAIN_RATIO)
    val_end = train_end + int(total_count * VAL_RATIO)

    # 切分名单
    train_names = valid_names[:train_end]
    val_names = valid_names[train_end:val_end]
    test_names = valid_names[val_end:]

    # 第五步：开始复制文件
    split_dict = {
        'train': train_names,
        'val': val_names,
        'test': test_names
    }

    print(f"\n准备就绪：总计 {total_count} 对有效数据。")
    print(f"划分结果：训练集 {len(train_names)}，验证集 {len(val_names)}，测试集 {len(test_names)}\n")

    for set_name, name_list in split_dict.items():
        # tqdm 进度条
        for name in tqdm(name_list, desc=f"正在处理 {set_name} 集"):
            # 原始路径
            img_src = os.path.join(SRC_IMAGES, name + ".jpg")
            lab_src = os.path.join(SRC_LABELS, name + ".txt")

            # 目标路径
            img_dst = os.path.join(ROOT_DIR, "images", set_name, name + ".jpg")
            lab_dst = os.path.join(ROOT_DIR, "labels", set_name, name + ".txt")

            # 复制文件 (copy2 会保留原始文件的元数据)
            shutil.copy2(img_src, img_dst)
            shutil.copy2(lab_src, lab_dst)

    print(f"\n🎉 数据划分成功！请查看文件夹: {ROOT_DIR}")


if __name__ == "__main__":
    split_data()