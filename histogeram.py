import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

im = cv.imread("a.jpg", 0)

im_A = cv.resize(im, (600, 600))
im_B = im_A.copy()

row, col = im_B.shape
data_ax = im_B.ravel().tolist()
shedat_i = list(set(data_ax))

p_i_ = []
s_i_ = []
g_i_ = []
sum_f = 0
n_s_ = row * col

for i in shedat_i:
    faravani = data_ax.count(i)
    p_i_.append(faravani / n_s_)
    sum_f += faravani
    s_i_.append(sum_f / n_s_)
    g_i_.append(round(s_i_[-1] * 255))

for i in range(row):
    for j in range(col):
        andis = shedat_i.index(im_B[i][j])
        im_B[i][j] = g_i_[andis]
        
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes[0, 0].imshow(im_A, cmap='gray')
axes[0, 0].set_title('Image A')


axes[1, 0].hist(im_A.ravel(), bins=256  )
axes[1, 0].set_xlim(0, 255)
axes[1, 0].set_ylim(0, 330)
axes[1, 0].set_title('Histogram of Image A')
axes[0, 1].imshow(im_B, cmap='gray')
axes[0, 1].set_title('Image B')

axes[1, 1].hist(im_B.ravel(), bins=256)
axes[1, 1].set_xlim(0, 255)
axes[1, 1].set_ylim(0, 330)
axes[1, 1].set_title('Histogram of Image B')


plt.tight_layout()
plt.show()
