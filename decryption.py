# Secret message intercepted from the network
secret_message = "DTF"
decrypted_message = ""

# Loop to shift each character back by 1 (The Key)
for letter in secret_message:
    num = ord(letter)
    new_num = num - 1
    new_letter = chr(new_num)
    decrypted_message = decrypted_message + new_letter

# Printing the final unlocked message
print("Unlocked Message:", decrypted_message)
