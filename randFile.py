import os, random
from PIL import Image, ImageDraw
import numpy as np

def randModulPathFile(MODUL):
    allfiles=os.listdir(os.getcwd()+ f'\\modules\\{MODUL}')
    imlist=[f'modules/{MODUL}/'+filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]
    return(random.choice(imlist))

#print(randModulPathFile('EYES'))

def recolorModul(MODUL):
    color = tuple(np.random.choice(range(256), size=3))
    
    im = MODUL
    draw = ImageDraw.Draw(im)
    im1 = Image.new('RGB',(10,13), color)
    im.paste(im1, (0,0), im)
    return im

    


#im = Image.open(randModulPathFile('HAIR'))
#im = recolorModul(im)

#im.resize((100,130), resample=Image.BOX).show()
