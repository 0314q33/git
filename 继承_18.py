class Flower:
    def __init__(self,name):
        self.name=name
    def bloom(self):
        print(f'{self.name}开花')
    def wither(self):
        print(f'{self.name}枯萎')
class Sunflower(Flower):
    def __init__(self,name,color,direction):
        super().__init__(name)#获得继承的属性的意思，要用super
        self.clor=color
        self.direction=direction
    def bloom_towards_sun(self):
        print(f'{self.name}往{self.direction}开')
sunflower=Sunflower(name='向日葵',color='蓝色',direction='东边')
sunflower.bloom_towards_sun()
sunflower.wither()