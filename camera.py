# Some code in this file is based on
# https://github.com/dgaletic/SimpleCV-image-stitcher/blob/master/stitch_sample.py

from numpy import vstack,hstack
import os
import SimpleCV
import time


class Camera:
    def __init__(self):
        self.camera = SimpleCV.Camera(0)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print "Exited camera"

    def snap(self):
        img = self.camera.getImage()
        img.save("file.png")
        return img

    # Without this 0.5 sec sleep, the first image my camera takes is very dark,
    # I suppose the issue is it not calibrating fast enough after turning on?
    # time.sleep(0.5)

    # matrices = []
#
    # for i in range(10):
    #     img = c.getImage()
    #     matrices.append(img.getNumpy())
    #     time.sleep(0.5)
#
    # mat = vstack(matrices)
    # img_stitched = SimpleCV.Image(mat)
    # img_stitched.save("stitched_h.png")
#
    # mat = hstack(matrices)
    # img_stitched = SimpleCV.Image(mat)
    # img_stitched.save("stitched_v.png")
#
    # print "Images saved in", os.getcwd()
