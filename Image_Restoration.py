import os
from tkinter import filedialog
import cv2
import numpy as np
from tkinter import * # type: ignore
from PIL import Image, ImageTk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    
def gambar_rusak():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Pilih File Gambar Rusak", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    img = Image.open(file)
    img = ImageTk.PhotoImage(img)
    labl1.configure(image=img, width=340,height=350)
    labl1.place(x=40,y=10)
    labl1.image = img
    
def gambar_mask():
    global file2
    file2 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Pilih File Gambar Rusak", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
    img = Image.open(file)
    img = ImageTk.PhotoImage(img)
    labl.configure(image=img, width=340,height=350)
    labl.place(x=40,y=10)
    labl.image = img
    
def proses_gambar():
    # Load Foto Rusak
    fotoRusak = cv2.imread(file)

    markedDamages = cv2.imread(file2, 0)

    # Mengubah foto menjadi citra binary
    ret, thresh1 = cv2.threshold(markedDamages, 254, 255, cv2.THRESH_BINARY)

    # Memperbesar Ukuran Citra Binary
    kernel = np.ones((7,7), np.uint8)
    mask = cv2.dilate(thresh1, kernel, iterations = 1)
    # Hasil Proses Inpainting
    hasil = cv2.inpaint(fotoRusak, mask, 3, cv2.INPAINT_NS)
    cv2.imshow('Hasil', hasil)
    cv2.imshow('Foto Rusak Awal', fotoRusak)
    cv2.imwrite("FotoBagus.png", hasil)
    cv2.waitKey(0)
    
root = Tk()
root.title("Aplikasi Restorasi Gambar")

#atur ukuran window
window_width = 700
window_height = 500

#Panggil center_window
center_window(root, window_width, window_height)
root.resizable(False, False)
root.configure(bg="#151D26")

#frame gambar 1
frame1=Frame(root,bd=3,bg="black",width=340,height=350,relief=GROOVE)
frame1.place(x=10,y=10)
labl1 = Label(frame1,bg="black")
labl1.place(x=40,y=10)

#frame gambar 2
frame1=Frame(root,bd=3,bg="black",width=340,height=350,relief=GROOVE)
frame1.place(x=350,y=10)
labl = Label(frame1,bg="black")
labl.place(x=40,y=10)

#frame button1
frame3 = Frame(root,bd=3,bg="#151D26",width=340,height=100,relief=GROOVE)
frame3.place(x=10,y=370)
Button(frame3,text="Gambar Rusak",width=12,height=2,font="arial 14 bold",command=gambar_rusak).place(x=12,y=18)
Button(frame3,text="Mask Gambar",width=12,height=2,font="arial 14 bold", command=gambar_mask).place(x=170,y=18)

#frame button2
frame4 = Frame(root,bd=3,bg="#151D26",width=340,height=100,relief=GROOVE)
frame4.place(x=350,y=370)
Button(frame4,text="Perbaiki Gambar",width=25,height=2,font="arial 14 bold",command=proses_gambar).place(x=12,y=18)

root.mainloop()