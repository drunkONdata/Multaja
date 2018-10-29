import numpy as np
import mimetypes
from PIL import Image
import numpy as np
from spectral import *
import pandas as pd
from math import sqrt
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray

def load_image(directory):
    '''
    Loads an image from a specified directory and encodes it into a numpy array

    Args:
        directory: The location of the image file as a string

    Returns:
        The specified image as a numpy array
    '''
    im = Image.open(directory)
    return np.array(im)

def binarize_img(imarray, threshold=0):
    '''
    Clusters the pixles from the input numpy array then binarizes them

    Args:
        imarray: image as a numpy array
        threshold: The max value a number can have without being set to 1

    Returns:
        A binarized version of the input image
    '''
    m, c = kmeans(imarray, 10, 100)
    filteredm = np.copy(m)
    filteredm[filteredm>threshold] = 1
    return filteredm

def generate_blobs(imarray, blob_type = 'dog'):
    '''
    Generates blobs from an image using the specified blobbing method

    Args:
        imarray: The image blobs will be found for as a numpy array
        blob_type: The blobbing method to be used in generateing blobs

    Returns:
        A list of tubles containing the coordinate and standard deviation for
        that blob
    '''
    image_gray = rgb2gray(imarray)
    if blob_type == 'log':
        blobs = blob_log(image_gray)
        #blob_log(image_gray, min_sigma=.01, max_sigma=10, num_sigma=5, threshold=.01)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
    elif blob_type == 'dog':
        blobs = blob_dog(image_gray, min_sigma=.5, max_sigma=5, threshold=.1)
        blobs[:, 2] = blobs[:, 2] * sqrt(2)
    else:
        blobs = blob_doh(image_gray, max_sigma=5, threshold=.01)
    return blobs

def get_im_metrics(directory, blob_type= 'dog'):
    '''
    Returns blob count and percentage of settlment coverage from a specified
    picture

    Args:
        directory: The path to the image as a string
        blob_type: The blobbing method to be used in generateing blobs

    Returns:
        A tuble containing the number of blobs as an int and the percentage of
        settlment coverage as a float
    '''
    imarray = load_image(directory)
    bi_img = binarize_img(imarray)
    settlement_perc = np.sum(1-bi_img)/bi_img.size
    blobs = generate_blobs(imarray, blob_type)
    return len(blobs), settlement_perc

if __name__ == '__main__':
    blob_count, settlement_perc = get_im_metrics('images/rukban_demo.png')

    print(f'{blob_count} settlements with a settlement percentage of {settlement_perc*100}%')
