import hashlib  # Python ki apni automatic hash machine

# Step 1: Hamara khufiya password jo hume safe rakhna hai
my_password = "MySecret123"

# Step 2: Password ko hash machine (SHA-256) ke andar bhej diya
# .encode() isliye likha kyunki machine ko characters nahi, bytes pasand hain
hash_machine = hashlib.sha256(my_password.encode())

# Step 3: Fingerprint (Ajeeb sa code) baahar nikalna
unique_fingerprint = hash_machine.hexdigest()

print("🗒 Asli Password:", my_password)
print("🔒 Uska Unique Fingerprint (Hash):", unique_fingerprint)

output:
🗒 Asli Password: MySecret123
🔒 Uska Unique Fingerprint (Hash): 82a3d0cb81005d52729a1b1a7d6560ef702111d0bbd60920b72fec016fb14
