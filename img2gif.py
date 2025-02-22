"""
GIF Converter

****************************************************
*                                                  *
*              THIS SCRIPT MUST GO IN THE          *
*                   SAME EXACT FOLDER              *
*              AS THE IMAGE(S) TO CONVERT          *
*              RUN THIS SCRIPT AND FOLLOW          *
*                 COMMAND LINE PROMPTS             *
*                                                  *
****************************************************

Made by: Dr. Z 
Created: Jan 22, 2020

Modified: 
    Dec 6, 2021 - gives users options of task & quit options. Updated string syntax. Fixed scale error.
    Oct 13, 2021 - added explanation prompts, changed order of actions, and keeps transparent background preservation (for use with .pngs)
    Nov 20, 2020 - now allows shrink scaling (removes TypeError for fraction
        scales like 0.5)

This script will prompt users for the name of their file, then convert it to a
.gif and save it. For this script to run properly, the working directory 
(upper right corner) MUST be the same as the file! 

          RUN THE CODE & ANSWER PROMPTS THAT APPEAR IN THE COMMAND LINE ga--->
"""

#modified from https://mail.python.org/pipermail/python-list/2000-May/036017.html
from PIL import Image 
import PIL
import sys, os, ast

def convertImg(imgName):
    ''' Converts image transparency into gif. 
    From https://stackoverflow.com/questions/46850318/transparent-background-in-gif-using-python-imageio'''
    im = Image.open(imgName)
    try:
        alpha = im.getchannel('A')
        # Set all pixel values below 128 to 255, and the rest to 0
        mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
    except ValueError:
        mask = None

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)


    if mask:
        # Paste the color of index 255 and use alpha as a mask
        im.paste(255, mask)

        # The transparency index is 255
        im.info['transparency'] = 255

    return im

def saveGif(img):
    # convert transparency
    if transparency and img.mode=='P':
        img.convert('RGBA', palette=Image.ADAPTIVE).save(outputName, transparency=255) #convert to filetype and save
    elif img.mode=='L':
        # Grayscale
        img.convert('RGB', palette=Image.ADAPTIVE).save(outputName) #convert to filetype and save

    else:
        # img = convertImg(name)
        img.convert(palette=Image.ADAPTIVE)
        img.save(outputName)
        #img.convert('RGBA',palette=Image.ADAPTIVE).save(outputName)
    print('Saved in the current working folder. Have a nice day!')

try:
    name = input("What is the name of the image you'd like to convert? (Please include the extension, no quotes around text!)\n ")
    outputName = name[:name.find('.')] +'.gif' #change name for output

    #do the magic
    img = Image.open(name)
    print(img.mode)
    keys = img.info.keys()
    if 'transparency' in keys:
        transparency = str(img.info["transparency"])
    else:
        transparency = []
        
    print("\n This tool updates your image. To keep the same, and just convert to a gif, type n. \n")
    print("  SCALE keeps the proportions, but allows the image to be made bigger (>1) or smaller (<1).")
    print("  RESIZE allows you to set and strech the image by entering in integer dimension sizes (w, h).\n")
    # decideScale = input("Do you want to SCALE this image? (keep proportions) (Y/n) ")
    
    w,h = img.size
    print(f"\n Your image size is {w},{h}.")
    decide = input("What do you want to do with your image? \n"+
                   "Type s for Scale, r for resize, \n"+
                   " N for nothing (converts to gif) and q to quit.")
    
    
    # decideSize = input("Do you want to RESIZE this image (set dimensions, don't keep proportions)? (Y/n) ")
   
    # adjust sizing
    if decide.lower()=='r':
        size = input("Enter your image pixel size as: width,height (in integers please!) "  )
        img = img.resize(ast.literal_eval(size), resample=PIL.Image.BICUBIC)
        saveGif(img)
        
    elif decide.lower()=='s':
        scale =float(input("Enter desired scale value. (Ex: 2 will scale twice the size, 0.5 will half it)  \n"))
        img = img.resize((int(img.size[0]*scale), int(img.size[1]*scale)), resample=PIL.Image.BICUBIC)
        print(f"New image size is {img.size}.")
        saveGif(img)
        
    elif decide.lower() in ['q','n']:
        sys.stdout.write("\033[1;34m" ) #Blue
        print('Good-bye!')
        
    elif decide.lower()!='n':
        print("You have entered an invalid entry. Please run the script again.")

except FileNotFoundError:
    print( "\nSorry, there's no file by that name.")
    sys.stdout.write("\033[1;31m" ) #Red
    print("Your current working folder is: " + os.getcwd())
    print("Which contains:")
    sys.stdout.write("\033[0;0m") #Black
    print(os.listdir())
    sys.stdout.write("\033[1;34m" ) #Blue
    print("\nPlease check your spelling and working directory, and run this code again!")
    sys.stdout.write("\033[0;0m") #Black
    
    #colors from https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python/37340245