# Problem Definition

the problem is implementation of a program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:
•	Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;
•	Synchronization should be performed periodically;
•	File creation/copying/removal operations should be logged to a file and to the console output;
•	Folder paths, synchronization interval and log file path should be provided using the command line arguments.

### requirments
First step is importing the required modules. Here, ```os, shutil, logging``` is used to have access to operations on files and collections of files.

Then, the arguments are defined in order to interacting with user by command line. arguments such as: ```source_path, replica_path, log_file, action, and number of interval```.
Class sync consists of three methods called, ```look_into, copy, and remove```. 

### look_into

This method is going tthough every folder and files, then creating sub_folders in the current path. Then based on the action, which is defined, copy method or remove method will be runned. 

### copy

This method will copy every file based on where the ```os.walk(path)``` function is.

### remove

The last method will remove all the directory.

# How to run

By running the command below, the program will launch.
For example:
```
.\main.py -s 'E:/Test/API/New folder/1' -d 'E:/Test/API/New folder/2' -l 'E:/Test/API/New folder/log.txt' -a c
```
Here, there is a log file in the define location.

