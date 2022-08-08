
def encrypt(text,s):
   result = ""
  
   for i in range(len(text)):
      char = text[i]
     
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
     
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result

text = input("Enter the message you would like to encrypt: ").strip()
print()
s = int(input("Enter key to encrypt: "))
print ("Encrypted Cipher: " + encrypt(text,s))

import string

alphabet = string.ascii_lowercase 

import string

alphabet = string.ascii_lowercase 

def decrypt():
    
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:")
    print(decrypted_message)

decrypt()
