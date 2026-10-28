#A dictionary stores data as key-value pairs.
skills = {
    "Python": "Beginner",
    "React": "Intermediate",
    "Node.js": "Advanced"
}

print(skills["Python"])  # Beginner
print(skills.get("React"))  # Intermediate
print(skills.get("JavaScript", "Not found"))  # Not found

skills["Python"] = "Advanced"  # Update a value
skills["JavaScript"] = "Beginner"  # Add a new key-value pair

print(skills)  # {'Python': 'Advanced', 'React': 'Intermediate', 'Node.js': 'Advanced', 'JavaScript': 'Beginner'}


ai_tool = {
    "name": "LangGraph",
    "type": "Framework",
    "language": "Python"
}

print(ai_tool.keys())#dict_keys(['name', 'type', 'language'])
print(ai_tool.values())#dict_values(['LangGraph', 'Framework', 'Python'])
print(ai_tool.items())#dict_items([('name', 'LangGraph'), ('type', 'Framework'), ('language', 'Python')])
print(ai_tool.get("name"))#LangGraph


profile = {
    "name": "Ajay",
    "skill": "Python"
}

print(profile.get("city", "Not provided"))#Not provided
print("name" in profile)#True
print("city" in profile)#False
#Important: The in operator checks whether a key exists in a dictionary. It returns True or False, not None.


profile = {
    "name": "Ajay",
    "skill": "Python",
    "goal": "AI Developer"
}

for key, value in profile.items():
    print(key, value)

# name Ajay
# skill Python
# goal AI Developer


scores = {
    "Math": 90,
    "Python": 85,
    "English": 75
}

for subject, score in scores.items():
    if score >= 85:
        print(subject)

# Math
# Python


scores = {
    "Math": 90,
    "Python": 85,
    "English": 75
}

for subject in scores:
    print(subject)

# Math
# Python
# English

#.items() gives you both the key and its value.

for score in scores.values():
    print(score)

# 90
# 85
# 75

# Remember these three rules:
# - for key in scores: → keys
# - for value in scores.values(): → values
# - for key, value in scores.items(): → both



# Create a dictionary called user with these details:
# - name: "Ajay"
# - age: 26
# - skill: "Python"
# Then perform these tasks:
# 1. Print the user's name.
# 2. Change the skill to "AI Developer".
# 3. Add a new key called "city" with the value "Hyderabad".
# 4. Remove the "age" key.
# 5. Print the final dictionary.
# Starter code:

user = {
    "name": "Ajay",
    "age": 26,
    "skill": "Python"
}

print(user["name"])

user["skill"] = "AI Developer"
user["city"] = "Hyderabad"

user.pop("age")

print(user)