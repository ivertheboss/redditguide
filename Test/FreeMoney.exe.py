import Video
import os
from plyer import notification

while True:
    temp = input("How many videos do you want to generate?")
    if temp[0] != "c":
        print("Estimated time: "+str((int(temp)*55)/60), "mins.")
        print("Loading...")
        dir = 'Videos'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        for x in range(int(temp)):
            try:
                Video.makeVideo(x)
            except:
                try:
                    Video.makeVideo(x)
                except:
                    try:
                        Video.makeVideo(x)
                    except:
                        try:
                            Video.makeVideo(x)
                        except:
                            try:
                                Video.makeVideo(x)
                            except:
                                try:
                                    Video.makeVideo(x)
                                except:
                                    Video.makeVideo(x)
                    Video.makeVideo(x)
        print("Videos ready!")
        notification.notify(
            title="Free Money Generator",
            message="Videos are done",
            app_name="FreeMoney.exe",
        )
    else:
        Video.compile(int(temp[4] + temp[5]))
