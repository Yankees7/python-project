class Role:
    def __init__(self, name, weapon, hp=500, mp=300):
        # __init__叫构造器方法，用于绑定属性到实例上
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.mp = mp


class Weapon:
    def __init__(self, wname, strength, type):
        self.wname = wname
        self.strength = strength
        self.type = type


if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理攻击')
    print(ji.wname, ji.strength, ji.type)
    lb = Role('吕布', ji)
    print(lb.weapon.wname, lb.weapon.strength, lb.weapon.type)
