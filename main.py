import sys

import cv2
import numpy

sys.set_int_max_str_digits(1000000)
def encoding(string):
    encodedString = ''
    count = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count+=1
        else:
            encodedString += str(count) + str(string[i-1])
            count = 1

    if len(string) > 0:
        encodedString += str(count) + str(string[-1])
    return encodedString

def decoding(encodedString,shape):
    decoded_data = []
    for i in range(0,len(encodedString),2):
        value = encodedString[i]
        count = encodedString[i + 1]
        decoded_data.extend([value] * count)
    return numpy.array(decoded_data).reshape(shape)


image = cv2.imread("little nightmares2 wallpaper.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

width = int(gray_image.shape[1] * 0.5)
height = int(gray_image.shape[0] * 0.5)
dim = (width,height)
resized_image = cv2.resize(gray_image,dim,interpolation = cv2.INTER_AREA)

pixels = resized_image.flatten().tolist()

compressed_data = encoding(pixels)
numpy.save("compressed_image.npy", numpy.array(compressed_data,dtype=numpy.uint64))

decompressed_data = decoding(compressed_data,resized_image.shape)
cv2.imwrite("C:/Users/ahmed.mostafa/PycharmProjects/Image_Hashing/images",decompressed_data)

