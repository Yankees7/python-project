class Book:
    def __init__(self, title, author):
        '构造器方法，实例化时自动调用'
        self.title = title
        self.author = author
    def __str__(self):
        return f'《{self.title}》'
    def __call__(self):
        '实例像函数一样调用时，执行      此方法中的代码'
        print(f'《{self.title}》是{self.author}编写的')

if __name__ == '__main__':
    linux = Book('Linux运维之道', '丁明一') # 调用__init__
    print(linux)
    linux()
