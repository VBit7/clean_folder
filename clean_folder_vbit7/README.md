# Package Name: `clean_folder`

### Description:

`clean_folder` is a Python package designed to automate the sorting and cleaning of the "Unsorted" folder on your desktop. This package provides a command-line script that makes it easy and fast to sort files by their extensions, renaming them and performing other actions to facilitate the organization of your desktop.

### Key Features and Capabilities:

Sorting files by types: `images`, `videos`, `documents`, `music`, `archives`, and files with unknown extensions.
Renaming files to eliminate problematic characters and transliterating Cyrillic characters to Latin.
Recursive traversal of folders to sort files in all subfolders.
Support for various file extensions that can be added and edited as needed.
Handling archives, including unpacking and moving them to a separate folder.
Removing empty folders after sorting.
Ignoring folders that already contain subfolders like archives, video, audio, documents, and images.
Requirements:

Install the package in the system using the pip install -e . command (or python setup.py install if administrator permissions are required).
After installation, the `clean_folder` package becomes available in the system.
Once the package is installed, the script can be called from the command line anywhere using the clean-folder command.

### Usage Example:

```$ clean-folder /user/Desktop/Unsorted```

This command runs the script to sort and clean the "`Unsorted`" folder at the specified path.

`clean_folder` simplifies and speeds up the organization of your desktop, reducing the need to manually sort files and folders.