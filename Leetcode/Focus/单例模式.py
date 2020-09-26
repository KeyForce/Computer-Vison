class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # 判断是否有instance属性，如果没有被实例化就实例化
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

a = Singleton()
b = Singleton()
print(id(a))
print(id(b))