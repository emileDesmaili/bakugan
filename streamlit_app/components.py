#library imports





import streamlit as st



import json

import pandas as pd
import requests

from jmd_imagescraper.core import *
import glob
from PIL import Image
import os, stat
import cv2








  
    
    
def scrape_images(anime, max_results=50):
    """method to scrape images from duckduckgo and save them

    Returns:
        
    """
    query = anime + ' anime characters'

    params = {
    "max_results": max_results,
    "img_size":    ImgSize.Cached, 
    "img_type":    ImgType.Photo,
    "img_layout":  ImgLayout.Square,
    "img_color":   ImgColor.All,
    "uuid_names": True
    }

    duckduckgo_search('data/raw/images', anime,query, **params)

def display_images(anime, max_results=50):
    """methods to display image in streamlit page

    Args:
        max_results (int, optional): number of scraped images. Defaults to 50.
    """
    
    path = 'data/raw/images/' + anime
    globpath = path + '/*.jpg'
    images = glob.glob(path)
    image_list = []

    #scrape only if directory doesn't exist
    if not os.path.isdir(path):
        scrape_images(anime)
    for img in glob.glob(globpath):
        image_list.append(cv2.imread(img))
    cols = st.columns(len(image_list))
    for a, x in enumerate(cols):
        with x:
            st.image(image_list[a], use_column_width=False, width=250, channels = 'BGR')




    









