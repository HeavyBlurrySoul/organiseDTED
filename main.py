import os

# create the output folders if they don't already exist
if not os.path.exists("outputLevel1/"):
    os.makedirs("outputLevel1/")

if not os.path.exists("outputLevel2/"):
    os.makedirs("outputLevel2/")

# loop through all files in the current directory
for file in os.listdir():
    if file.endswith(".dt2"): #level2
        print(".")
        # extract the direction (e/w) and number (xxx) from the filename
        direction = file.split("_")[1][0]
        number = file.split("_")[1][1:4]
        print(file)
        # create a folder named (e/w)xxx inside the output folder if it doesn't already exist
        folder_name = "outputLevel2/" + direction + number
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # rename the file to nxx
        new_name = "" + file.split("_")[0]

        # move the file to the correct folder
        os.rename(file, folder_name + "/" + new_name + ".dt2")
    elif file.endswith(".dt1"): #level1
        print(".")
        # extract the direction (e/w) and number (xxx) from the filename
        direction = file.split("_")[1][0]
        number = file.split("_")[1][1:4]
        print(file)
        # create a folder named (e/w)xxx inside the output folder if it doesn't already exist
        folder_name = "outputLevel1/" + direction + number
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # rename the file to nxx
        new_name = "" + file.split("_")[0]

        # move the file to the correct folder
        os.rename(file, folder_name + "/" + new_name + ".dt1")
       