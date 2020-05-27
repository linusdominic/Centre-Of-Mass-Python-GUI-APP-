# -*- coding: utf-8 -*-
"""
Created on Mon May 25 07:50:07 2020

@author: XD
"""

import tkinter as tk
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import label2rgb
import imageio as imio
from skimage import filters
from skimage.color import rgb2gray
from skimage.measure import regionprops
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from math import *
n = 20
x = np.random.randint(-50,50,n)
m = np.random.randint(1,200,n)
y = np.random.randint(0,200,n)
z = np.random.randint(0,30,n)
cgx = np.sum(x*m)/np.sum(m)
cgy = np.sum(y*m)/np.sum(m)
cgz = np.sum(z*m)/np.sum(m)
y1 = np.zeros(len(m))

def D1Shape():
    plt.scatter(x,y1,s=m)
    plt.scatter(cgx,0,color='g',marker = '|', s=1e4)
    plt.show()
def D2Shape():
    plt.plot(x,y, color='green', linestyle = 'dashed', linewidth = 3, marker='o',markerfacecolor='blue',markersize=12)
    plt.xlabel('x - axis')
    plt.ylabel('y - label')
    plt.title('Centre of Mass')
    plt.show()
    plt.plot(cgx,cgy, color='green', linestyle = 'dashed', linewidth = 3, marker='o',markerfacecolor='blue',markersize=12)
    plt.xlabel('x - axis')
    plt.ylabel('y - label')
    plt.title('Centre of Mass')
    plt.show()
def D3Shape():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(x,y,z,s=m)
    ax.scatter(cgx,cgy,cgz,color = 'k',marker='+',s=1e4)
    plt.show(ax)
def Image():
    image = rgb2gray(imio.imread(r'C:\Users\TEXON WARE\Documents\NC Project\pexels-photo-736230.jpeg'))
    threshold_value = filters.threshold_otsu(image)
    labeled_foreground = (image > threshold_value).astype(int)
    properties = regionprops(labeled_foreground,image)
    cofm = properties[0].centroid
    weighted_cofm = properties[0].weighted_centroid
    print(cofm)
    colorized = label2rgb(labeled_foreground,image,colors=['black','yellow'],alpha= 0.0)
    fig, ax = plt.subplots()
    ax.imshow(colorized)

    ax.scatter(cofm[1],cofm[0],s = 160, c='C0', marker='.')
    plt.show()



def Circle():
    
    # read image through command line 
    img = cv2.imread('circle.png')

    # convert image to grayscale image
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # convert the grayscale image to binary image
    ret,thresh = cv2.threshold(gray_image,127,255,0)
 
    # calculate moments of binary image
    M = cv2.moments(thresh)
 
    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
 
    # put text and highlight the center
    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
    # display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def Sigmoid():
    def sigmoid(x):
        return (3/ (2 + np.exp(-x)))

    x = np.linspace(-10,10,10)
    y = np.linspace(-10,10,100)

    plt.plot(x,sigmoid(x),'r', label='linspace(-10,10,10)')
    plt.plot(y,sigmoid(y),'b', label='linspace(-10,10,100)')
    cgx = -0.7
    cgy = 0.75

    plt.plot(cgx,cgy,marker="*")

    plt.grid()  

    plt.title('Sigmoid Function')
    plt.suptitle('Sigmoid')

    plt.legend(loc = 'lower right')

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))

    plt.show()        

app = tk.Tk()

app.geometry("650x500")  
  
app.title("Center of Mass in GUI")
app.iconbitmap(r'C:\Users\TEXON WARE\Documents\NC Project\cg-symbol.ico')
label =  tk.Label(app, text = "Numerical Computing Project",background = "green", foreground = "white", font = ("Times New Roman", 40))
label2 =  tk.Label(app)
label3 =  tk.Label(app)
label4 =  tk.Label(app)
label1 =  tk.Label(app, text = "Center of Mass", background = "green", foreground = "white", font = ("Times New Roman", 30))
label5 =  tk.Label(app)
label6 =  tk.Label(app)
B = tk.Button(text ="Center of Mass of 1D Shape",bg="yellow",fg="black",command=D1Shape)
B2 = tk.Button(text ="Center of Mass of 2D Shape",bg="yellow",fg="black",command=D2Shape)
B3 = tk.Button(text ="Center of Mass of 3D Shape",bg="yellow",fg="black",command=D3Shape)
B4 = tk.Button(text ="Center of Mass of Image",bg="yellow",fg="black",command=Image)
B5 = tk.Button(text ="Center of Mass of Circle",bg="yellow",fg="black",command=Circle)
B6 = tk.Button(text ="Center of Mass of Sigmoid",bg="yellow",fg="black",command=Sigmoid)

label.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3)
label1.grid(row=4)
label5.grid(row=5)
label6.grid(row=6)
B.grid(row=7, columns=1)
B2.grid(row=8, columns=2)
B3.grid(row=9, columns=2)
B4.grid(row=10, columns=4)
B5.grid(row=11, columns=5)
B6.grid(row=12, columns=6)

app.mainloop()