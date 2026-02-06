# computer_vision.py

from PIL import Image
import numpy as np

def person_detected(image1_file, image2_file, t1):
    """
    Takes in image1 and image2 locations and t1
    Returns a Boolean indicating if a "person" is in the image based on t1
    """
    img1 = Image.open(image1_file)
    img2 = Image.open(image2_file)
    
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    difference = np.abs(arr1 - arr2)
    
    total_difference = np.sum(difference)
    
    if total_difference > t1:
        return True
    else:
        return False