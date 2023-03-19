import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import sys

root = Tk()
root.title('21812055 장지헌')

tl = Label(root)
tl.config(text="CV 공간필터링 프로그램 구현\n") 
tl.pack(side="top")

t2 = Label(root)
t2.config(text="필터 사이즈", justify=LEFT)
t2.pack(side="left")     

fsize=1

ent = Entry(root,textvariable=fsize) # root라는 창에 입력창 생성
ent.config(width=5) 
ent.pack(side="left")



def open():
    root = tkinter.Tk()
    root.withdraw()
    dir_path = filedialog.askopenfilename(parent=root,initialdir="/",title='Please select a directory')
    return dir_path

def median(filterSize):
    src = cv2.imread(open())

    if src is None:
        print('Image load failed!')
        sys.exit()
    
    dst = cv2.medianBlur(src, filterSize)

    cv2.imshow('Before', src)
    cv2.imshow('After Median', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()

def mean(filterSize):
    src = cv2.imread(open())

    if src is None:
        print('Image load failed!')
        sys.exit()

    dst = cv2.blur(src, (filterSize,filterSize))
    cv2.imshow('Before', src)
    cv2.imshow('After Mean', dst)
    cv2.waitKey()

def laplacian(filterSize):
    src = cv2.imread(open())
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    if src is None:
        print('Image load failed!')
        sys.exit()

    dst = cv2.Laplacian(gray, cv2.CV_8U, ksize=filterSize)
    cv2.imshow('Before', src)
    cv2.imshow('After Laplacian', dst)
    cv2.waitKey()

def medlap(filterSize):
    src = cv2.imread(open())

    if src is None:
        print('Image load failed!')
        sys.exit()
    
    dst = cv2.medianBlur(src, filterSize)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    dst = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
    cv2.imshow('Before', src)
    cv2.imshow('After Laplacian', dst)
    cv2.waitKey()

cv2.destroyAllWindows()


ent_btn = Button(root, text='확인').pack(side="left")
mean_btn = Button(root, text='Mean Filter',command=lambda: mean(int(ent.get()))).pack()
median_btn = Button(root, text='Median Filter',command=lambda: median(int(ent.get()))).pack()
lap_btn = Button(root, text='Laplacian Filter',command=lambda: laplacian(int(ent.get()))).pack()
medlap_btn = Button(root, text='Median + Laplacian Filter',command=lambda: medlap(int(ent.get()))).pack()

root.mainloop() 