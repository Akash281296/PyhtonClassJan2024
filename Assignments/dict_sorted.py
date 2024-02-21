import string

# Define the large sentence
large_sentence = """
The shimmering moon cast its ethereal glow upon the tranquil lake, where the gentle ripples danced in harmony with the 
whispers of the night. Amidst the silvery mist, a lone figure stood, bathed in the soft luminescence, contemplating the
mysteries of the universe. The ancient trees, adorned with emerald leaves, swayed in the breeze, their branches reaching 
towards the star-studded sky. A symphony of crickets filled the air, blending with the distant calls of nocturnal creatures.
In this enchanted realm, time seemed to stand still, as if caught in a reverie of eternal peace and serenity.
Each moment held a promise of magic, as the world embraced the quietude of the nocturnal hour.
"""

# Character frequency analysis
# a) Case sensitive
char_freq_case_sensitive = {}
for char in large_sentence:
    if char in char_freq_case_sensitive:
        char_freq_case_sensitive[char] += 1
    else:
        char_freq_case_sensitive[char] = 1
print("Character Frequency Analysis (Case Sensitive):")
print(char_freq_case_sensitive)

# b) Case insensitive
char_freq_case_insensitive = {}
for char in large_sentence.lower():
    if char in char_freq_case_insensitive:
        char_freq_case_insensitive[char] += 1
    else:
        char_freq_case_insensitive[char] = 1
print("\nCharacter Frequency Analysis (Case Insensitive):")
print(char_freq_case_insensitive)

# Word frequency analysis
# a) Case sensitive
words = large_sentence.split()
word_freq_case_sensitive = {}
for word in words:
    if word in word_freq_case_sensitive:
        word_freq_case_sensitive[word] += 1
    else:
        word_freq_case_sensitive[word] = 1
print("\nWord Frequency Analysis (Case Sensitive):")
print(word_freq_case_sensitive)

# b) Case insensitive
word_freq_case_insensitive = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_freq_case_insensitive:
        word_freq_case_insensitive[word_lower] += 1
    else:
        word_freq_case_insensitive[word_lower] = 1
print("\nWord Frequency Analysis (Case Insensitive):")
print(word_freq_case_insensitive)

# Cleansed words frequency analysis
cleansed_words = [''.join(char for char in word if char.isalnum()) for word in words]
# a) Case sensitive
cleansed_word_freq_case_sensitive = {}
for word in cleansed_words:
    if word:
        if word in cleansed_word_freq_case_sensitive:
            cleansed_word_freq_case_sensitive[word] += 1
        else:
            cleansed_word_freq_case_sensitive[word] = 1
print("\nCleansed Word Frequency Analysis (Case Sensitive):")
print(cleansed_word_freq_case_sensitive)

# b) Case insensitive
cleansed_word_freq_case_insensitive = {}
for word in cleansed_words:
    word_lower = word.lower()
    if word_lower:
        if word_lower in cleansed_word_freq_case_insensitive:
            cleansed_word_freq_case_insensitive[word_lower] += 1
        else:
            cleansed_word_freq_case_insensitive[word_lower] = 1
print("\nCleansed Word Frequency Analysis (Case Insensitive):")
print(cleansed_word_freq_case_insensitive)