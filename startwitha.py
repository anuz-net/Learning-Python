words = input("Enter words:  ").split()

mileko_words = []

for word in words:
    if len(word) > 3 and word.lower().startswith('a'):
        mileko_words.append(word)

mileko_words.sort()

print(mileko_words)
