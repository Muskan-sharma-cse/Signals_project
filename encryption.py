mymessage = "CSE"
secret_message = ""

for letter in mymessage:
    num = ord(letter)
    new_num = num + 1
    new_letter = chr(new_num)
    secret_message = secret_message + new_letter

print("Secret Code:", secret_message)
