import numpy as np
import cv2
import matplotlib.pyplot as plt

# 图6-1中的矩阵
# img = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
# ], dtype=np.uint8)

# 用matplotlib存储
# plt.imsave('./img/img_pyplot.jpg', img)

# 用OpenCV存储
# cv2.imwrite('./img/img_cv2.jpg', img)

# 直接读取单通道
color_img = cv2.imread('../Automatically grab pictures/img/a6528029.jpg',cv2.IMREAD_GRAYSCALE);
print(color_img);

# 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
# cv2.imwrite('./img/test_grayscale.jpg',color_img);

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
cv2.imwrite('./img/test_imwrite.jpg',color_img,(cv2.IMWRITE_JPEG_QUALITY,100));

# cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
cv2.imwrite('./img/test_imwrite.png',color_img,(cv2.IMWRITE_PNG_COMPRESSION,5));