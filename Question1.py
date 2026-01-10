# Question 1 
# Create a program that reads the text file "raw_text.txt", encrypts its contents using a 
# simple encryption method, and writes the encrypted text to a new file 
# "encrypted_text.txt". Then create a function to decrypt the content and a function to 
# verify the decryption was successful. 
# Requirements 
# The encryption should take two user inputs (shift1, shift2), and follow these rules: 
# • For lowercase letters: 
# o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 * 
# shift2 positions 
# o If the letter is in the second half (n-z): shift backward by shift1 + shift2 
# positions 
# • For uppercase letters: 
# o If the letter is in the first half (A-M): shift backward by shift1 positions 
# o If the letter is in the second half (N-Z): shift forward by shift2² positions 
# (shift2 squared) 
# • Other characters: 
# o Spaces, tabs, newlines, special characters, and numbers remain 
# unchanged

# Main Functions to Implement
# Encryption function: Reads from "raw_text.txt" and writes encrypted content to
# "encrypted_text.txt".

# Decryption function: Reads from "encrypted_text.txt" and writes the decrypted
# content to "decrypted_text.txt".
# Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints
# whether the decryption was successful or not.
# Program Behavior
# When run, your program should automatically:
# 1. Prompt the user for shift1 and shift2 values
# 2. Encrypt the contents of "raw_text.txt"
# 3. Decrypt the encrypted file
# 4. Verify the decryption matches the original

def encryption(raw_file, shift1, shift2):
    print("Starting encryption...")
    with open(raw_file, 'r') as file:
        content = file.read()
    encrypted_content = ""
    for char in content:
        if char.islower():
            if 'a' <= char <= 'm':
                encrypted_content += chr((ord(char) - ord('a') + shift1 * shift2) % 13 + ord('a'))
            elif 'n' <= char <= 'z':
                encrypted_content += chr((ord(char) - ord('n') - (shift1 + shift2)) % 13 + ord('n'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                encrypted_content += chr((ord(char) - ord('A') - shift1) % 13 + ord('A'))
            elif 'N' <= char <= 'Z':
                encrypted_content += chr((ord(char) - ord('N') + shift2 ** 2) % 13 + ord('N'))
        else:
            encrypted_content += char
    with open("encrypted_text.txt", 'w') as file:
        file.write(encrypted_content)
        print("Encryption completed. Encrypted content written to 'encrypted_text.txt'.")
    return "encrypted_text.txt"


def decryption(encrypted_file, shift1, shift2):
    print("Starting decryption...")
    with open(encrypted_file, 'r') as file:
        content = file.read()
    decrypted_content = ""
    for char in content:
        if char.islower():
            if 'a' <= char <= 'm':
                decrypted_content += chr((ord(char) - ord('a') - shift1 * shift2) % 13 + ord('a'))
            elif 'n' <= char <= 'z':
                decrypted_content += chr((ord(char) - ord('n') + (shift1 + shift2)) % 13 + ord('n'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                decrypted_content += chr((ord(char) - ord('A') + shift1) % 13 + ord('A'))
            elif 'N' <= char <= 'Z':
                decrypted_content += chr((ord(char) - ord('N') - shift2 ** 2) % 13 + ord('N'))
        else:
            decrypted_content += char
    with open("decrypted_text.txt", 'w') as file:
        file.write(decrypted_content)
        print("Decryption completed. Decrypted content written to 'decrypted_text.txt'.")
    return "decrypted_text.txt"

def verification(raw_file, decrypted_file):
    print("Verifying decryption...") 
    with open(raw_file, 'r') as file1, open(decrypted_file, 'r') as file2:
        raw_content = file1.read()
        decrypted_content = file2.read()    
    if raw_content == decrypted_content:
        print("Decryption successful: The decrypted content matches the original.")
    else:
        print("Decryption failed: The decrypted content does not match the original.")

def main(raw_file):
    try:
        shift1 = int(input("Enter shift1 value: "))
        shift2 = int(input("Enter shift2 value: "))

        encrypted_file = encryption(raw_file=raw_file, shift1=shift1, shift2=shift2)
        decrypted_file = decryption(encrypted_file, shift1=shift1, shift2=shift2)
        verification("raw_text.txt", decrypted_file)

    except ValueError as ve:
        print(f"Invalid input: {ve}, please enter integer values for shifts.")
        return
    except Exception as e:
        print(f"Error during encryption: {e}")
        return
    


if __name__ == "__main__":
    raw_file = "raw_text.txt"
    main(raw_file)