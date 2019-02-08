
import os
import shutil


# Create the secret folder #
def CreateFolder():

    # Ask for new password
    pswrd = str(input("Enter a new password: "))

    os.mkdir(path + file)

    CreateInfo(pswrd)

# Create Info file for password #
def CreateInfo(pswrd):
    with open(path + file + "\info.txt", 'w') as f:
        f.write(pswrd)


# Hide the folder #
def HideFolder():
    shutil.move(path + file, secret_path)


# Show the folder #
def ShowFolder():
    shutil.move(secret_path + file, path)


# Ask user password #
def AskPass(desiredPath):

    if not (os.path.exists(desiredPath + file + "\info.txt")):
        # Ask for new password
        pswrd = str(input("Enter a new password: "))
        CreateInfo(pswrd)

    # Get password
    pswrd = ""
    with open(desiredPath + file + "\info.txt", 'r') as f:
        pswrd = f.readline()

    # Verify password
    passCheck = str(input("Enter password: "))
    if (passCheck == pswrd):
        print("YES")
        return True
    else :
        print("NO")
        return False


# Main #
file = "Private"
path = os.getcwd() + "\\"
secret_path = "C:\Windows\Temp\\"

if (os.path.exists(secret_path + file)):
    if (AskPass(secret_path)):
        ShowFolder()
elif (os.path.exists(path + file)):
    HideFolder()
else:
    CreateFolder()
