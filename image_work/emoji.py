import matplotlib.pyplot as plt
import math
import numpy as np
import cv2 as cv
from d2_str_study import strix
"""smile=cv.imread("image_work\sin.png")
smilegray=cv.cvtColor(smile,cv.COLOR_BGR2GRAY)
ret,threshold=cv.threshold(smilegray,162.5,255,0)
contour,hierechy=cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.drawContours(smile,contour,-1,(0,255,0),2)
cv.imshow('img',smile)
cv.waitKey(0)
print(contour)
print(hierechy)"""

emoji=cv.imread('image_work\image\heart.png')

"""plt.subplot(121),plt.imshow(smile,cmap='gray')
plt.title('oringinal picture')"""

edge1=cv.Canny(emoji,575,200)
contours1,hierechy1=cv.findContours(edge1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
edge2=cv.Canny(emoji,585,300)
contours2,hierechy2=cv.findContours(edge2,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
edge3=cv.Canny(emoji,595,400)
contours3,hierechy3=cv.findContours(edge3,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
edge4=cv.Canny(emoji,605,500)
contours4,hierechy4=cv.findContours(edge4,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


x4=[]
y4=[]
for i in range(len(contours4)):
    for j in contours4[i]:
        x4.append(j[0][0])
        y4.append(j[0][1])
X4=np.array(x4)
Y4=np.array(y4)

Cdt=np.vstack((X4,Y4))

# print(Cdt[0,:])

#先获得一行的索引
sort_indices=np.argsort(Cdt[0,:])
sorted_Cdt=Cdt[:,sort_indices]
sorted_Cdt=sorted_Cdt.T
Cdt_list=sorted_Cdt.tolist()



# for arr1 in contours4:
#     print(arr1[:,0][:,0].tolist())
#     print(arr1[:,0][:,1].tolist())
    


x1=[]
y1=[]
for i in range(len(contours1)):
    for j in contours1[i]:
        x1.append(j[0][0])
        y1.append(-j[0][1])
plt.subplot(2,2,1)
plt.scatter(x1,y1,color='blue',s=20)
x2=[]
y2=[]
for i in range(len(contours2)):
    for j in contours2[i]:
        x2.append(j[0][0])
        y2.append(-j[0][1])
plt.subplot(2,2,2)
plt.scatter(x2,y2,color='red',s=10)
x3=[]
y3=[]
for i in range(len(contours3)):
    for j in contours3[i]:
        x3.append(j[0][0])
        y3.append(-j[0][1])
plt.subplot(223)
plt.scatter(x3,y3,color='black',s=10)
x4=[]
y4=[]
for i in range(len(contours4)):
    for j in contours4[i]:
        x4.append(j[0][0])
        y4.append(-j[0][1])
plt.subplot(224)
plt.scatter(x4,y4,color='green',s=10)
plt.show()

