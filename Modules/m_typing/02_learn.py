from typing import Callable, List, Dict


def greeting(names: list):
    return names[0].split()


ames: List[str] = ["yangjing", "alice"]
age: Callable[..., None] = greeting


if __name__ == "__main__":
    # 字典注释。key为str,value为可调用对象(无参数变为None)
    switcher: Dict[str, Callable[..., None]] = {"gecc": greeting, "abb": greeting}
    print(switcher["gecc"]())
