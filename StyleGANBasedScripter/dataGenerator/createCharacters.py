"""
Character generator- A script to generate images of characters from different scripts.
"""

## Import libraries
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import filecmp

## Image details
imgSize = (32, 32)  # image size
imgSize = (128, 128)
offset = (8, 0)     # offset to centralize
offset = (32, 32)
colorRange = (256, 256, 256)
colorBlack = (0, 0, 0)

## Font details
font = "Arial Unicode.ttf"  # font file used
fontSize = 16
fontSize = 64

## Character details
# number of characters to randomly select per block
charPerBlock = 256

## Directory details
dir = "script_jpgs"
if not os.path.exists(dir):
	os.makedirs(dir)

# generated from wikipedia

# unicode_ranges = [["0000", "007F", "Basic Latin[g]", "128", "128", "Latin (52 characters), Common (76 characters)"]]
unicode_ranges = [["0061", "007B", 'English lowercase alphabets'], ["0590", "05FF", "Hebrew", "112", "88", "Hebrew"], ["0600", "06FF", "Arabic", "256", "255", "Arabic (237 characters), Common (6 characters), Inherited (12 characters)"], ["0700", "074F", "Syriac", "80", "77", "Syriac"], ["0750", "077F", "Arabic Supplement", "48", "48", "Arabic"], ["0900", "097F", "Devanagari", "128", "128", "Devanagari (122 characters), Common (2 characters), Inherited (4 characters)"], ["0980", "09FF", "Bengali", "128", "96", "Bengali"], ["0C80", "0CFF", "Kannada", "128", "89", "Kannada"], ["0D00", "0D7F", "Malayalam", "128", "117", "Malayalam"], ["0B80", "0BFF", "Tamil", "128", "72", "Tamil"], ["0C00", "0C7F", "Telugu", "128", "98", "Telugu"]]
# unicode_ranges = [["0061", "007B", 'English lowercase alphabets'], ["0590", "05FF", "Hebrew", "112", "88", "Hebrew"]]

letter = chr(10)
empty = os.path.join(dir, "empty.jpg") # get empty to use a reference for when the script didn't render a character
image = Image.new('RGB', imgSize, colorRange)
draw = ImageDraw.Draw(image)
draw.text(offset, letter, font=ImageFont.truetype(font, fontSize), fill=colorBlack)
image.save(empty, "JPEG")

letter = chr(1)
unsupported = os.path.join(dir, "unsupported.jpg") # get unsupported to use a reference for when the script didn't render a character
image = Image.new('RGB', imgSize, colorRange)
draw = ImageDraw.Draw(image)
draw.text(offset, letter, font=ImageFont.truetype(font, fontSize), fill=colorBlack)
image.save(unsupported, "JPEG")


for scriptType in unicode_ranges:
	for letterIdx in range(int(scriptType[0], 16), int(scriptType[1], 16)):
		imgName = os.path.join(dir, str(letterIdx) + ".jpg")
		letter = chr(letterIdx)
		image = Image.new('RGB', imgSize, colorRange)
		draw = ImageDraw.Draw(image)
		draw.text(offset, letter, font=ImageFont.truetype(font, fontSize), fill=colorBlack)
		image.save(imgName, "JPEG")
		if filecmp.cmp(imgName, empty) or filecmp.cmp(imgName, unsupported):
			os.remove(imgName)
