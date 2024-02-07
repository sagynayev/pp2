def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]
word = input("Введите слово: ")
if is_palindrome(word):
    print("Это слово является палиндромом")
else:
    print("Это слово не является палиндромом")
