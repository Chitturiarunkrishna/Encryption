import base64
import binascii
import binhex
import os
import string
import sys
from random import choice
import smtplib
import os
import hashlib


try:
    from colorama import Fore, Style, init
    from Crypto.Cipher import AES
    from Crypto.Random import random
    from cryptography.fernet import Fernet
except ImportError:
    print(
        "ERROR: Missing required libraries.\n"
        "Install dependencies with: pip install -r requirements.txt"
    )
    sys.exit(1)

colorList = [Style.BRIGHT + Fore.RED, Style.BRIGHT , Style.BRIGHT + Fore.YELLOW, Style.BRIGHT + Fore.BLUE, Fore.GREEN ,Fore.MAGENTA, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.WHITE]


init()
print(choice(colorList) +
f"""
{choice(colorList)} 
 ####    #   #
#    #	 #  #
#    #   # # 
# ## #   #  # 
#    #   #    #  
{choice(colorList)}
{Fore.GREEN}Created by: {choice(colorList)}Arun krishna
{choice(colorList)}Theme Pack: {choice(colorList)}incognito
\n"""
)


MENU_OPTIONS = list()


def get(datatype):
    try:
        (message) = {
            "plaintext": ("Enter plaintext message"),
            "encoded": ("Enter encoded message"),
            "encrypted": ("Enter encrypted message"),
            "filename": ("Specify filename"),
            "passwordfilename": ("Specify  passwordfilename"),
            "password": ("Enter encryption password"),
            "Select": ("Choose any one"),
        }[datatype]
    except KeyError:
        message = datatype
    return input(f"\n{message}: {Style.RESET_ALL}").encode()


def show(datatype, output):
    try:
        (message) = {
            "filename": ("Output saved as"),
            "encoded": ("Encoded message"),
            "encrypted": ("Encrypted message"),
            "plaintext": ("Plaintext"),
            "password": ("Encryption password"),
        }[datatype]
    except KeyError:
        message = datatype
    print(f"\n{message}:{Style.RESET_ALL}{output}")


def random_key(length):
    """Generate a random key of the specified length."""
    chars = string.ascii_letters + string.digits
    keypass = "".join(choice(chars) for x in range(length))
    return keypass




def binhex_enc():
    """Encode with BinHex4."""
    temp_filename = f"temp_{random_key(32)}"
    with open(temp_filename, "wb") as outfile:
        outfile.write(get("plaintext"))
    dest_filename = get("filename").decode()
    binhex.binhex(temp_filename, dest_filename)
    os.unlink(temp_filename)
    show("outfile", dest_filename)


MENU_OPTIONS.append(binhex_enc)


def binhex_dec():
    """Decode with BinHex4."""
    temp_filename = f"temp_{random_key(32)}"
    binhex.hexbin(get("filename").decode(), temp_filename)
    with open(temp_filename, "rb") as infile:
        show("plaintext", infile.read().decode())
    os.unlink(temp_filename)


MENU_OPTIONS.append(binhex_dec)


def fernet_enc():
    """Encrypt with Fernet (Symmetric)."""
    plaintext = get("plaintext")
    encryption_key = Fernet.generate_key()
    instance = Fernet(encryption_key)
    key = encryption_key.decode()
    output = instance.encrypt(plaintext).decode()
    # print(key)
    # print(output)
    print("Enter the file name as FERNET.txt")
    filename = get("filename").decode()

    print("Enter the file name as FERNETPWD.txt")
    filename2 = get("filename").decode()

    print("Files are saved")

    with open(filename2, "w+") as outfile:
    	_ = [outfile.write(item) for item in (key)]

    with open(filename, "w+") as outfile:
    	_ = [outfile.write(item) for item in (output)]

    print("Fernet encrypted message and key files are saved")
    os.system('python bot3.py')
MENU_OPTIONS.append(fernet_enc)



def fernet_dec():
    """Decrypt with Fernet (Symmetric)."""
    encrypted_text = get("encrypted")
    password = get("password")
    instance = Fernet(password)
    decrypted_text = instance.decrypt(encrypted_text).decode()
    show("plaintext", decrypted_text)
MENU_OPTIONS.append(fernet_dec)


def aes_enc_auto():
    """Encrypt with AES."""
    keypass = random_key(16)
    data = get("plaintext")
    filename = get("filename").decode()
    cipher = AES.new(keypass.encode(), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(filename, "wb") as outfile:
        _ = [outfile.write(item) for item in (cipher.nonce, tag, ciphertext)]
    
    save_path='Path/Whatsapp'
    kn = "AESKEY"
    passwordfilename = os.path.join(save_path, kn+".txt") 
    with open(passwordfilename, "wt") as outfile:
        _ = [outfile.write(item) for item in (keypass)]
    print("AES encrypted message and key files are saved")
    os.system('python bot.py')
MENU_OPTIONS.append(aes_enc_auto)


def aes_dec_auto():
    """Decrypt with AES."""
    filename = get("filename")
    keypass = get("password")
    with open(filename, "rb") as infile:
        nonce, tag, ciphertext = [infile.read(x) for x in (16, 16, -1)]
    cipher = AES.new(keypass, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag).decode()
    show("plaintext", data)
MENU_OPTIONS.append(aes_dec_auto)


def sha_enc_auto():
	"""Hashing with SHA 512"""
	text = input('Enter string to hash: ')
	hash_obj = hashlib.sha1(text.encode())
	hash2 = hash_obj.hexdigest()
	hashed = hash_obj.hexdigest()
	print("Enter the file name as HASH.txt")
	filename = get("filename").decode()
	with open(filename, "w+") as outfile:
		_ = [outfile.write(item) for item in (hashed)]
	print("File saved as HASH.txt")
	os.system('python bot2.py')
MENU_OPTIONS.append(sha_enc_auto)



# Main Function
def main():
    try:
        while True:
            print(
                "\n"
                + Fore.GREEN + "Choose from the following options, or press Ctrl-C to quit:\n\n"
                + Style.RESET_ALL
            )
            for index, option in enumerate(MENU_OPTIONS, 1):
                print(Style.BRIGHT + f"{index}: {' ' if index < 10 else ''}" f"{option.__doc__}" + Style.RESET_ALL)
            choice = get("Select")
            print()
            try:
                MENU_OPTIONS[int(choice) - 1]()
            except (IndexError,UnboundLocalError):
                print("Unknown option." + Style.RESET_ALL)
            # except ValueError:
            #     print("Invalid option."+ "Enter the number of your selection."+ Style.RESET_ALL)
    
    except (KeyboardInterrupt,UnboundLocalError):
        print("\n{}Program Terminated\n{}Have A Nice Day{}".format(Fore.RED,Style.BRIGHT,Style.RESET_ALL))

        sys.exit(1)


if __name__ == "__main__":
    main()
