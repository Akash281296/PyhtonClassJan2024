# Assignment
# chr(), ord()
print("chr(77) ", chr(77))
print("ord('M')", ord("M"))
# Caesar cipher
# a b c d e f ......
# 0 1 2 3 4 5 .......
# +3
# bad -> edg
# ex: attack is planned to happen on next sunday

# HINT : % operation, chr(), ord(), list comprehension

original_message = "Whispering winds dance beneath the moonlit sky's gentle glow"
shift_value = 3
encrypted_message = ''.join([chr((ord(char) - ord('a') + shift_value) % 26 + ord('a')) if 'a' <= char <= 'z' else 
                              chr((ord(char) - ord('A') + shift_value) % 26 + ord('A')) if 'A' <= char <= 'Z' else char 
                              for char in original_message])

print(f"Original message: {original_message}")
print(f"Encrypted message: {encrypted_message}")