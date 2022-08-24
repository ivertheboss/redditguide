from moviepy.editor import *
import Picture
import random
import RedditAPI
import os


def makeVideo(y):
    data = RedditAPI.getData()
    clips = []
    Picture.createPost(data[0], data[1])

    postAudio = AudioFileClip("post.wav")
    postPicture_ = ImageClip("post.png").set_duration(postAudio.duration)
    Picture.createComments(data[2], data[3])
    commentAudio1 = AudioFileClip("comment1.wav")
    commentAudio2 = AudioFileClip("comment2.wav")
    commentAudio3 = AudioFileClip("comment3.wav")
    commentAudio4 = AudioFileClip("comment4.wav")
    commentPicture1_ = ImageClip("comment1.png").set_duration(commentAudio1.duration)
    commentPicture2_ = ImageClip("comment2.png").set_duration(commentAudio2.duration)
    commentPicture3_ = ImageClip("comment3.png").set_duration(commentAudio3.duration)
    commentPicture4_ = ImageClip("comment4.png").set_duration(commentAudio4.duration)
    empty = ImageClip("empty.png").set_duration(0.6)
    postPicture = postPicture_.set_audio(postAudio)
    commentPicture1 = commentPicture1_.set_audio(commentAudio1)
    commentPicture2 = commentPicture2_.set_audio(commentAudio2)
    commentPicture3 = commentPicture3_.set_audio(commentAudio3)
    commentPicture4 = commentPicture4_.set_audio(commentAudio4)
    clips.append(postPicture)
    clips.append(empty)
    clips.append(commentPicture1)
    clips.append(empty)
    clips.append(commentPicture2)
    clips.append(empty)
    clips.append(commentPicture3)
    clips.append(empty)
    clips.append(commentPicture4)
    music = AudioFileClip("music.wav")
    randomNum = random.randrange(1, 41)

    video = concatenate_videoclips(clips, method="compose")
    minecraft = VideoFileClip("game"+str(randomNum)+".mp4", audio=False).subclip(0, video.duration)

    final_video = CompositeVideoClip([minecraft, video.set_position((0, 0.4), relative=True)])
    final_video.audio = CompositeAudioClip([final_video.audio, music.set_end(final_video.end)])

    final_video.write_videofile(
        "Videos/Reddit Guide AskReddit #shorts #reddit #askreddit "+str(y+1)+".mp4",
        fps=60,
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
        threads=6,
    )


def compile(x):
    final = []
    for x in range(x):
        final.append(VideoFileClip("Videos/Reddit Guide AskReddit #shorts #reddit #askreddit "+str(x+1)+".mp4",))
    final = concatenate_videoclips(final)
    final.write_videofile("Videos/Reddit Video YT SHORTS COMPILATION (r ̸AskReddit).mp4")
