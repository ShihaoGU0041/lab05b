class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def __str__(self):
        """返回人类可读的字符串表示。"""
        return f"Person(name='{self.name}', age={self.age})"

alice = Person("Alice", 25)
print(alice)        # Person(name='Alice', age=25)
print(str(alice))   # Person(name='Alice', age=25)





