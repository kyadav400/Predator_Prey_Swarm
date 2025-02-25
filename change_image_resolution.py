#python program to change the resolutions of image
from PIL import Image
import os

f = r'/Users/kunal/Documents/NN_project/Images/lig2' # Directory containing the images

#reading tje files in the directory and looping through it
for file in os.listdir(f):
    f_img = f+"/"+file              # read the image file
    img = Image.open(f_img)         #open the image
    img = img.resize((800,600))     # resize the image: height X width
    img.save(f_img)                 # save the image
