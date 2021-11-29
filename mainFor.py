from PIL import Image
from genPPL import generateOnePPL
import random

for i in range(3):
    PPL = generateOnePPL()

    PPL = PPL.resize((100,130), resample=Image.BOX)
    PPL.save(f'PPL_{random.randint(1, 100000)}_{random.randint(1, 100000)}.png', 'PNG')
    #PPL.show()
