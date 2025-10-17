# def caesar_decrypt(ciphertext, shift):
#     decrypted = ""
#     for char in ciphertext:
#         if char.isalpha():
#             # Preserve case
#             start = ord('A') if char.isupper() else ord('a')
#             # Shift within alphabet range
#             decrypted += chr((ord(char) - start - shift) % 26 + start)
#         else:
#             decrypted += char
#     return decrypted
#
#
#
#
#
# text = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
#
# print("Trying all possible shifts:\n")
# for s in range(1, 26):
#     print(f"Shift {s:2}: {caesar_decrypt(text, s)}")
#
# decrypted  = caesar_decrypt(text, 14)
#
#
# print("Decrypted :" ,decrypted)


"""
Step 1: Caesar Cipher - Frequency Analysis Attack
"""


def caesar_decrypt(ciphertext, shift):
    """Decrypt text using Caesar cipher"""
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char
    return decrypted


def frequency_analysis(ciphertext):
    """Perform frequency analysis attack"""
    # Count letter frequencies
    freq = {}
    for char in ciphertext.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("Letter Frequencies:")
    for letter, count in sorted_freq:
        print(f"{letter}: {count}")

    # Try all shifts (brute force)
    print("\nAll possible decryptions:")
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
        print(f"Shift {shift:2d}: {decrypted}")

    return results


# Main
ciphertext = "mznxpz"
print(f"Ciphertext: {ciphertext}\n")
results = frequency_analysis(ciphertext)

print("\nDecrypted text (anagram for Step 2):")
print(results[21][1])