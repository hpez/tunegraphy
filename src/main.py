import math
import time

from scipy import signal
from scipy.io import wavfile
import cv2

t1 = time.time()

sample_rate, samples = wavfile.read('/home/hassan/PycharmProjects/untitled/I Love You More.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

hFrequencies = []
maxAmp = 0
minAmp = 1000000
maxFreq = 0
minFreq = 1000000
for i in range(0, times.size):
    maxAmpT = 0
    mft = 0
    for j in range(0, frequencies.size):
        mft += spectrogram[j, i] * frequencies[j]
        if spectrogram[j, i] > maxAmpT:
            maxAmpT = spectrogram[j, i]
    maxAmp = max(maxAmpT, maxAmp)
    minAmp = min(maxAmpT, minAmp)
    maxFreq = max(mft, maxFreq)
    minFreq = min(mft, minFreq)
    hFrequencies.append((mft, maxAmpT))

imgLU = cv2.imread("/home/hassan/PycharmProjects/untitled/untitled.png", cv2.IMREAD_COLOR)
imgRU = cv2.imread("/home/hassan/PycharmProjects/untitled/untitled.png", cv2.IMREAD_COLOR)
imgLD = cv2.imread("/home/hassan/PycharmProjects/untitled/untitled.png", cv2.IMREAD_COLOR)
imgRD = cv2.imread("/home/hassan/PycharmProjects/untitled/untitled.png", cv2.IMREAD_COLOR)
height, width, channels = imgLU.shape

for (t, (f, a)) in enumerate(hFrequencies):
    hsv = (
        180 - math.floor((((f - minFreq) / (maxFreq - minFreq)) * 180)), (math.floor(((a - minAmp) / (maxAmp - minAmp)) * 100.0) + 155), 255)
    cv2.circle(imgLU, (0, 0), math.floor(t), hsv, 2)

for (t, (f, a)) in enumerate(hFrequencies):
    hsv = (
        180 - math.floor((((f - minFreq) / (maxFreq - minFreq)) * 180)), (math.floor(((a - minAmp) / (maxAmp - minAmp)) * 100.0) + 155), 255)
    cv2.circle(imgRU, (-width, 0), math.floor(t), hsv, 2)

for (t, (f, a)) in enumerate(hFrequencies):
    hsv = (
        180 - math.floor((((f - minFreq) / (maxFreq - minFreq)) * 180)), (math.floor(((a - minAmp) / (maxAmp - minAmp)) * 100.0) + 155), 255)
    cv2.circle(imgLD, (0, -height), math.floor(t), hsv, 2)

for (t, (f, a)) in enumerate(hFrequencies):
    hsv = (
        180 - math.floor((((f - minFreq) / (maxFreq - minFreq)) * 180)), (math.floor(((a - minAmp) / (maxAmp - minAmp)) * 100.0) + 155), 255)
    cv2.circle(imgRD, (-width, -height), math.floor(t), hsv, 2)

imgLU = cv2.cvtColor(imgLU, cv2.COLOR_HSV2RGB)
imgLD = cv2.cvtColor(imgLD, cv2.COLOR_HSV2RGB)
imgRU = cv2.cvtColor(imgRU, cv2.COLOR_HSV2RGB)
imgRD = cv2.cvtColor(imgRD, cv2.COLOR_HSV2RGB)

cv2.namedWindow('LU', cv2.WINDOW_NORMAL)
cv2.imshow('LU', imgLU)

cv2.namedWindow('LD', cv2.WINDOW_NORMAL)
cv2.imshow('LD', imgLD)

cv2.namedWindow('RU', cv2.WINDOW_NORMAL)
cv2.imshow('RU', imgRU)

cv2.namedWindow('RD', cv2.WINDOW_NORMAL)
cv2.imshow('RD', imgRD)

print(time.time() - t1)
cv2.waitKey(0)
cv2.destroyAllWindows()
