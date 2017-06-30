import PIL
from PIL import ImageFont, Image, ImageDraw

font = ImageFont.truetype("/Users/user/Documents/Projects/Ultra_Memer/chinese_font.ttf", 48)
img = Image.open("greenT.png")
# img=Image.new("RGBA", (200,200),(120,20,20))
draw = ImageDraw.Draw(img)
draw.text((200, 200),"你说啥",(43,43,43),font=font)
draw = ImageDraw.Draw(img)
draw = ImageDraw.Draw(img)
img.save("a_test.png")

# target_img = Image.open("greenT.png")
