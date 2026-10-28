# A list stores multiple values in one variable.

skills = ["Python", "LangGraph", "RAG", "AI Agents"]

print(skills)#['Python', 'LangGraph', 'RAG', 'AI Agents']
print(skills[0])#Python
print(skills[-1])#AI Agents
print(len(skills))#4

skills = ["Python", "React", "Node.js"]

skills.append("LangGraph")  # Add an item
skills.remove("React")      # Remove an item
skills[0] = "Advanced Python"  # Update an item
print(skills)#['Advanced Python', 'Node.js', 'LangGraph']


tools = ["OpenAI", "LangGraph", "Qdrant"]

tools.append("FastAPI")
tools[1] = "CrewAI"

print(tools)#['OpenAI', 'CrewAI', 'Qdrant', 'FastAPI']
print(tools[2])#Qdrant
print(len(tools))#4

data = [
    ["Python",  beginner := 1],
    ["React", 2]
]

print(data[1][0])#React
print(data[0][1])#1


#Tupple
skills_list = ["Python", "React"]
skills_tuple = ("Python", "React")

skills_list[0] = "Java"  # Allowed
# skills_tuple[0] = "Java"  # Error