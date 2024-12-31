class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # __init__叫构造器方法，用于绑定属性到实例上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp

    def show_me(self):
        # 绑定在实例身上的属性，在类中任意地方都可用
        print(f'我是{self.name},擅用{self.weapon}')

    def speak(self, words):
        # 没有绑定在实例身上的变量，是函数的局部变量，只能在函数内部使用
        hh = '呵呵'
        print(hh)
        print(words)


class Warrior(Role):  # 括号中是Warrior的父类,也叫基类
    '战士子类'
    def attack(self,target):
        print(f'与{target}近身肉搏')


class Mage(Role):
    '法师子类'
    def attack(self,target):
        print(f'远程攻击{target}')

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    zgl = Mage('诸葛亮', '羽扇')
    lb.show_me()  # 子类中没有show_me 方法，继承了父类的方法
    zgl.show_me()
    lb.attack('张飞')
    zgl.attack('刘备')