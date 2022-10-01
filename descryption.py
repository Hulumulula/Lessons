class ReadIntX:  # Дескриптор без данных
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  # Дескпритор данных
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != float:
            raise TypeError("Координата должна быть вещественным числом.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()  # Дескпритор данных
    y = Integer()  # Дескпритор данных
    z = Integer()  # Дескпритор данных
    xr = ReadIntX()  # Дескриптор без данных

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__, p.x)
