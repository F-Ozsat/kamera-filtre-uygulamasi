import cv2 
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk



#------------------------------Backend------------------------------#

frame_mode=0
cam_mode = 0

red,green,blue = 1,1,1

def cam_run():
    
    if cam_mode == 1:
    
        ret,frame = cam.read()
    
        if not ret:
            messagebox.showerror("Kamera Hatası","görüntü alınamıyor")
    
        if frame_mode == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif frame_mode == 1:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        elif frame_mode == 2:
            frame = (frame * np.array([red,green,blue])).clip(0, 255).astype(np.uint8)
            
            
    
    if cam_mode == 0:
        frame = np.zeros((800,600,3),dtype=np.uint8)
    
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(img)
    canvas.imgtk = imgtk
    canvas.itemconfig(canvas.image_on_canvas, image=imgtk)
        
    
    root.after(1, cam_run)


def cam_open():
    global cam
    global cam_mode
    cam = cv2.VideoCapture(0)
    cam_mode = 1
    
def cam_close():
    global cam_mode
    cam_mode = 0
    cam.release()



def turn_gray():
    global frame_mode
    frame_mode = 1

def turn_bgr():
    global frame_mode
    frame_mode = 0
    
def turn_rgb_filter():
    global frame_mode,red,blue,green
    
    try:
        red = int(red_entry.get())/100
        green = int(green_entry.get())/100
        blue = int(blue_entry.get())/100
        
    except:
        messagebox.showerror("girdi hatası","0-100 arasında bir sayı giriniz")
    
    frame_mode = 2

#-------------------------------------------------------------------#



#------------------------------Frontend-----------------------------#

root = Tk()
root.geometry("800x600+100+100")
root.title("Filtre Uygulaması")



btn_cam_open = Button(root,text="Kamera Aç",font=("Calibri",10),command=cam_open,bg="green")
btn_cam_open.place(x=50,y=50)

btn_cam_close = Button(root,text="Kamera Kapat",font=("Calibri",10),command=cam_close,bg="red")
btn_cam_close.place(x=150,y=50)

btn_gray = Button(root,text="Gri Filtre",font=("Calibri",10),command=turn_gray)
btn_gray.place(x=50,y=100)

btn_bgr = Button(root,text="Normal Filtre",font=("Calibri",10),command=turn_bgr)
btn_bgr.place(x=150,y=100)



red_label = Label(root,text="Red:",font=("Calibri",10))
red_label.place(x=300,y=50)

red_entry = Entry(root, font=("Calibri",10))
red_entry.place(x=350,y=50,width=50)

btn_rgb_filter = Button(root,text="RGB Filt",font=("Calibri",10),command=turn_rgb_filter)
btn_rgb_filter.place(x=450,y=50)

green_label = Label(root,text="Green:",font=("Calibri",10))
green_label.place(x=300,y=70)

green_entry = Entry(root, font=("Calibri",10))
green_entry.place(x=350,y=70,width=50)

blue_label = Label(root,text="Green:",font=("Calibri",10))
blue_label.place(x=300,y=90)

blue_entry = Entry(root, font=("Calibri",10))
blue_entry.place(x=350,y=90,width=50)



canvas = Canvas(root,width=600,height=300)
canvas.place(x=50,y=150)



black_frame = np.zeros((300, 400, 3), dtype=np.uint8)
img = Image.fromarray(black_frame)
imgtk = ImageTk.PhotoImage(image=img)
canvas.image_on_canvas = canvas.create_image(0, 0, anchor=NW, image=imgtk)
canvas.imgtk = imgtk




cam_run()

mainloop()

#-------------------------------------------------------------------#