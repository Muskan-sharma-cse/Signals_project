# 1. Hamari Do Alag-Alag Chabiyaan (Two Keys)
public_key = 3   # Khula Tala (Sabko pata hai - Encryption ke liye)
private_key = 3  # Khufiya Chabi (Sirf mere paas hai - Decryption ke liye)

asli_message = "ATTACK NOW"
print("🗒 Asli Message:", asli_message)

# -------------------------------------------------------------
# 🔒 LOCK KARNA (ENCRYPTION) -> Sirf Public Key se hoga (+3)
# -------------------------------------------------------------
encrypted_code = ""
for letter in asli_message:
    if letter == " ":
        encrypted_code += " "
    else:
        # Public Key lagakar letter ko 3 kadam aage badha diya
        encrypted_code += chr(ord(letter) + public_key)

print("🔒 Encrypted Code (Dushman ko aisa dikhega):", encrypted_code)


# -------------------------------------------------------------
# 🔓 UNLOCK KARNA (DECRYPTION) -> Sirf Private Key se hoga (-3)
# -------------------------------------------------------------
decrypted_message = ""
for letter in encrypted_code:
    if letter == " ":
        decrypted_message += " "
    else:
        # Private Key lagakar 3 kadam peeche lekar aaye
        decrypted_message += chr(ord(letter) - private_key)

print("🔓 Decrypted Message (Wapas Asli Roop):", decrypted_message)


 Output: Asli Message: ATTACK NOW
🔒 Encrypted Code (Dushman ko aisa dikhega): DWWDFN QRZ
🔓 Decrypted Message (Wapas Asli Roop): ATTACK NOW
