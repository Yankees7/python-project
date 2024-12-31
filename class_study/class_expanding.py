"""对类的扩展理解"""


obj1 = 1
obj2 = "string"
obj3 = []
obj4 = {}
print(type(obj1), type(obj2), type(obj3), type(obj4))

# python中一切皆对象，任何种类的对象都是类的实例，上面的这些类型被称为内建类型，他们并不需要像我们上面一样实例化



from bs4 import BeautifulSoup
soup = BeautifulSoup
print(type(soup))


 