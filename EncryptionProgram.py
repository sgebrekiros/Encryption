# Solomon Gebrekiros
import string

# Opens a file and returns the data in file
def read_text(text):
    file = open(text, 'r')
    data = file.read()
    file.close()
    return data

# Takes a key and plaintext
# Returns ciphertext through the use of a monoalphabetic caesar cipher
def encrypt(key, plaintext):
    letters = string.ascii_letters
    ciphertext = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char in letters:
            if 64 < ord(plaintext[i]) < 91:
                ciphertext += chr((ord(char) + key - 65) % 26 + 65)
            elif 96 < ord(plaintext[i]) < 123:
                ciphertext += chr((ord(char) + key - 97) % 26 + 97 )
        else:
            ciphertext += char
    return ciphertext

# Takes a key and ciphertext.
# Returns plaintext through the use of a monalphabetic caesar cipher
def decrypt(key, ciphertext):
    origText = ''
    letters = string.ascii_letters
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char in letters:
            if 64 < ord(ciphertext[i]) < 91:
                origText += chr((ord(char) - key - 65) % 26 + 65)
            elif 96 < ord(ciphertext[i]) < 123:
                origText += chr((ord(char) - key - 97) % 26 + 97)
        else:
            origText += char
    return origText
    
# Makes use of the previous caesar cipher (encrypt function)
# Splits plaintext into blocks to be encrypted
# Creates encrypted file called ciphertext
def complex_encrypt(key, block, plaintext):
    ciphertext = ''
    k = -1
    for i in range(len(plaintext)):
        if i % block == 0 or i == 0:
            k = k + 1
            if (len(plaintext) - i) < block:
                output = encrypt(key[k], plaintext[i:len(plaintext)])
            else:
                output = encrypt(key[k], plaintext[i:i + block])
            ciphertext += output
            if k == len(key) - 1:
                k = -1
    file = open('ciphertext', 'w')
    file.write(ciphertext)
    file.close()
    return ciphertext

# Makes use of the previous caesar cipher (decrypt function)
# Splits plaintext into blocks to be decrypted
# Creates decrypted file called plaintext
def complex_decrypt(key, block, ciphertext):
    plaintext = ''
    k = -1
    for i in range(len(ciphertext)):
        if i % block == 0 or i == 0:
            k = k + 1
            if (len(ciphertext) - i) < block:
                output = decrypt(key[k], ciphertext[i:len(ciphertext)])
            else:
                output = decrypt(key[k], ciphertext[i:i + block])
            plaintext += output
            if k == len(key) - 1:
                k = -1
    file = open('plaintext', 'w')
    file.write(plaintext)
    file.close()
    return plaintext

# Creates a file called ciphertext and writes information to it
def create_encrypt(ciphertext):
    print('The encrypted file is saved as ciphertext and the output is shown below: ')
    print(ciphertext)
    file = open('ciphertext', 'w')
    file.write(ciphertext)
    file.close()

# Creates a file called plaintext and writes information to it
def create_decrypt(plaintext):
    print('The decrypted file is saved as plaintext and the output is shown below: ')
    print(plaintext)
    file = open('plaintext', 'w')
    file.write(plaintext)
    file.close()

# Permutates a plaintext
# Takes 3 blocks of plaintext at a time that contain 3 characters each
# Reverses the order of these blocks before moving on to to the next set
# of plaintext
def permutate(plaintext):
    output = ''
    temp = ''
    temp1 = ''
    temp2 = ''
    temp3 = ''
    n = 0
    for i in range(len(plaintext)):
        if len(plaintext) > 3:
            if i % 3 == 0 or i == 0:
                n += 1
                if (len(plaintext) - i) < 3:
                    temp = plaintext[i:len(plaintext)]
                    if n % 3 == 0:
                        output += temp
                        output += temp2
                        output += temp1
                    elif n % 3 == 2:
                        output += temp
                        output += temp1
                    elif n % 3 == 1:
                        output += temp
                elif n % 3 == 0:
                    temp3 = plaintext[i:i + 3]
                    output += temp3
                    output += temp2
                    output += temp1
                elif n % 3 == 1:
                    temp1 = plaintext[i:i + 3]
                    if (i + 3) == len(plaintext):
                        output += temp1
                elif n % 3 == 2:
                    temp2 = plaintext[i:i + 3]
                    if (i + 3) == len(plaintext):
                        output += temp2
                        output += temp1
        else:
            output = plaintext
    return output

# Reverses the beginning portion of the permutated data
def reverse_permutate_beg(ciphertext):
    output = ''
    temp = ''
    temp1 = ''
    temp2 = ''
    temp3 = ''
    n = 0
    for i in range(len(ciphertext)):
        if len(ciphertext) > 3:
            if len(ciphertext) > 9 and i % 3 == 0 or i == 0:
                n += 1
                if (len(ciphertext) - (len(ciphertext) % 9)) > i:
                    if n % 3 == 0:
                        temp3 = ciphertext[i:i + 3]
                        if (i + 3) == len(ciphertext):
                            output += temp3
                            output += temp2
                            output += temp1
                    elif n % 3 == 1:
                        temp1 = ciphertext[i:i + 3]
                        if (i + 3) == len(ciphertext):
                            output += temp1
                    elif n % 3 == 2:
                        temp2 = ciphertext[i:i + 3]
                        if (i + 3) == len(ciphertext):
                            output += temp2
                            output += temp1
        else:
            output = ciphertext
    return output

# Reverses the end portion of the permutated data
def reverse_permutate_end(ciphertext):
    output = ''
    temp = ''
    temp1 = ''
    temp2 = ''
    for i in range(len(ciphertext)):
        if len(ciphertext) > 3:
            if i % 3 == 0 or i == 0:
                k = len(ciphertext) % 9
                if k == 1:
                    output = ciphertext[len(ciphertext) - k]
                    break
                elif 1 < k < 4:
                    output = ciphertext[len(ciphertext) - k:len(ciphertext)]
                    break
                elif k == 4:
                    temp = ciphertext[len(ciphertext) - k]
                    temp1 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
                elif k == 5:
                    temp = ciphertext[len(ciphertext) - k:len(ciphertext) - 3]
                    temp1 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
                elif k == 6:
                    temp = ciphertext[len(ciphertext) - k:len(ciphertext) - 3]
                    temp1 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
                elif k == 7:
                    temp = ciphertext[len(ciphertext) - k]
                    temp1 = ciphertext[len(ciphertext) - 6:len(ciphertext) - 3]
                    temp2 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
                elif k == 8:
                    temp = ciphertext[len(ciphertext) - k: len(ciphertext) - 6]
                    temp1 = ciphertext[len(ciphertext) - 6:len(ciphertext) - 3]
                    temp2 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
                elif k == 0 and i < 10:
                    temp = ciphertext[len(ciphertext) - 9:len(ciphertext) - 6]
                    temp1 = ciphertext[len(ciphertext) - 6:len(ciphertext) - 3]
                    temp2 = ciphertext[len(ciphertext) - 3:len(ciphertext)]
                    break
    output += temp2
    output += temp1
    output += temp
    return output

# Combines the beginning and end of the reveresed permutated data to get the original text
def reverse_permutate(ciphertext):
    output = ''
    output += reverse_permutate_beg(ciphertext)
    output += reverse_permutate_end(ciphertext)
    return output

def main():
    while True:
        print('1. Encrypt text file\n2. Decrypt text file\n3. Permutate file \n4. End Operation')
        value = input('Enter the number for the operation you want: ')
        # Asks user if they want to encrypt their file
        if value == '1':
            print('1. Use a single Caesar Cipher\n2. Use multiple Caesar Ciphers')
            temp = input('Enter the number for the encryption process you want: ')
            if temp == '1':
                key = input('Input your key: ')
                key = int(key)
                file = input('Enter the file you want to encrypt: ')
                file = read_text(file)
                ciphertext = encrypt(key, file)
                create_encrypt(ciphertext)
            elif temp == '2':
                key_list = []
                key_size = int(input('How many keys will be used? '))
                for i in range(0, key_size):
                    print('Enter key', i + 1 , ': ')
                    key = input('')
                    key_list.append(int(key))
                block = int(input('Enter the block size: '))
                file = input('Enter the file you want to encrypt: ')
                file = read_text(file)
                ciphertext = complex_encrypt(key_list, block, file)
                create_encrypt(ciphertext)
        # Asks user if they want to decrypt their file
        elif value == '2':
            print('1. Use a single Caesar Cipher\n2. Use multiple Caesar Ciphers')
            temp = input('Enter the number for the encryption process you want: ')
            if temp == '1':
                key = input('Input your key: ')
                key = int(key)
                file = input('Enter the file you want to decrypt: ')
                file = read_text(file)
                plaintext = decrypt(key, file)
                create_decrypt(plaintext)
            elif temp == '2':
                key_list = []
                key_size = int(input('How many keys will be used? '))
                for i in range(0, key_size):
                    print('Enter key', i + 1 , ': ')
                    key = input('')
                    key_list.append(int(key))
                block = int(input('Enter the block size: '))
                file = input('Enter the file you want to decrypt: ')
                file = read_text(file)
                plaintext = complex_decrypt(key_list, block, file)
                create_decrypt(plaintext)
        # Asks user if they want to permutate or reverse permutate their file
        elif value == '3':
            temp = input('1. Permutate file\n2. Reverse Permutate file\n')
            if temp == '1':
                file = input('Enter the file you want to permutate: ')
                file = read_text(file)
                ciphertext = permutate(file)
                create_encrypt(ciphertext)
            elif temp == '2':
                file = input('Enter the file you want to reverse permutate: ')
                file = read_text(file)
                plaintext = permutate(file)
                create_decrypt(plaintext)
        # Ends the program
        elif value == '4':
            break
        else:
            print('Enter a value from the options given')
if __name__ == '__main__':
    main()
