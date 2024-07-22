import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def ImageAdd(image1,image2,cv2):
    weightedSum=cv2.addWeighted(image1,0.5,image2,0.4,0)
    return weightedSum
def ImageSubtact(image1,image2,cv2):
    sub=cv2.subtrct(image1,image2)
    return sub
def ImageMultiply(image1,image2):
    mul=cv2.multiply(image1,image2)
    print("Multiply :\n",mul)
    return mul
def Imagediv(image1,imaage2,cv2):
    div=cv2.divide(image1,image2)
    return div
def ImageInv1(image1,cv2):
    inv=cv2.bitwise_not(image1)
    return inv
def ImageInv2(image2,cv2):
    inv=cv2.bitwise_not(image2)
    return inv 
print("please your action or Image:")
print("1.Addition")
print("2.Subtraction")
print("4.Division")
print("5.Sclar Multipliction")
inNum=input("Enter your Choice:")
plt.figure(figsize=(8,15))
image1 = plt.imread("C:\\Users\\mritu\\image3.jpg")
image2 = plt.imread("C:\\Users\\mritu\\image3.jpg")
iA=Image.open("C:\\Users\\mritu\\dog1.jpg")
A=cv2.imread("C:\\Users\\mritu\\dog1.jpg")
iB=iA.convert("L")
iB.show()
cv2.imshow("image3", image1)
cv2.imshow("image3", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()