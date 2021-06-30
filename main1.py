import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('run.jpg')
img = np.float32(img) / 255.0

gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

bin_n = 16
bin = np.int32(bin_n*angle/(2*np.pi))
print(bin.shape)
type(bin)
bin_cells = bin[:10,:10], bin[10:,:10], bin[:10,10:], bin[10:,10:]
mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
# print(hists)
# hist = np.hstack(hists)
# print(hist)




