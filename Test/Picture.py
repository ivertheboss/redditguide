from PIL import Image, ImageFont,  ImageDraw
from Sound import makeSound
import random
import numpy as np
import textwrap

def createPost(title_text, username_text):
    makeSound(title_text, "post")
    post = Image.open('RedditPostEmpty.png')
    image_editable = ImageDraw.Draw(post)
    title_font = ImageFont.truetype('NotoSans.ttf', 18)
    title_text1 = textwrap.wrap(str(title_text), width=65)
    y = 0
    for u in title_text1:
        image_editable.text((30, 30 + y), u, (225, 225, 225), font=title_font)
        y += 16
    title_font = ImageFont.truetype('NotoSans.ttf', 15)
    image_editable.text((205, 3), "u/"+username_text, (129, 131, 132), font=title_font)
    post.save("post.png")


def createComments(title_text, username_text):
    global pfp
    for x in range(len(title_text)):
        random2 = random.randrange(1, 28)
        pfp = Image.open('redditPic'+str(random2)+'.png').convert("RGB")
        npImage = np.array(pfp)
        h, w = pfp.size

        # Create same size alpha layer with circle
        alpha = Image.new('L', pfp.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)

        # Convert alpha Image to numpy array
        npAlpha = np.array(alpha)

        # Add alpha layer to RGB
        npImage = np.dstack((npImage, npAlpha))


        post = Image.open('RedditCommentEmpty.png')
        Image.Image.paste(post, Image.fromarray(npImage), (8, 10))
        post.save("temp1image_editable.png")
        post = Image.open('temp1image_editable.png')
        image_editable = ImageDraw.Draw(post)
        title_font = ImageFont.truetype('NotoSans.ttf', 18)
        title_text1 = textwrap.wrap(str(title_text[x]), width=65)
        y = 0
        for u in title_text1:
            image_editable.text((30, 45+y), u, (225, 225, 225), font=title_font)
            y += 16
        title_font = ImageFont.truetype('NotoSans.ttf', 15)
        image_editable.text((50, 13), username_text[x], (129, 131, 132), font=title_font)
        makeSound(title_text[x], "comment"+str(x+1))
        bg_colour = (26, 26, 27)
        if post.mode in ('RGBA', 'LA') or (post.mode == 'P' and 'transparency' in post.info):
            # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
            alpha = post.convert('RGBA').split()[-1]

            # Create a new background image of our matt color.
            # Must be RGBA because paste requires both images have the same format
            # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
            bg = Image.new("RGBA", post.size, bg_colour + (255,))
            bg.paste(post, mask=alpha)
        bg.save("comment"+str(x+1)+".png")
