#syntax: {key: value for item in collection}

#dictionary comprehension
numbers = [2, 3, 4, 5]
cubes = {number: number**3 for number in numbers}
print(cubes)

#Lists 
numbers = [10, 15, 20, 25, 30]

greater = [number for number in numbers if number > 20]

print(greater)