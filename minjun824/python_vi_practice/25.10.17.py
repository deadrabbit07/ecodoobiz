# def greet(name):
#     message = f"Hello, {name}!"
#     return message

# for i in range(1, 6):
#     print(f"Loop interation {i}")

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]


# print(fruits[0])
# print(fruits[-1])

# fruits[1] = "blueberry"
# fruits.append("fig")
# fruits.insert(2, "kiwi")

# del fruits[0]
# fruits.pop()
# fruits.remove("kiwi")

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "Seoul"
# }

# print(person["name"])
# print(person.get("age"))

# person["age"] = 26
# person["job"] = "Developer"

# if person["age"] > 20:
#     print("Adult")
# else:
#     print("Young")

# def check_fruits(fruit_list):
#     for fruit in fruit_list:
#         if "a" in fruit:
#             print(f"{fruit} contains 'a'")

#         else:
#             print(f"{fruit} does not contain 'a'")

# check_fruits(fruits)

# people = [
#     {"name": "Bob", "age": 30},
#     {"name": "Carol", "age": 25},
#     {"name": "Dave", "age": 35},
# ]

# for person in people:
#     for key, value in person.items():
#         print(f"{key}: {value}")
#     print("-----")


# text = "Vi Editor Practice"
# print(text.upper())
# print(text.lower())
# print(text.replace("Vi", "VIM"))

# def min_max(numbers):
#     return min(numbers), max(numbers)

# numbers = [4, 7, 1, 9, 3]
# minimum, maximum, = min_max(numbers)
# print(f"Min: {minimum}, Max: {maximum}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def greet(self):
        print(f"Hello, I am {self.name} and my grade is {self.grade}")

student1 = Student("Alice", 10)
student2 = Student("Bob", 12)

student1.greet()
student2.greet()

scores = [95, 67, 88, 76, 199, 54, 81]

for score in scores:
    if score >= 90:
        print(f"{score}: Excellent")
    elif score >= 70:
        print(f"score: Good")
    else:
        print(f"{score}: Needs Improvement")

filename = "students.txt"

with open(filename, "w") as f:
    f.write("Alice,10\n")
    f.write("Bob,12\n")
    f.write("Carol, 11\n")

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        name, grade = line.strip().split(",")
        print(f"{name} is in grade {grade}")

grades = {"Alice": 10, "Bob": 12, "Carol": 11, "Dave": 9}
for name, grade in grades.items():
    print(f"{name} -> Grade: {grade}")

def filter_passed(scores, passing_score=70):
    return [s for s in scores if s >= passing_score]

passed = filter_passed(scores)
print("Passed scores:", passed)

text = "python programming"
print(text.title())
print(text.replace("python", "Python"))
print(text.split())

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

try:
    x = int("abc")
except ValueError:
    print("Conversion error!")
finally:
    print("Finished error handling")

def get_user_name():
    name = input("Enter your name: ")
    return name.strip()


numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted numbers:", numbers)