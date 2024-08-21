class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Tạo đối tượng
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy is barking!