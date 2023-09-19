word=input("please enter a string: ")
word_without_spaces = word.replace(" ", "")
reversed_word= word_without_spaces[::-1]

if reversed_word==word_without_spaces: print(f"'{word}' is a palindrome")
else: print(f"'{word}' is not a palindrome")