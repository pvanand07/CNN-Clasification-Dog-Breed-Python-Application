#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: Anand Siva P V
# DATE CREATED: 21-11-2022
# REVISED DATE: 25-11-2022
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Defines get_input_args function
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """
    # Creates Parse using ArgumentParser

    parser = argparse.ArgumentParser()
    # Creates 3 command line arguments as mentioned above using add_argument() from ArguementParser method

    parser.add_argument(
        "--dir",
        type=str,
        default="pet_images/",
        help="path to the folder of pet images",
    )
    parser.add_argument(
        "--arch", type=str, default="resnet", help="type of CNN model architecture"
    )
    parser.add_argument(
        "--dogfile",
        type=str,
        default="dognames.txt",
        help="file containing the list of valid dognames",
    )

    return parser.parse_args()
