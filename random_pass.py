import random
import os.path


PASSWORD_FILE = 'saved_passwords.txt'
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%^&*()"

def password_generator():
    
    if not os.path.exists(PASSWORD_FILE) :
        print("File doesn't exist.")
        my_file =open(PASSWORD_FILE, "w+")
        my_file.close()
    while True:
        password_len = int(input("What length would you like your password to be : "))
        password_count = int(input("How many passwords would you like : "))
        for x in range(0,password_count):
            password = ""
            for y in range(0,password_len):
                password_char = random.choice(chars)
                password = password + password_char
            print("Here is your password : ", password)
            my_file = open(PASSWORD_FILE, "a+")
            my_file.write(password +"\n")
            my_file.close()


if __name__ == '__main__':
    print("================================\n")
    print("Welcome to Rahul's first program\n")
    print("================================\n")
    password_generator()
