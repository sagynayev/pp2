def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

userWrite = input()
reversedSentence = reverse_sentence(userWrite)
print(reversedSentence)
