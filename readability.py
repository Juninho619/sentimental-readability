from cs50 import get_string

# Get text from the user
text = get_string("Text: ")

# Initialize letters, sentences and words
letters = 0
sentences = 0
words = 1

# Use i to calculate the 3 values cf type functions
# Words = roughly spaces + 1
for i in text:
    if i.isalpha():
        letters += 1
    if i.isspace():
        words += 1
    if i in ['.', '!', '?']:
        sentences += 1

# Letters and sentences per words
L = (letters / words) * 100
S = (sentences / words) * 100

# Coleman-Liau index
score = round(0.0588 * L - 0.296 * S - 15.8)

# Print the results
if score < 1:
    print("Before Grade 1")

elif score >= 16:
    print("Grade 16+")

else:
    print("Grade", score)