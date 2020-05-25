# -*- coding: utf-8 -*-
"""
Created on Mon May 25 07:50:07 2020

@author: XD
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import label2rgb
import imageio as imio
from skimage import filters
from skimage.color import rgb2gray
from skimage.measure import regionprops

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

def show_circle():
    x1= int(ent1.get())
    y1= int(ent2.get())
    radius= int(ent3.get())


    fig,ax = plt.subplots()
    ax = fig.add_subplot(111)

    circle = plt.Circle((x1,y1),radius,color="red")
    ax.add_patch(circle)
   

    label = ax.annotate("*",xy = (x1,y1), fontsize = 30,ha = "center")

    ax.axis('off')
    ax.set_aspect('equal')
    ax.autoscale_view()
    plt.show(ax)



def Circle():
    
    view= tk.Tk()
    view.geometry("200x250")

    l1=tk.Label(view, text="X1: ")
    l2=tk.Label(view, text="Y1: ")
    l3=tk.Label(view, text="Radius: ")

    global ent1
    global ent2
    global ent3

    ent1= tk.Entry(view) 
    ent2= tk.Entry(view) 
    ent3= tk.Entry(view)

    btn= tk.Button(view, text="Calculate", bg="green", fg="white", command=show_circle)

    l1.grid(row=0)
    l2.grid(row=1)
    l3.grid(row=2)
    ent1.grid(row=0, column=1)
    ent2.grid(row=1, column=1)
    ent3.grid(row=2, column=1)
    btn.grid(row=3, columnspan=2)

    view.mainloop()

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

app.geometry("900x1000")  
  
app.title("Center of Mass in GUI")
app.iconbitmap(r'C:\Users\TEXON WARE\Documents\NC Project\cg-symbol.ico')
label =  tk.Label(app, text = "Numerical Computing Project",background = "green", foreground = "white", font = ("Times New Roman", 40))
label2 =  tk.Label(app)
label3 =  tk.Label(app)
label4 =  tk.Label(app)
label1 =  tk.Label(app, text = "Center of Mass", background = "green", foreground = "white", font = ("Times New Roman", 30))
label5 =  tk.Label(app)
label6 =  tk.Label(app)
B = tk.Button(text ="Center of Mass of 1D Shape",command=D1Shape)
B.place(relx = 0.1, rely = 0.5)
B2 = tk.Button(text ="Center of Mass of 2D Shape",command=D2Shape)
B3 = tk.Button(text ="Center of Mass of 3D Shape",command=D3Shape)
B4 = tk.Button(text ="Center of Mass of Image",command=Image)
B5 = tk.Button(text ="Center of Mass of Circle",command=Circle)
B6 = tk.Button(text ="Center of Mass of Sigmoid",command=Sigmoid)

label.pack()
label2.pack()
label3.pack()
label4.pack()
label1.pack()
label5.pack()
label6.pack()
B.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()

app.mainloop()