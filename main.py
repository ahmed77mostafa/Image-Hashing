import sys

import cv2
import numpy

sys.set_int_max_str_digits(100000000)
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

pixels = gray_image.flatten().astype(str)

compressed_data = numpy.array(encoding(pixels), dtype = numpy.uint8)
numpy.save("Compressed_image_new.bmp", compressed_data)

decompressed_data = decoding(compressed_data, gray_image.shape)
cv2.imwrite("C:/Users/Ahmed mostafa/PycharmProjects/Image-Hashing/images",decompressed_data)

print("Compression complete. Decompressed image saved as 'Compressed_image_new.bmp'.")

