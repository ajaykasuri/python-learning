#A set stores unique values. If a value appears multiple times, Python keeps only one copy.
#The order may vary because sets are unordered.
skills = {"Python", "React", "Python", "AI"}

print(skills)#{'Python', 'React', 'AI'}

#2. Adding and removing values

skills = {"Python", "React", "AI"}

skills.add("LangGraph")       # Add a value
skills.discard("React")       # Remove a value

print(skills)#{'Python', 'AI', 'LangGraph'}
#discard() doesn't raise an error if the value doesn't exist. By contrast,
#remove() raises a KeyError if the value is missing.

#3. Set operations
#These are useful when comparing data, such as finding common skills between developers.
backend = {"Python", "Node.js", "SQL"}
ai = {"Python", "LangGraph", "SQL"}

# Union (|) — all unique values from both sets.
# Intersection (&) — values common to both sets.
# Difference (-) — values in the first set but not the second.

a = {1, 2, 3, 3, 4}
b = {3, 4, 5}

print(a | b)#{1, 2, 3, 4, 5}
print(a & b)#{3, 4}
print(a - b)#{1, 2}