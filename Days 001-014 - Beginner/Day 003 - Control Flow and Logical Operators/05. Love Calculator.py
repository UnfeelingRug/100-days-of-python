print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

names = name1 + name2
trueCounter = 0
loveCounter = 0

for letter in names.lower():
    if letter in "true":
        trueCounter += 1
    if letter in "love":
        loveCounter += 1

compatibility = int(str(trueCounter) + str(loveCounter))

if compatibility < 10 or compatibility > 90:
    print(f'Your score is {compatibility}, you go together like coke and mentos.')
elif compatibility >= 40 and compatibility <= 50:
    print(f'Your score is {compatibility}, you are alright together.')
else:
    print(f'Your score is {compatibility}.')