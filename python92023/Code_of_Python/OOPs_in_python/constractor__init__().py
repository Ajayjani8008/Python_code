class person:
    name = "sahjanandswami"

    def __init__(self, name, occ):
        print("jay swaminarayan")
        self.name = name
        self.occ = occ
    print(name)

    def info(self):
        print(f"{self.name} is {self.occ}")


a = person("ajay", "python programmer")
b = person("meena", "forest gurd")

print(a.name, "is", a.occ)
print(b.name, "is", b.occ, "\n")
# as similer way we can
a.info()
b.info()
