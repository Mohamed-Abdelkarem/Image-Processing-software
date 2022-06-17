import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# Function to plot 2 image side-to-side 
def plot_images(image_1, image_2, title_1="Orignal", title_2='modified'):
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    # check if image_1 is colored or grayscaled
    if len(image_1.shape) == 3:
        plt.imshow(image_1)
    elif len(image_1.shape) < 3:   
        plt.imshow(image_1, cmap='gray')    
    plt.title(title_1)
    
    plt.subplot(1, 2, 2)
    # check if image_2 is colored or grayscaled
    if len(image_2.shape) == 3:
        plt.imshow(image_2)
    elif len(image_2.shape) < 3:   
        plt.imshow(image_2, cmap='gray')    
    plt.title(title_2)

    plt.show()     

# Function to plot 3 image side-to-side 
def plot_images3(image_1, image_2, image_3, title_1="Orignal", title_2="with noise", title_3="after filter"):
    plt.subplot(1, 3, 1)
    plt.imshow(image_1)
    plt.title(title_1)
    plt.subplot(1, 3, 2)
    plt.imshow(image_2)
    plt.title(title_2)
    plt.subplot(1, 3, 3)
    plt.imshow(image_3)
    plt.title(title_3)
    plt.show()   

# Function to plot 4 image 
def plot_images4(image_1, image_2, image_3, image_4, title_1="Orignal", title_2="original after filter",
                  title_3="with noise", title_4="noise with filter"):
    # plt.figure(figsize=(30, 30))                  
    plt.subplot(1, 4, 1)
    plt.imshow(image_1)
    plt.title(title_1)
    plt.subplot(1, 4, 2)
    plt.imshow(image_2)
    plt.title(title_2)
    plt.subplot(1, 4, 3)
    plt.imshow(image_3)
    plt.title(title_3)
    plt.subplot(1, 4, 4)
    plt.imshow(image_4)
    plt.title(title_4)
    plt.show()  

# function to plot two histograms side-by-side.
def plot_histograms(old_image, new_image, title_1="Orignal", title_2="modified"):
    intensity_values=np.array([x for x in range(256)])
    plt.subplot(1, 2, 1)
    plt.bar(intensity_values, cv.calcHist([old_image],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.bar(intensity_values, cv.calcHist([new_image],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(title_2)
    plt.show()

# function returns noisy image
def noised(img):
    rows, cols= img.shape[:2]
    noise = np.random.normal(0,15,(rows,cols,3)).astype(np.uint8)
    return (img + noise)

# make it global to re-use it again
global img2

#____________________________________________    
# function 1- Convert to GRAYSCALE image
def to_GRAYSCALE(imgORG, fun_name):
    global img2
    # check if imgORG is gray or not (can't convert gray to gray)
    if len(imgORG.shape) == 3:
        img2= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        img2= imgORG

    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 2- Flip image vertically
def flip_vertically(imgORG, fun_name): 
    global img2
    img2= cv.flip(imgORG, 0) 
    plot_images(imgORG, img2, title_2=fun_name) 

#____________________________________________    
# function 3- Flip image horizontally
def flip_horizontally(imgORG, fun_name):
    global img2
    img2= cv.flip(imgORG, 1)
    plot_images(imgORG, img2, title_2=fun_name)

 #____________________________________________    
# function 4- Crop the image to half size to middle
def crop(imgORG, fun_name):
    global img2
    width, lenght, _ =imgORG.shape
    widht1 = width//4
    widht2 = width//4*3
    lenght1 = lenght//4
    lenght2 = lenght//4*3
    if len(imgORG.shape) == 3:
        img2= imgORG[widht1:widht2 , lenght1:lenght2, :]
    elif len(imgORG.shape) < 3:
        img2= imgORG[widht1:widht2 , lenght1:lenght2]
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 5- Plot histogram for the GRAYSCALED image
def plot_histogram(imgORG, fun_name):
    global img2
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        imgORG= imgORG

    global histogram
    hist = cv.calcHist([imgORG],[0], None, [256], [0,256])
    intensity_values = np.array([x for x in range(256)])
    
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow(imgORG, cmap="gray")
    plt.title('GRAY SCALE')
    plt.subplot(1, 2, 2)
    histogram= plt.bar(intensity_values, hist[:,0], width = 5)
    plt.title('Histogram')
    plt.show()
    print(type(histogram))

#____________________________________________    
# function 6- Increase contrast and brightness
def increse_contrast_and_brightness(imgORG, fun_name):
    global img2
    img2 = cv.convertScaleAbs(imgORG, alpha=1, beta=30)
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 7- Decrease contrast and brightness
def decrease_contrast_and_brightness(imgORG, fun_name):
    global img2
    img2 = cv.convertScaleAbs(imgORG, alpha=.8, beta=-30)
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 8- Scale image horizontally
def scale_horizontally(imgORG, fun_name):
    global img2
    img2= cv.resize(imgORG, None, fx=2, fy=1, interpolation=cv.INTER_AREA)
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 9- Pixelate image
def pixelate(imgORG, fun_name):
    global img2
    img2= cv.resize(imgORG, (50,50), fx=1, fy=1, interpolation=cv.INTER_AREA)
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 10- Translate image horizontally
def translate_horizontally(imgORG, fun_name):
    global img2
    M = np.float32([[1, 0, 300], [0, 1, 0]])
    rows, cols = imgORG.shape[:2]
    img2 = cv.warpAffine(imgORG, M, (rows+300, cols))
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 11- Rotate image 90 degree
def rotete_90_degree(imgORG, fun_name):
    global img2
    rows, cols = imgORG.shape[:2]
    x= cols//2 - 1
    y= rows//2 - 1
    M = cv.getRotationMatrix2D(center=(x, y), angle=90, scale=1)

    abs_cos = abs(M[0,0]) 
    abs_sin = abs(M[0,1])
    bound_w = int(rows * abs_sin + cols * abs_cos)
    bound_h = int(rows * abs_cos + cols * abs_sin)
    M[0, 2] += bound_w/2 - x
    M[1, 2] += bound_h/2 - y

    img2= cv.warpAffine(imgORG, M, (bound_w, bound_h))
    plot_images(imgORG, img2, title_2=fun_name)

#____________________________________________    
# function 12- Apply histogram equalization
def apply_histogram_equalization(imgORG, fun_name):
    global img2
    # check if imgORG is gray or not (can't convert gray to gray) 
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        pass
    img2 = cv.equalizeHist(imgORG)

    intensity_values=np.array([x for x in range(256)])
    plt.subplot(1, 4, 1)
    plt.imshow(imgORG, cmap='gray')
    plt.title("Gray Scale")
    plt.subplot(1, 4, 2)
    plt.imshow(img2, cmap='gray')
    plt.title(fun_name)
    plt.subplot(1, 4, 3)
    plt.bar(intensity_values, cv.calcHist([imgORG],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title("Gray Scale")
    plt.subplot(1, 4, 4)
    plt.bar(intensity_values, cv.calcHist([img2],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(fun_name)
    plt.show()  

#____________________________________________    
# function 13- Apply adabtive threshold
def apply_adaptive_threshold(imgORG, fun_name):
    global img2
    # check if imgORG is gray or not (can't convert gray to gray) 
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        pass
    ret, img2 = cv.threshold(imgORG,125,255, cv.THRESH_OTSU+cv.THRESH_TOZERO_INV)

    intensity_values=np.array([x for x in range(256)])
    plt.subplot(1, 4, 1)
    plt.imshow(imgORG, cmap='gray')
    plt.title("Gray Scale")
    plt.subplot(1, 4, 2)
    plt.imshow(img2, cmap='gray')
    plt.title(fun_name)
    plt.subplot(1, 4, 3)
    plt.bar(intensity_values, cv.calcHist([imgORG],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title("Gray Scale")
    plt.subplot(1, 4, 4)
    plt.bar(intensity_values, cv.calcHist([img2],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(fun_name)
    plt.show()  

#____________________________________________    
# function 14- Apply Low pass filter
def low_pass_filter(imgORG, fun_name):
    global img2
    kernel = np.ones((6,6))/36
    img2= cv.filter2D(imgORG, ddepth=-1, kernel=kernel)
    noisy_image= noised(imgORG)
    img2_noise= cv.filter2D(noisy_image, ddepth=-1, kernel=kernel)
    plot_images4(imgORG, img2, noisy_image, img2_noise, title_2=fun_name)

#____________________________________________    
# function 15- Apply Gaussian filter
def gaussian_filter(imgORG, fun_name):
    global img2
    img2= cv.GaussianBlur(imgORG,(5,5),sigmaX=4,sigmaY=4)
    noisy_image= noised(imgORG)
    img2_noise= cv.GaussianBlur(noisy_image,(5,5),sigmaX=4,sigmaY=4)
    plot_images4(imgORG, img2, noisy_image, img2_noise, title_2=fun_name)

#____________________________________________    
# function 16- Apply Median filter
def median_filter(imgORG, fun_name):
    global img2
    img2= cv.medianBlur(imgORG, 15)
    noisy_image= noised(imgORG)
    img2_noise= cv.GaussianBlur(noisy_image,(5,5),sigmaX=4,sigmaY=4)
    plot_images4(imgORG, img2, noisy_image, img2_noise, title_2=fun_name) 

#____________________________________________    
# function 17- Apply Erosion
def erasion(imgORG, fun_name):
    global img2
    # check if imgORG is gray or not (can't convert gray to gray) 
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        pass
    kernel = np.ones((5,5), np.uint8)
    img2 = cv.erode(imgORG, kernel, iterations=1)
    plot_images(imgORG, img2, title_1= "Gray Scale", title_2=fun_name)

#____________________________________________    
# function 18- Apply Dilation
def dilation(imgORG, fun_name):
    global img2
    # check if imgORG is gray or not (can't convert gray to gray) 
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        pass
    kernel = np.ones((5,5), np.uint8)
    img2 = cv.dilate(imgORG, kernel, iterations=1)
    plot_images(imgORG, img2, title_1= "Gray Scale", title_2=fun_name)

#____________________________________________    
# function 19- Apply Sobel edge detection
def sobel(imgORG, fun_name):
    global img2
    if len(imgORG.shape) == 3:
        imgORG= cv.cvtColor(imgORG, cv.COLOR_BGR2GRAY)
    elif len(imgORG.shape) < 3:
        pass
    img2= cv.GaussianBlur(imgORG, (3,3), sigmaX=.1, sigmaY=.1)
    grad_x= cv.Sobel(img2, ddepth=cv.CV_16S, dx=1, dy=0, ksize=3)
    grad_y= cv.Sobel(img2, ddepth=cv.CV_16S, dx=0, dy=1, ksize=3)
    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    img2= cv.addWeighted(abs_grad_x, .5, abs_grad_y, .5, 0)

    plot_images(imgORG, img2, title_1= "Gray Scale", title_2=fun_name)