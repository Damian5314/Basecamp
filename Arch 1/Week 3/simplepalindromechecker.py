word=input("please enter a string: ")
reversed_word= word[::-1]

if reversed_word==word: print(f"'{word}' is a palindrome")
else: print(f"'{word}' is not a palindrome")