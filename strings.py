numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total += i

print(total)


numbers = [10, 15, 20, 25, 30, 35]

count = 0

for i in numbers:
    if i > 20:
        count += 1

print(count)


numbers = [12, 45, 7, 89, 23]

largestNumber = numbers[0]

for i in numbers:
    if i > largestNumber:
        largestNumber = i

print(largestNumber)

numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest)


numbers = [10, 15, 20, 25, 30, 35]

total = 0

for i in numbers:
    if i % 2 == 0:
        total += i

print(total)


numbers = [10, 15, 20, 25, 30, 35, 7]

evencount = 0
oddcount = 0

for i in numbers:
    if i % 2 == 0:
        evencount += 1
    else:
        oddcount += 1

print("Even count:", evencount)
print("Odd count:", oddcount)


# for i in numbers:
#     if condition:
#         # inside if
#     else:
#         # inside else
# # outside the loop


text = "agentic ai"

print(text.upper())  # AGENTIC AI
print(text.title())  # Agentic Ai
print(len(text))     # 10
# Remember:
# - .upper() — converts letters to uppercase.
# - .title() — capitalizes the first letter of each word.
# - len() — counts every character, including spaces. "agentic ai" has 10 characters.

word = "developer"

print(word[0])   # d
print(word[4])   # l
print(word[-1])  # r


word = "developer"

print(word[0:3])   # dev 
print(word[0:5])   # devel 
print(word[2:])    # veloper 
print(word[::-1])  # repoleved


text = "  hello python  "

print(text.strip())       # "hello python"
print(text.replace("python", "AI"))  # "  hello AI  "
print(text.lower())       # "  hello python  "


# .strip() removes spaces from the beginning and end.
# .replace(old, new) replaces matching text.
# .lower() converts letters to lowercase.

message = "  Hello AI Developer  "

print(message.strip().lower())
# hello ai developer

print(message.replace("AI", "GenAI"))
#   Hello GenAI Developer


text = "  Hello    GenAI   "

print(text.strip())
# Hello    GenAI

print(text.replace(" ", ""))
# HelloGenAI

print(" ".join(text.split()))
# Hello GenAI

# strings are immutable in Python. That means methods like .replace() return a new string; 
# they don't change the original string itself.

message = "I am learning Python for AI"

print("Python" in message)  # True
print("AI" in message)      # True
print("python" in message)  # False

# Why is the last one False? Because Python is case-sensitive. "Python" and "python" are different strings.
message = "AI is interesting"

words = message.split()

print(words[0])  # AI
print(len(words))  # 3

# split() converts the sentence into ["AI", "is", "interesting"].
# words[0] gets the first word because Python indexing starts at 0.
# len(words) counts the items in the list, which is 3.

words = ["GenAI", "and", "Agents"]

print("-".join(words))  # GenAI-and-Agents
print(" ".join(words))  # GenAI and Agents
sentence = "AI is useful and AI is interesting"

count = 0
a = "AI"

words = sentence.split()

for i in words:
    if i == a:
        count += 1

print(count)

sentence = "ai AI Ai AI"


print(sentence.count("AI"))
print(sentence.lower().count("ai"))
# Remember that .count() is case-sensitive unless you normalize the text first.