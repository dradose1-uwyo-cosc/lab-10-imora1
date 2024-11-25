# Isabell Mora
# UWYO COSC 1010
# 11-24--24
# Lab 10
# Lab Section:11
# Sources, people worked with, help given to: Ethan Romero
# your
# comments
# here

#import modules you will need 

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()
def get_password():
    try:
        with open('hash', 'r') as hash: 
            hash_storage = hash.read().strip()
    except FileNotFoundError:
        print("File 'hash' was not found.")
        return 
    except OSError:
        print("Error opening the the 'hash' file.")
        return
    
    try:
        with open('rockyou.txt','r') as rockyou_file:
            for password in rockyou_file:
                password = password.strip()
                hash_password = get_hash(password)
                if hash_password == hash_storage:
                    print(f"Password: {password}")
                    return
    except FileNotFoundError:
        print("'rockyou.txt' was not found")
    except OSError:
        print("Error opeing the 'rockyou.txt' file.")
get_password()
