from ctypes import windll
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfile
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from functions import *     # my module of image processing functions
import functions
import matplotlib.image as mpimg
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import PIL 
import PIL.Image

window= Tk()
window.geometry('400x335+100+100')
window.title('Image processing software')
window.resizable(0,0)
 # ---------------------------------------------------------------------------   
# a button to upload new image, and save the path in 'filename'
b1 = Button(text= 'upload new image', borderwidth=1, highlightthickness=4, relief="ridge" ,command = lambda:upload_file())
b1.pack()

# ComboBox
cb= ttk.Combobox(width=50)
cb["values"]= ('1- Convert image to GRAYSCALE','2- Flip image vertically','3- Flip image horizontally','4- Crop image to half size to middle',
                '5- Plot histogram for the GRAYSCALED image','6- Increase contrast and brightness','7- Decrease contrast and brightness',
                '8- Scale image horizontally','9- Pixelate image','10- Translate image horizontally','11- Rotate image 90 degree','12- Apply histogram equalization',
                '13- Apply adaptive threshold','14- Apply Low pass filter','15- Apply Gaussian filter','16- Apply Median filter','17- Apply Erosion','18- Apply Dilation',
                '19- Apply Sobel edge detection')
cb.current(0)
cb.pack()

# Button to apply the effect
b2= Button(text= 'apply the effect', borderwidth=1, highlightthickness=10, relief='ridge', bg='#999999', fg='White',command= lambda: getSelection(cb))
b2.pack()

# Button to Reuse the image with another effect
b3 = Button(text= 'use the result image with another effect', borderwidth=1, highlightthickness=5, relief="ridge", command= lambda:reuse())
b3.pack()

# Button to save final image
b1 = Button(text= 'save final image to device', borderwidth=1, highlightthickness=4, relief="ridge", command = lambda:savefile())
b1.pack() 

# Frame and Labels for Instructions
frame= ttk.LabelFrame(window,text= "Instructions", height=300, width=300, relief=RIDGE, padding=(10,10))
frame.pack()

l= Label(frame, text='* to apply an effect on a new image and see it :- \n  - press "upload new image" \n -> select the effect -> press "apply the effect" \n\n \
* to apply multiple effects on the same image :- \n  - press "use the result image with another effect" -> \n \
  select the new effect -> press "apply the effect" ' , fg='black', bg='white', justify='left')
l.pack()

l2= Label(frame, text='ــــــــ This software is made by eng\ Mohamed Abdelkarem ــــــــ', fg='white', bg='black')
l2.pack()

# ---------------------------------------------------------------------------
# function to get the image from device using the path
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    # open window to select file
    path = filedialog.askopenfilename(filetypes=f_types)
    global imgOrg 
    imgOrg= mpimg.imread(path)

# function to save the final image (this saves images only, no histograms)
def savefile():
    # open window to select place to save file
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    # turn to class 'PIL.Image.Image'> to be able to save
    im = PIL.Image.fromarray(functions.img2)
    im.save(filename)

# function to Reuse the image in another function    
def reuse():
    global imgOrg
    imgOrg = functions.img2

# Function to get the text of selection in ComboBox
def getSelection(cb):
    global user_selection
    user_selection= cb.get()
    select_function(user_selection)

# Function to select and call image-processing function .. based on selection in ComboBox    
def select_function(i):
    match i:

        case '1- Convert image to GRAYSCALE':
            to_GRAYSCALE(imgOrg ,i[3:]) 

        case '2- Flip image vertically':
            flip_vertically(imgOrg, i[3:])

        case '3- Flip image horizontally':
            flip_horizontally(imgOrg ,i[3:]) 

        case '4- Crop image to half size to middle':
            crop(imgOrg ,i[3:]) 

        case '5- Plot histogram for the GRAYSCALED image':
            plot_histogram(imgOrg ,i[3:]) 

        case '6- Increase contrast and brightness':
            increse_contrast_and_brightness(imgOrg ,i[3:]) 

        case '7- Decrease contrast and brightness':
            decrease_contrast_and_brightness(imgOrg ,i[3:]) 

        case '8- Scale image horizontally':
            scale_horizontally(imgOrg ,i[3:]) 

        case '9- Pixelate image':
            pixelate(imgOrg ,i[3:]) 

        case '10- Translate image horizontally':
            translate_horizontally(imgOrg ,i[3:]) 

        case '11- Rotate image 90 degree':
            rotete_90_degree(imgOrg ,i[3:]) 

        case '12- Apply histogram equalization':
            apply_histogram_equalization(imgOrg ,i[3:]) 

        case '13- Apply adaptive threshold':
            apply_adaptive_threshold(imgOrg ,i[3:]) 

        case '14- Apply Low pass filter':
            low_pass_filter(imgOrg ,i[3:]) 

        case '15- Apply Gaussian filter':
            gaussian_filter(imgOrg ,i[3:]) 

        case '16- Apply Median filter':
            median_filter(imgOrg ,i[3:]) 

        case '17- Apply Erosion':
            erasion(imgOrg ,i[3:]) 

        case '18- Apply Dilation':
            dilation(imgOrg ,i[3:]) 

        case '19- Apply Sobel edge detection':
            sobel(imgOrg ,i[3:]) 
                  
        case default:
            print("faileeeed")
            

window.mainloop()