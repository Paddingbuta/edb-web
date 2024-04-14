from PIL import Image
img=Image.open('logo2.png')
box=(0,0,700,260)
cropped_img=img.crop(box)
cropped_img.save('logo3.png')