class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Environment(metaclass=Singleton):
    def __init__(self, name: str = "Production"):
        self.name = name


env1 = Environment()
env2 = Environment("Development")
print("env1 name: ", env1.name)
print("env2 name: ", env2.name)

