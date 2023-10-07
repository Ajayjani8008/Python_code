class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}\n{self.age}\n{self.gender}"


p2 = person("ajay jani", 24, "male")

print(p2)
