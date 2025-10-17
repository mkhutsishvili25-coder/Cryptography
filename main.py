def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            # Preserve case
            start = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet range
            decrypted += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted += char
    return decrypted





text = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

print("Trying all possible shifts:\n")
for s in range(1, 26):
    print(f"Shift {s:2}: {caesar_decrypt(text, s)}")

decrypted  = caesar_decrypt(text, 14)


print("Decrypted :" ,decrypted)