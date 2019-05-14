# -*- coding: utf-8 -*-

import dataiku
from dataiku.customrecipe import *
import dataiku
import os
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from google_images_download import google_images_download

# Config destination folder for the images
images_folder = dataiku.Folder(get_output_names_for_role('images_folder')[0])
images_folder_path = images_folder.get_path()
images_info = images_folder.get_info()

# Class instantiation
response = google_images_download.googleimagesdownload()

#creating list of arguments with parameters given by the user
arguments = {
         "keywords": get_recipe_config().get('keywords'),
         "limit": get_recipe_config().get('limit', 20),
         "print_urls": True,
         "format": get_recipe_config().get('format'),
         "color_type": get_recipe_config().get('color_type'),
         "output_directory": images_folder_path,
         "silent_mode": True
        }
# passing the arguments to the function and get the list of images path
_ = response.download(arguments)


            


