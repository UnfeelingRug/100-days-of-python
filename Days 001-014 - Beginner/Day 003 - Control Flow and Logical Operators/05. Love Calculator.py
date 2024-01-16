# This calculator will determine your Compatibility Score based on a completely arbitrary set of rules that might as well be random.random().
print("The Love Calculator is calculating your score...")
name1 = input('What is your name? ')
name2 = input('What is their name? ')

# Combining the names into one string for easier checking, and initializing the counters.
names = name1 + name2
trueCounter = 0
loveCounter = 0

# Add to the counters for every time the letters of "TRUE" and "LOVE" appear in both names.
for letter in names.lower():
    if letter in "true":
        trueCounter += 1
    if letter in "love":
        loveCounter += 1

# Combine the counters into one two-digit number that is the Compatibility Score.
compatibility = int(str(trueCounter) + str(loveCounter))

# Report back on their Compatibility Score, based on the number.
if compatibility < 10 or compatibility > 90:
    print(f'Your score is {compatibility}, you go together like coke and mentos.')
elif compatibility >= 40 and compatibility <= 50:
    print(f'Your score is {compatibility}, you are alright together.')
else:
    print(f'Your score is {compatibility}.')