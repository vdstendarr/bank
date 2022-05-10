from PIL import Image, ImageFont, ImageDraw 


title_font = ImageFont.truetype('ThaleahFat.ttf', 64)

for gems in range(201):
    background = Image.open("bank.png").convert("RGBA")
    W, H = background.size
    mod = int(64/16)
    border_color = "black"    
    quantity = str(gems)
    draw = ImageDraw.Draw(background)
    w, h = draw.textsize(quantity, font=title_font)
    print(w,h)
    x = (W/2)-w-8-14
    y = 196

    draw.text((x - mod, y - mod), f"{quantity}", font=title_font, fill=border_color)
    draw.text((x + mod, y - mod), f"{quantity}", font=title_font, fill=border_color)
    draw.text((x - mod, y + mod), f"{quantity}", font=title_font, fill=border_color)
    draw.text((x + mod, y + mod), f"{quantity}", font=title_font, fill=border_color)
    draw.text((x, y), quantity, fill="white", font=title_font)

    filename = f'{gems}.png'
    background.save(filename)