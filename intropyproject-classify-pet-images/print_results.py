#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Jessica Rudder
# DATE CREATED: 2019-03-09
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """  
    # results_stats_dic = {
    #     "n_images": 0, # number of images
    #     "n_dogs_img": 0, # number of dog images X
    #     "n_notdogs_img": 0, # number of NON-dog images X
    #     "n_match": 0, # number of matches between pet & classifier labels X
    #     "n_correct_dogs": 0, # number of correctly classified dog images X
    #     "n_correct_notdogs": 0, # number of correctly classified NON-dog images X
    #     "n_correct_breed": 0, # number of correctly classified dog breeds X
    #     "pct_match": 0, # percentage of correct matches
    #     "pct_correct_dogs": 0, # percentage of correctly classified dogs
    #     "pct_correct_breed": 0, # percentage of correctly classified dog breeds
    #     "pct_correct_notdogs": 0, # percentage of correctly classified NON-dogs
    # }
    print("\n\n###### Stats for Run Using {} Model ######\n".format(model.upper()))
    print("Number of Images: {}".format(results_stats_dic["n_images"]))
    print("Number of Dog Images: {}".format(results_stats_dic["n_dogs_img"]))
    print("Number of 'Not-a' Dog Images: {}".format(results_stats_dic["n_notdogs_img"]))

    for key in results_stats_dic:
      if "pct" in key:
        key_label = key.replace("pct", "%").replace("_"," ").title()
        print("{}: {}".format(key_label, results_stats_dic[key]))

    # Labels are misclassified as dogs when both labels aren't in agreement regarding 
    # whether or not an image is of a dog.
    if print_incorrect_dogs:
      if (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']:
        print("\n\n###### Misclassified Dogs When Using {} Model ######\n".format(model.upper()))

        for key in results_dic:
          pet_info = results_dic[key]

          if pet_info[3] != pet_info[4]:
            if pet_info[3] == 1:
              print("{}: Pet Image Label is a Dog - Classified as NOT-A-DOG".format(pet_info[0].title()))
            else:
              print("{}: Pet Image Label is NOT-a-Dog - Classified as a-DOG".format(pet_info[0].title()))
      else:
        print("\n\n###### There were NO Misclassified Dogs When Using {} Model ######\n".format(model.upper()))

    # Labels have a misclassification of breeds of dog when both labels indicate that the 
    # image is a dog; but, labels aren't in agreement regarding the dog's breed.
    if print_incorrect_breed:
      if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\n\n###### Misclassified Breeds When Using {} Model ######\n".format(model.upper()))

        for key in results_dic:
          pet_info = results_dic[key]

          # ['beagle', 'foxhound', 0, 1, 1]
          if pet_info[3] == 1 and pet_info[4] == 1 and pet_info[2] == 0:
              print("Pet Label: {} vs Classifier Label: {}".format(pet_info[0], pet_info[1]))
      else:
        print("\n\n###### There were NO Misclassified Breeds When Using {} Model ######\n".format(model.upper()))
