
# MODULES ARE THE (.PY) FILES THAT CONTAINS  SET OF FUNCTIONS YOU WANT TO INCLUDE IN YOUR PROGRAM

# DATE TIME MODULE

import datetime as diddy

x =diddy.datetime.now()   # for the current time
print(x)

y = diddy.datetime(1997,10,14)  # for customized time
print(y.strftime("%A"))   # it will tell the particular day of the date

# RANDOM MODULE

import random as r

z = r.randint(1,90)
print(z)

list1 = ["heads" , "tails"]
choice = r.choice(list1)
print(choice)


# MATH MODULES

import math

var1 = max(10,20900,897618)
print(var1)

var2 = min(1272,372973,937127923)
print(var2)

var3 = pow(2,4)      # finding the power (in the parentheses the first value is the base and the next value is the power)
print(var3)

var4 = math.sqrt(49) # used for finding the square root of any number
print(var4)

var5 = abs(-12)   # used to convert the value into absolute posiitve value
print(var5)

var6 = math.ceil(2.4)     # it returns the smallest integer freater than or equal to a given number
print(var6)

var7 = math.floor(2.4)    # opposite of ceil
print(var7)

# TO CREATE A MODULE ALL WE NEED TO DO IS CREATE A .PY FILE IN A SIMILAR PATH TO OUR PYTHON FILE. INSIDE THAT FILE WE CAN ADD REQUIRED FUNCTIONS WE NEED IN OUR PROGRAM TO PERFORM

# TO CALL THE MODULE INSIDE OUR PROGRAM ALL WE NEED TO DO IS USE IMPORT KEYWORD FOLLOWED BY THE NAME OF OUR .PY FILE

# OS MODULE

import os

print(os.getcwd())   # it is used to print the current working directory (cwd)

# in order to change directory we need to write :-
# os.chdir("the name of the file or directory")

# in order to list all the files and folders in a directory :-
# print(os.listdir("pass in the name of the directory"))

# in order to make a new folder in the current directory
# os.mkdir("path name")
# in order to make an entire directory tree (it will create sub dirs)
# os.makedirs("reports/2025/week1" exist_ok = True)

# in order to delete a single directory :-
# os.rmdir("path name")
# in order to remove the whole directory and with sub directories at once:-
# os.removedirs("path name" )  # this will remove multiple dirs at a time

# in order to rename a file or folder :-
# os.rename("the original file name" , "the new name of the file")

# in order to print the stats about the directory or file :-
#print(os.stat("file name"))
# to check the size of the folder :-
# print(os.stat("path name"). st_size)
# to check the last modification time 
# print(os.stat("path name").st_mtime)

# when we will print the modification time and to convert it into human readable form what we need to do is :-

# import datetime module
# assign the modification checking code to any variable (e.g. mod_time)
# then write print(datetime.fromtimestamp(pass the variable name))

# traverse the directory tree anad see all the files and folder :-
#for dirpath,dirname,filename in os.walk(os.getcwd()):
 #                     print('current path : ' , dirpath)
  #                    print("directories :" , dirname)
   #                   print("files : " , filename)
    #                  print()


# in order to get environment variables :-
# os.environ.get()
# to get only one vaariable:-
# os.environ.get("path name")

# in order to combine the directory with the file name :-
# var_name = os.path.join(os.environ.get('path name') , 'file name')

# to get the directory name:-  print(os.path.dirname("path name"))
# to get the file name :- print(os.path.basename("path name"))
# to get the whole name :- print(os.path.split("path name"))
# to check if the directory exists :- print(os.path.exists("path name"))
# to check if its a file :- print(os.path.isfile("path name"))
# to check if its a directory :- print(os.path.isdir("path name"))
# to spilt the extension :- print(os.path.splitext("path name"))
