"""类的继承"""


# from class_method import CocaCola
class CocaCola:
    calories = 40  # 卡路里
    sodium = 45  # 钠
    total_carb = 39  # 总共碳水化合物
    caffeine = 34  # 咖啡因
    ingredients = [
        "High Fructose Corn Syrp",
        "Carbonated Water",
        "Phosphoric Acid",
        "Natual Flavors",
        "Caramel Color",
        "Caffeine",
    ]  # 成分配料

    def __init__(self, logo_name) -> None:
        self.local_logo = logo_name

    def drink(self):
        print("You got {} cal energy!".format(self.calories))


class CaffeineFree(CocaCola):  # 类的继承：新类括号里面放入父类，类的变量和方法完全被子类继承
    caffeine = 0
    ingredients = [
        "High Fructose Corn Syrp",
        "Carbonated Water",
        "Phosphoric Acid",
        "Natual Flavors",
        "Caramel Color",
    ]


# 类的变量和方法完全被子类继承
coke_a = CaffeineFree("Cocacola-Free")
coke_a.drink()
print(coke_a.local_logo)
