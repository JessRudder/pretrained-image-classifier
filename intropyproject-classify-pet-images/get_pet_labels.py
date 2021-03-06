#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Jessica Rudder
# DATE CREATED: 2019-03-02
# REVISED DATE: 2019-03-09
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # Imports only listdir function from OS module

    # Retrieve the filenames from folder pet_images/
    results_dic = {}
    filename_list = listdir(image_dir)

    for name in filename_list:
      results_dic[name] = results_dic.get(name, create_label_from_filename(name))

    return results_dic

def create_label_from_filename(filename):
  """
  Takes a filename and turns it into a list with a single lowercase string
  containing the pet label that is in the filename
  (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
  Parameters:
   filename - The filename (string)
  Returns:
    List with filename turned into lowercase string stripped of numbers and
    extensions (e.g. 'Boston_terrier_02259.jpg' => ['boston terrier'])
  """
  name_list = filename.split("_")[:-1]

  for idx in range(0, len(name_list)):
    name_list[idx] = name_list[idx].lower()

  return [" ".join(name_list)]
