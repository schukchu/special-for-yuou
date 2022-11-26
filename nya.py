from moviepy.editor import *
import os
from PIL import Image, ImageDraw, ImageFont

def create():
    im = Image.open('C:/Users/student/Downloads/всё/e956ab_53c4f95aa5a796043562ec252ca.jpg')
    font = ImageFont.truetype('C:/Windows/Fonts/ebrima.ttf', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100,100),
        'И тебя вылечат',
        font=font,
        fill=('#1C0606')
        )
    im.save('C:/Users/student/Documents/pythonProject278')

create()

directory = 'C:/Users/student/Documents/pythonProject278'
files = os.listdir(directory)
imges = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in imges]

final_clip = concatenate_videoclips(clips, method = 'compose')
final_clip.write_videofile('testik.mp4', fps = 24)
