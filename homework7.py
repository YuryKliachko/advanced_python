from collections import defaultdict


class MyMetaClass(type):
    def __new__(cls, cls_name, bases, dct):
        properties = defaultdict(dict)
        for name, value in dct.items():
            if name.startswith('get_'):
                properties[name[name.rfind('_') + 1]]['fget'] = dct[name]
            elif name.startswith('set_'):
                properties[name[name.rfind('_') + 1]]['fset'] = dct[name]
            elif name.startswith('del_'):
                properties[name[name.rfind('_') + 1]]['fdel'] = dct[name]
        for prop in properties.keys():
            dct[prop] = property(**properties[prop])
        return type.__new__(cls, cls_name, bases, dct)


class Example(metaclass=MyMetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


ex = Example()
ex.x = 255
print(ex.x)
print(ex.y)
