# Write to a file
# with open("notes.txt", "w") as file:
#     file.write("Learning Python for AI")

# # Read from a file
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# "w" — write; creates a file or overwrites its existing content.
# "r" — read an existing file.
# "a" — append content to the end of a file.


# Write to a file
with open("user.txt", "w") as file:
    file.write("Ajay is learning Python")

# Read from a file
with open("user.txt", "r") as file:
    content = file.read()
    print(content)

# Append to a file
with open("user.txt", "a") as file:
    file.write(" and Gen AI")

# Read the updated file
with open("user.txt", "r") as file:
    content = file.read()
    print(content)