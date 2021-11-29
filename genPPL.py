from PIL import Image
from randFile import randModulPathFile, recolorModul

def generateOnePPL():
    PPL = Image.new('RGBA', (10, 13), color = (0, 0, 0, 0))

    SKIN = Image.open(randModulPathFile("SKIN"))
    EYES = Image.open(randModulPathFile("EYES"))
    SHIRT = Image.open(randModulPathFile("SHIRT"))
    SHOES = Image.open(randModulPathFile("SHOES"))
    SHORT = Image.open(randModulPathFile("SHORT"))
    HAIR = Image.open(randModulPathFile("HAIR"))

    PPL = Image.alpha_composite(PPL, SKIN)
    PPL = Image.alpha_composite(PPL, recolorModul(EYES))
    PPL = Image.alpha_composite(PPL, recolorModul(HAIR))

    PPL = Image.alpha_composite(PPL, recolorModul(SHORT))
    PPL = Image.alpha_composite(PPL, recolorModul(SHOES))
    PPL = Image.alpha_composite(PPL, recolorModul(SHIRT))

    return PPL
