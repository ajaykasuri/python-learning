# JSON in Python:
# JSON is a format used to exchange data between applications, especially between a frontend and backend.

# 2. Convert Python data to JSON

import json

user = {
    "name": "Ajay",
    "age": 26
}

result = json.dumps(user, indent=4)
print(result)
# json.dumps() converts a Python object into a JSON string

# 3. Convert JSON into Python data

import json

data = '{"name": "Ajay", "age": 26}'

user = json.loads(data)

print(user["name"])
print(user["age"])
# json.loads() converts a JSON string into a Python dictionary.

# 4. Save JSON to a file
# You don't need to create user.json manually. Python creates it when you open it in write mode.

import json

user = {
    "name": "Ajay",
    "skills": ["React", "Python"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

# To read the file later:
with open("user.json", "r") as file:
    data = json.load(file)

print(data["skills"])


# 5. Remember these four functions
# Function	Purpose
# json.dumps()	Python data → JSON string
# json.loads()	JSON string → Python data
# json.dump()	Python data → JSON file
# json.load()	JSON file → Python data



# indent=4 tells Python to format the JSON with 4 spaces for each indentation level, making it easier to read.

# Without indent=4:
# import jsonuser = {"name": "Ajay", "skills": ["React", "Python"]}print(json.dumps(user))



# Output:
{"name": "Ajay", "skills": ["React", "Python"]}


# With indent=4:
print(json.dumps(user, indent=4))



Output:
{
    "name": "Ajay",
    "skills": [
        "React",
        "Python"
    ]
}


# Notice that each nested level moves 4 spaces to the right.

# You can also use indent=2 if you prefer two spaces.

# Remember: indent=4 only changes how the JSON is formatted. It doesn't change the actual data.