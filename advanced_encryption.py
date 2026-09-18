# The full military sentence to encrypt
mymessage = "ATTACK NOW"
secret_message = ""

# Loop through each letter in the sentence
for letter in mymessage:
    # If the character is a space, keep it as a space
    if letter == " ":
        secret_message = secret_message + " "
    # If it is a normal letter, apply the +1 key
    else:
        num = ord(letter)
        new_num = num + 1
        new_letter = chr(new_num)
        secret_message = secret_message + new_letter

# Printing the final secure output
print("Secret Code:", secret_message)
