class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_color(self):
        print(self.color)
dog=Dog(name='拉布拉多',age=2,color='黄色')
dog.get_name()
dog.get_age()
dog.get_color()