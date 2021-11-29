from PIL import Image
from genPPL import generateOnePPL
import time

a = 13*8
b = 10*8


PPL_MAS = Image.new('RGBA', (10*a, 13*b), color = (0, 0, 0, 0))

t1 = time.time()

for i in range(a):
    for j in range(b):
        PPL = generateOnePPL()
        PPL_MAS.paste(PPL, (i*10, j*13))

print(time.time() - t1)

PPL_MAS.save('PPL_104x80_0.png', 'PNG')
PPL_MAS.show()

