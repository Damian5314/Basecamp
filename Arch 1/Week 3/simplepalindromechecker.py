word=input("please enter a string: ")
clean_word = word.replace(" ", "").replace(".", "").replace(",", "").lower()
reversed_word = ""
index = len(clean_word) - 1

while index >= 0: 
    reversed_word += clean_word [index] 
    index -= 1

if reversed_word==clean_word:
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
