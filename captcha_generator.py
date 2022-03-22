#--------------------------------------------------------------------------------------------------------------------
#                                               Import libraries
#--------------------------------------------------------------------------------------------------------------------
from captcha.image import ImageCaptcha
import random
import sys
import os
#--------------------------------------------------------------------------------------------------------------------
#                               Checking for arguments in terminal excecution
#--------------------------------------------------------------------------------------------------------------------
try:
    DataSet_size = int(sys.argv[1])
except:
    DataSet_size = 1000

try:
    c_size_1 = int(sys.argv[2])
    c_size_2 = c_size_1
except:
    c_size_1 = 5                   #   >>>>>>   # c_size_1 -> minimum of characters in captcha
    c_size_2 = 5                                # c_size_2 -> maximum of characters in captcha
#--------------------------------------------------------------------------------------------------------------------
#                                   Setting DataSet folder directory
#--------------------------------------------------------------------------------------------------------------------

DataSet_path = "./DataSet/"         # file_path -> Sets the folder path where the captchas are going to be saved
c_width = 280
c_height = 90

if os.path.exists(DataSet_path):    # checks that the folder exists
    os.rmdir(DataSet_path)
os.makedirs(DataSet_path)
#--------------------------------------------------------------------------------------------------------------------
#                                            Main definition
#--------------------------------------------------------------------------------------------------------------------
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nGenerating",DataSet_size,"Captchas of",c_size_1,"characters.\n")

    random.seed(a=None, version=2)

    # Create an image instance of the given size
    image = ImageCaptcha(c_width, c_height)
    percentage = 0
    # Image captcha text
    for i in range(DataSet_size):
        if i%(DataSet_size*0.1) == 0:               #print progress, every 10%
            percentage += 10
            print("\r \t\t", percentage,"%","\tCompleted", sep='', end='')
            
        captcha_text = ''

        n_int = random.randint(c_size_1,c_size_2)   # n_init -> set how many characters are in captcha, between c_size_1 and c_size_2
        for i in range(n_int):                                    
            r_type = random.randint(1,3)            # r_type -> The are 3 types of characters, Numbers, Uppercase and Lowercase
            if r_type == 1:
                num = random.randint(48, 57)        # num -> Get random from 48 to 57, converts to ascii with chr()
                captcha_text += chr(num)
            elif r_type == 2:                          
                Upper = random.randint(65, 90)      # Upper -> Get random from 65 to 90, converts to ascii with chr()
                captcha_text += chr(Upper)
            else:
                Lower = random.randint(97, 122)     # Lower -> Get random from 97 to 122, converts to ascii with chr()
                captcha_text += chr(Lower)

        #print("random:",captcha_text)              # <------------------ PRINT CAPTCHA ------------------------------
        
        # generate the image of the given text
        data = image.generate(captcha_text) 
        
        # write the image on the given file and save it
        file_name = DataSet_path + captcha_text + ".png"
        image.write(captcha_text, file_name)
    
    print("\n\n")

#--------------------------------------------------------------------------------------------------------------------
#                                          Running main program
#--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # do nothing here
        print("\n\nCaptcha generator stopped by user.\n\n")
        pass