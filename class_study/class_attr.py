"""
类的学习
"""


class CocaCola:  # 定义类就像def定义函数一样简单
    formula = ["caffeine", "sugar", "water", "soda"]  # 类里面赋值的变量就是类的变量，这里有一个专有名称叫：类的属性


coke_for_me = CocaCola()  # 左边一个变量，右边写上类的名称双括号，像是赋值的行为，称为类的实例化，coke_for_me叫：实例
coke_for_you = CocaCola()

print(CocaCola.formula)  # 类属性的引用:类名后面输入.自定联想定义类时定义的属性
print(coke_for_me.formula)  # 类的属性被所有实例共享。所以实例后面.,索引的属性值是一样的
print(coke_for_you.formula)  # 类的属性被所有实例共享。所以实例后面.,索引的属性值是一样的


"""实例的属性"""
coke_for_china = CocaCola()
coke_for_china.local_logo = "可口可乐"  # 创建实例属性
print(coke_for_china.local_logo)  # 打印实例属性引用结果
