import random
import math

# Forward declare some variables
noWords = int(input("How many words? "))
password = ""
words = []

# Read 4 random words from the words dictionary
with open("/usr/share/dict/words") as file:
    text=file.read()
    words = text.split("\n")
    for i in range(noWords):
        password += random.choice(words) + " "
# Calculate entropy of password
entropy = math.log2(len(words)) * len(password.split(" "))

# The character space for a completely random password (without special chars) is 26+26+10
randCharSpace = 62

# log2(62^n) should be greater than entropy, where n is the number of characters needed, 
# with some algebra we get the following equation
n = math.ceil(entropy / math.log2(randCharSpace))

# Print it all out
print("Password: " + password)
print("Entropy : " + str(round(entropy, 2)) + " bits.")
print("You would need " + str(n) + " characters in [A-Za-z0-9] to get the same entropy")

