# QR/Bar Code Sorter
## Sort images based on a QR/Bar code!

A simply python script which uses zbar (the windows app, not the library) to sort images into folders based on a QR code in the image.

This uses the [zbar](the http://zbar.sourceforge.net/) application (Windows/Linux only) to read the QR codes. I couldn't get the zbar module to work in python 3 so I just used the application itself.

##To use:
Just put the script in the folder full of images and run it. It will make folders for each unique code and put the images with that code in it. If it can't find an code in an image, or otherwise can't read it, it will put those images in an "unreadable_code" folder. You will need to have zbar installed on your machine and have it in your PATH.

##Potential Improvements:
- arguments to control whether it sorts into folders or just renames the files in situ.
- zbar struggles sometimes if the image isn't white-balanced well, adding some [ImageMagick](http://www.imagemagick.org/) would make this a little more robust.