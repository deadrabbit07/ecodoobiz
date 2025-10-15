def practice_function():
    numbers = [1, 2, 3, 4, 5] #yy 복사하기 p 커서 아래에 붙여넣기
    numbers = [1, 2, 3, 4, 5] #nyy n줄복사하기 P 커서 앞에 붙여넣기
    numbers = [1, 2, 3, 4, 5]
    result = [] #u 실행 취소 Ctrl + r 다시 실행
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n * 3)
        else:
            result.append(n + 1)
    return result

class PraticeClass:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.items.append(item)
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item}")

def loop_example():
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
        print("Inner loop finished")

def condition_example(x):
    if x > 0:
        print("Positive")
    elif x == 9:
        print("Zero")
    else:
        print("Negative")

def string_list_example():
    fruits = ["apple", "banana", "cherry"]
    vegetables = ["carrot", "broccoli", "spinach"]
    combined = fruits + vegetables
    for item in combined:
        print(item.upper())
        print(item.lower())

def dict_example():
    info = {"name": "Alice", "age": 30, "city": "Seoul"}
    for key, value in info.items():
        print(f"{key}: {value}")

def calc_example():
    a = 10
    b = 20
    c = a + b
    d = a * b
    e = b - a
    f = b / a
    g = a ** 2 
    h = b % 3
    return c, d, e, f, g, h

def while_example():
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1

def nested_loop():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z)

def boolean_example(flag):
    if flag and not flag:
        print("Impossible")
    elif flag or not flag:
        print("Always True")

def main():
    print(practice_function())
    obj = PractiveClass("Test")
    obj.add_item("Item2")
    obj.show_items()
    loop_example()
    condition_example(5)
    string_list_example()
    dict_example()
    calc_example()
    while_example()
    nested_loop()
    boolean_example(True)

if __name__ == "__main__":
    main()
    
    
