# 1. Asli Message aur hamari secret key
message = "ATTACK"
key = 5  # Yeh hamari secret chabi hai

# -------------------------------------------------------------
# 🔒 LOCK KARNA (ENCRYPTION)
# -------------------------------------------------------------
encrypted_message = ""
for letter in message:
    # ord(letter) se number mila, ^ (XOR) kiya key ke sath, aur wapas letter banaya
    encrypted_message += chr(ord(letter) ^ key)

print("🔒 Encrypted Code (Dushman ko aisa dikhega):", encrypted_message)


# -------------------------------------------------------------
# 🔓 UNLOCK KARNA (DECRYPTION)
# -------------------------------------------------------------
decrypted_message = ""
for letter in encrypted_message:
    # Magic Point: Dobara wahi same XOR (^) chalane se message wapas seedha ho jata hai!
    decrypted_message += chr(ord(letter) ^ key)

print("🔓 Decrypted Message (Wapas Asli Roop):", decrypted_message)



🖥️ Output : 🔒 Encrypted Code (Dushman ko aisa dikhega): DWWDFA
🔓 Decrypted Message (Wapas Asli Roop): ATTACK
