from SimpleCV import Image, Camera
import time

cam = Camera(0)
img = cam.getImage()
img.save("filename.jpg")
time.sleep(2)
img = cam.getImage()
img.save("filename2.jpg")
time.sleep(2)
img = cam.getImage()
img.save("filename3.jpg")
