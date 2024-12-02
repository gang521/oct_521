"""
复制移动图片的位置
"""
import os
import shutil

# 定义源目录和目标目录
source_dir = 'Image/3'
target_dir = 'DataImage/3'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 复制文件
for i in range(1, 12):  # 从1到11
    src_file = os.path.join(source_dir, f'{i}be.png')  # 源文件路径
    dst_file = os.path.join(target_dir, f'{i}be.png')  # 目标文件路径

    # 检查源文件是否存在
    if os.path.exists(src_file):
        shutil.copy(src_file, dst_file)  # 复制文件
        print(f'已复制: {src_file} 到 {dst_file}')
    else:
        print(f'文件不存在: {src_file}')