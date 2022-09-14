# DataSorting

This project consists of some scripts for handling various types of files, with which you will practice your Python and NumPy skills.

## Step 1

Start by creating, in a notebook, a Python script that will iterate alphabetically over the files in the files folder and, depending on the type (audio, document, image), move them to the appropriate subfolder (below is an example). If the subfolder does not exist, your script will have to create it automatically.

During the loop, the script should print the information of the files: name, type and size in bytes.

In addition to printing the information as you move them, keep track of the files by creating a *recap.csv* document with the same information. Find an example in this folder.

## Step 2

Place the script you created in a small executable (call it *addfile.py* and place it in this folder, next to the notebook) equipped with a *command-line interface* (CLI).

The purpose of the executable is to move a *single* file (located in the files folder) to the appropriate subfolder, updating the recap.

The executable's interface has as its only (mandatory) argument the name of the file to be moved (including format, e.g., 'trump.jpeg'). In case the file passed as an argument does not exist, the interface must notify the user.

## Step 3

A grayscale image has only one color level, an RGB has 3, an RGBA 4 (the last one is called an *alpha* channel).

The *Image* module of the *PIL* library allows you to load an image, which can be transformed into a NumPy array through the *np.array* function. From that array, you can tell whether the loaded image is grayscale, RGB, or RGBA.

Add to the Step 1 notebook a script that iterates over the *images* subdirectory and builds a summary table.
