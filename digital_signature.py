asli_message = "ATTACK NOW"

# 1. SIGNATURE BANANA (General sahab ne apni khufiya Private Key yaani apna naam piche jod diya)
signed_message = asli_message + "-SignedByGeneral"
print("🗒 General Sahab ne message bheja:", signed_message)


# 2. VERIFICATION (Border Post wale General ki Public Key se check kar rahe hain)
# Unhone check kiya: "Kya iske aakhiri mein -SignedByGeneral likha hai?"
if signed_message.endswith("-SignedByGeneral"):
    print("✅ VERIFICATION SUCCESSFUL: Signature ekdum asli General sahab ka hai!")
else:
    print("❌ ALERT: Signature jhoota hai!")

output:
🗒 General Sahab ne message bheja: ATTACK NOW-SignedByGeneral
✅ VERIFICATION SUCCESSFUL: Signature ekdum asli General sahab ka hai!
