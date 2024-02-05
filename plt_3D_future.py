import matplotlib.pyplot as plt
import numpy as np

def visualize_feature_map(feature_map, save_path):
    slice_idx = feature_map.shape[2] // 2  # 选择中间的深度切片
    slice_map = feature_map[0, 0, slice_idx, :, :]  # B=0, C=0 为例

    slice_map = (slice_map - slice_map.min()) / (slice_map.max() - slice_map.min())

    plt.imshow(slice_map, cmap='gray')
    plt.colorbar()
    plt.savefig(save_path)  # 保存图像
    plt.close()  # 关闭图形，防止重复显示

