import random

word_list=['welcome','kantara','avatar']
choosen_word=random.choice(word_list)
print(choosen_word)
guess=input("Guess a letter:")
guess_word=guess.casefold()
print(guess_word)
for idx ,char in enumerate(choosen_word):
    if char==guess_word:
        print(f"{guess_word}, found at index {idx}")
    else:
        print("wrong")
word_length=len(choosen_word)
print(word_length)

blank_word=[]
for i in range(word_length):
    blank_word.append("_")
print(blank_word)
