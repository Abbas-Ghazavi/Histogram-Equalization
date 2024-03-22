import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

im = cv.imread("a.jpg", 0)

im_A = cv.resize(im, (600, 600))
im_B = im_A.copy()

row, col = im_B.shape
data_ax = im_B.ravel().tolist()
shedat_i = list(set(data_ax))

#_________________________________________________________________________________________________________
#mohasebe meghdare faravani va tedad kol satr*sotoon va ehtemale kol va ehtemal i va natije
p_i_ = []
s_i_ = []
g_i_ = []
sum_f= 0
n_s_ = row * col          #tedade pixelhaye matris(omghe bit 8=256)

for i in shedat_i :
    faravani = data_ax.count(i)            #shomaresh tedad tekrar meghdare har pixel dar matris
    p_i_.append( faravani / n_s_ )       #taghsime faravani har pixel bar tedad kol pixelhaye matris jadid
    sum_f += faravani                      #jame maghadir faravani har pixel
    s_i_.append( sum_f / n_s_ )            #ekhtesase maghadire faravali har pixel i dar list
    g_i_.append( round( s_i_[-1] * 255 ) ) #zarb meghdare s(i) dar omghe bit va round   

# print("data ax :  ",data_ax)
# print("faravani: ",faravani)
# print("shedate i :  ",shedat_i)
# print("p(i) :  ",p_i_)
# print("S(i) :  ",s_i_)
# print("g(i) :  ",g_i_)

#_________________________________________________________________________________________________________
#jaygozari matris ax ba meghdare mohsebe shode jadid
for i in range(row):
    for j in range(col):
        #jostejoye meghdare har pixel ax asli dar liste shedate(i) va bargardandane andis an
        andis = shedat_i.index(im_B[i][j])  
        im_B[i][j] = g_i_[andis]  #jaygozini meghdare har pixel ax asli ba meghdare moadele an dar list g(i)

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
