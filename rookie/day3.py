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
    def speak(self,words):
        # 没有绑定在实例身上的变量，是函数的局部变量，只能在函数内部使用
        hh = '呵呵'
        print(hh)
        print(words)

if __name__ == '__main__':
    # 创建实例，实例名自动作为第一个参数传递给__init__方法
    lb = Role('吕布', '方天画戟')  # 创建实例，自动调用__init__.
    print(lb.name)
    print(lb.weapon)
    print(lb.hp)
    print(lb.hp)
    zf = Role('张飞', '丈八蛇茅')
    print(zf.name, zf.weapon, zf.hp, zf.mp)
    lb.show_me()
    zf.show_me()
    lb.speak('人中吕布，马中赤兔')
    zf.speak('我乃燕人张翼德')

