import subprocess
import os
import locale
import glob
encoding = locale.getdefaultlocale()[1]

def get_code(file):
	# if there is no QR code in the image, or if for some reason zbar can't read the code
	# then it will throw an error, so I use try/except to handle that error gracefully
	# images like this will be put in a folder called "unreadable_code"
	try:
		raw_code = subprocess.check_output(["C:\\Program Files (x86)\\ZBar\\bin\\zbarimg", "-q", \
		file])
		raw_code = raw_code.rstrip()
		raw_code = raw_code.decode(encoding)
		code = raw_code.split(':',1)[1]
		return(code)
	except:
		return("unreadable_code")

# edit this to specify which kinds of image files
# you want it to look at
image_files=glob.glob('*.JPG') + glob.glob('*.png')
print(image_files)

for file in image_files:
 # make the file into a path
 file_path = os.path.join(os.getcwd(), file) 
 # get the code
 code = get_code(file)
 # make the folder
 # you could edit here and make it rename the file
 # instead of a new folder, or make it name the folders
 # in some other way
 folder = os.path.join(os.getcwd(), code)
 os.makedirs(folder, exist_ok=True)
 #move the file
 os.rename(file_path, folder + "\\" + file)
 #done
