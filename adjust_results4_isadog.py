#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Harini Sri
# DATE CREATED: 10-07-2024                             
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog'. This function modifies
    the results dictionary in place.
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Each list contains:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) where 1 = match between pet image
                               and classifier labels, 0 = no match between labels
                    The function will add:
                      index 3 = 1/0 (int) where 1 = pet image 'is-a' dog,
                               0 = pet Image 'is-NOT-a' dog
                      index 4 = 1/0 (int) where 1 = Classifier classifies image 
                               'as-a' dog, 0 = Classifier classifies image 
                               'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
    """
    # Read in the dog names from dognames.txt into a dictionary
    dognames_dic = {}
    with open(dogfile, 'r') as file:
        for line in file:
            dog_name = line.strip()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(f"Warning: Duplicate dog name found in {dogfile}: {dog_name}")
    
    # Iterate through results_dic and update index 3 and index 4
    for key in results_dic:
        pet_label = results_dic[key][0].lower()  # Pet image label
        classifier_label = results_dic[key][1].lower()  # Classifier label
        
        # Determine if labels are dogs
        results_dic[key].append(1 if dognames_dic.get(pet_label, 0) else 0)  # Index 3
        results_dic[key].append(1 if dognames_dic.get(classifier_label, 0) else 0)  # Index 4
