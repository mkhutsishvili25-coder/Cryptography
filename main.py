#TASK 1

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
TASK 2.1: Caesar Cipher - Frequency Analysis Attack
"""


# def caesar_decrypt(ciphertext, shift):
#     """Decrypt text using Caesar cipher"""
#     decrypted = ""
#     for char in ciphertext:
#         if char.isalpha():
#             decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
#         else:
#             decrypted += char
#     return decrypted


# def frequency_analysis(ciphertext):
#     """Perform frequency analysis attack"""
#     # Count letter frequencies
#     freq = {}
#     for char in ciphertext.lower():
#         if char.isalpha():
#             freq[char] = freq.get(char, 0) + 1
#
#     # Sort by frequency
#     sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#
#     print("Letter Frequencies:")
#     for letter, count in sorted_freq:
#         print(f"{letter}: {count}")
#
#     # Try all shifts (brute force)
#     print("\nAll possible decryptions:")
#     results = []
#     for shift in range(26):
#         decrypted = caesar_decrypt(ciphertext, shift)
#         results.append((shift, decrypted))
#         print(f"Shift {shift:2d}: {decrypted}")
#
#     return results



# ciphertext = "mznxpz"
# print(f"Ciphertext: {ciphertext}\n")
# results = frequency_analysis(ciphertext)
#
# print("\nDecrypted text (anagram for Step 2):")
# print(results[21][1])
#


"""
TASK 2.2: Solve the Anagram
Rearrange the decrypted words to form the original passphrase
Hint: The final passphrase is a fundamental concept in cryptography
"""
# def caesar_shift(text, shift):
#     result = []
#     for ch in text:
#         if 'a' <= ch <= 'z':
#             result.append(chr((ord(ch)-97 + shift) % 26 + 97))
#         elif 'A' <= ch <= 'Z':
#             result.append(chr((ord(ch)-65 + shift) % 26 + 65))
#         else:
#             result.append(ch)
#     return ''.join(result)
#
#
# def brute_force_caesar(ciphertext):
#     results = []
#     for s in range(26):
#         results.append((s, caesar_shift(ciphertext, s)))
#     return results
#
#
# cipher2 = "mznxpz"
# print("=== Caesar brute-force for cipher2 (mznxpz) ===")
# candidates = brute_force_caesar(cipher2)
# for s, p in candidates:
#     print(f"shift {s:2d}: {p}")
# print("\n( shift=5 -> 'rescue'. Rearrange 'rescue' -> 'secure' (passphrase).)\n")









# Part 2.3: XOR decryption
import base64
from itertools import cycle


def repeating_key_xor(data_bytes, key_bytes):
    return bytes([b ^ k for b, k in zip(data_bytes, cycle(key_bytes))])

b64_ct = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
ct_bytes = base64.b64decode(b64_ct)
passphrase = "secure"  # recovered from step 2
pt_bytes = repeating_key_xor(ct_bytes, passphrase.encode('ascii'))
print("Base64 decoded ciphertext (hex):", ct_bytes.hex())
print("Using passphrase:", passphrase)
