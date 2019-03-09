# 1 - Instructor
Jennifer Staab
  - statistician/computer scientist
  - previously a professor at Florida Polytechnic University

# 2 - Project Description
Goal
  - improve your programming skills with Python
  - focus more on the Python and worry less about the image classifier

Description
  - create registration system for dog show
  - people should register pets with photo and description
  - use already trained classifier to ensure participants are dogs

Tasks
  - determine which classifier algorithm works best for classifying dogs
  - determine how well the best algorithm works
  - time how long each algorithm takes to solve the problem

Notes
  - image classification program here will use a "convolutional neural network" (CNN)
  - CNNs are good at detecting image features (color, texture, edges) and using those to determine what the image is
  - explore 3 different CNN architectures and determine which is best for our application:
    - AlexNet
    - VGG
    - ResNet

# 3 - Project Instructions
Principal Objectives
  - correctly identify images of dogs
  - correctly classify breed of dog (if image is dog)
  - determine which CNN model best achieves #1 and #2
  - Consider time resources and decide if alternative solution would be 'good enough'

To Do
  - edit `check_images.py` to create the currently undefined functions needed to achieve the objectives
  - for additional guidance check files that end in `_hints.py`


# 4 - Workspace How-to
Discusses how to use the built in work space.

Good video to watch if you need to know how to add/delete files or reset the workspace to its original format

# 5 - Timing Code
Test the timing output by adding `sleep()` with various times
  - note: `sleep` in Python uses seconds, not milliseconds like Ruby!

Output showed how long it took (and indicated that a bunch of things hadn't been implemented yet)

Walks through the already implemented timing code
  - of special note is the formatting for the output string

# 6 - Project Workspace - Timing
Implemented in the given workspace

# 7 - Command Line Arguments
Write `get_input_args()` to create and retrieve command line arguments
  - use `argparse` to retrieve 3 command line arguments

Purpose
  - command line arguments give your program more flexibility by allowing external inputs

Argparse
  - Will want folder that contains pet images, CNN model architecture to use, file with valid dog names
  - create arg parser object using `argparse.ArgumentParser()` then use `add_argument_method` to allow users to enter the three inputs

```
# Creates Argument Parser object named parser
parser = argparse.ArgumentParser()

# Argument 1: that's a path to a folder
parser.add_argument('--dir', type = str, default = 'pet_images/',
                    help = 'path to the folder of pet images')
```
`--dir` - variable name of argument
`type` - type of argument
`default` - default value
`help` - Text that willa ppear if user types prgoram name then `-h` or `--help`

# 8 - Project Workspace: Command Line Arguments
Implement the 3 command line arguments and return the parser

# 9 - Mutable Data Types and Functions
mutable data types - can be changed after they're created
  - lists, dictionaries, sets
immutable data types - cannot be changed after they're created
  - integers, tuples, strings, etc

# 10 - Creating Pet Image Labels
Fill in `get_pet_labels()` function to create pet image labels
  - dictionary where key = `filename` and value = `file label`

Expected Outcome
  - code will return dictionary with pet image filename as key and list with pet image label as value for all 40 images in pet_image folder

Manual Check
  - run `check_images.py`
    - The dictionary containing 40 key-value pairs (e.g. dictionary length is 40).
    - The pet image labels the following way:
      -dirLower case letters
      - Single space separating each word
      - Correct representation of the filenames (from the 10 key-value pairs)

To read filenames
  - import listdir from os module

```
# Imports only listdir function from OS module 
from os import listdir  

# Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")
```

Create Pet Image Labels
  - Label: with only lower case letters
  - Blank space separating each word in a label composed of multiple words
  - Whitespace characters stripped from front & end of label

# 11 - Project Workspace: Pet Image Labels
Create a list of pet photo filenames and turn them into a dictionary with filenames as keys and the label (from the file name) in a list as the value
  - Saint_bernard_34322.jpg => `{ 'Saint_bernard_34322.jpg': ['saint bernard'] }`

# 12 - Classifying Images
Create classifier labels with classifier functions using in_arg.arch then compare labels and create dictionary of results

Expected Outcome
Code will return dictionary of lists with pet image filename as key and value will be list as follows:
  - index 0 - pet image label
  - index 1 - classifier label
  - index 2 comparison of labels

Testing the classifier function with `python test_classifier.py`
  collie should be correctly classified as a collie

Function will need to determine matches between pet image labels and labels from classifier function
  use lower() to get them all lower case
  use strip() to get rid of leading/trailing white space
  use `in` to check if your label is in their label

# 13 - Project Workspace: Classifying Images
Wrote the code


# 14 - Classifying Labels as Dogs
Goal is not just to see if the classification is correct, but to see if the classification is actually a dog
  - read in dog names from dognames.txt (turn into a dict, perhaps)
  - compare dog names to classifier and pet image labels in results dict
  - adjust results dict to indicate whether labels indicate image is 'of-a-dog'

# 15 - Project Workspace: Adjusting Results


# 16 - Calculating Results


# 17 - Project Workspace: Calculating Results


# 18 - Printing Results


# 19 - Project Workspace: Printing Results


# 20 - Classify Uploaded Images


# 21 - Project Workspace: Classify Uploaded Images


# 22 - Final Results


# 23 - Project Workspace: Final Results


# 24 - Project: Use a Pre-trained Image Classifier to Identify Dog Breeds

