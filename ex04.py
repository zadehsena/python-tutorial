# Exercise description

# The next step on our journey to implementing Wordle is to produce a program 
# that gives the player six guesses at your program’s secret word, just like 
# the real game. Examples of how the function should perform can be seen below.

# ----------------------------------------------------------------------------

# Exmaple inputs and outputs

# === Turn 1/6 ===
# Enter a 5 character word: dukes
# 🟨⬜⬜🟩🟩
# === Turn 2/6 ===
# Enter a 5 character word: gonna
# ⬜🟩⬜⬜⬜
# === Turn 3/6 ===
# Enter a 5 character word: lose
# That wasn't 5 chars! Try again: loser
# ⬜🟩🟨🟩⬜
# === Turn 4/6 ===
# Enter a 5 character word: tounc
# ⬜🟩⬜⬜🟨
# === Turn 5/6 ===
# Enter a 5 character word: saturday
# That wasn't 5 chars! Try again: sat 
# That wasn't 5 chars! Try again: stday
# 🟨⬜🟩⬜⬜
# === Turn 6/6 ===
# Enter a 5 character word: biscuits
# That wasn't 5 chars! Try again: bscts
# ⬜🟨🟨⬜🟩
# X/6 - Sorry, try again tomorrow!


# === Turn 1/6 ===
# Enter a 5 character word: ideas
# ⬜🟨🟨⬜🟩
# === Turn 2/6 ===
# Enter a 5 character word: doges
# 🟨🟩⬜🟩🟩
# === Turn 3/6 ===
# Enter a 5 character word: codes
# 🟩🟩🟩🟩🟩
# You won in 3/6 turns!

# ----------------------------------------------------------------------------

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# Given two strings, the first of any length, the second a single character, 
# it will return True if the single character of the second string is found 
# at any index of the first string, and return False otherwise

# Example: contains_char("abc", "b") -> True

def contains_char(word, char):
    pass

# Given two strings of equal length, the first a guess and the second a secret, 
# it will return a string of emoji green/yellow/white squares.

# Example: emojified("ideas", "codes") -> ⬜🟨🟨⬜🟩

def emojified(guess, secret):
    pass

# Given an integer “expected length” of a guess as a parameter, it will prompt 
# the user for a guess and continue prompting them until they provide a guess 
# of the expected length. This function then returns the users guess.

# Example: input_guess(5)
# Enter a 5 character word: what
# That wasn't 5 chars! Try again: trains
# That wasn't 5 chars! Try again: logan
# -> logan

def input_guess(length):
    pass

# Now it’s time to pull together your functions, which are building blocks, into 
# the main wordle function. Use the functions that you wrote above.

def wordle(secret):
    pass
