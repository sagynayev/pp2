def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

userWrite = input("Enter a sentence: ")
reversedSentence = reverse_sentence(userWrite)
print(reversedSentence)
