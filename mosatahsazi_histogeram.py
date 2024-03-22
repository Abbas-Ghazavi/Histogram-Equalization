import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#_________________________________________________________________________________________________________
im = cv.imread("a.jpg",0)
im_A = cv.resize(im,(600,600))
im_B = im_A.copy()
row , col = im_B.shape

data_ax = im_B.ravel().tolist()    #tabil be list yek bodi
shedat_i = list(set(data_ax))      #hazfe anasor tekrari(az har onsor yek nemuneh) va moratab sazi soudi

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

#im_C=cv.equalizeHist(im_A)
#_________________________________________________________________________________________________________
#namayesh

plt.subplot(311),plt.hist(im_A),plt.xlim(0, 255),plt.ylim(0, 330)
plt.subplot(312),plt.hist(im_B),plt.xlim(0, 255),plt.ylim(0, 330)
# plt.subplot(313),plt.hist(im_C),plt.xlim(0, 255),plt.ylim(0, 330)

cv.imshow('A',im_A)
cv.imshow('B',im_B)
#cv.imshow('C',im_C)

plt.show()
cv.waitKey()
