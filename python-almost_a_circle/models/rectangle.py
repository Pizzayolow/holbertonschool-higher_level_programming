#!/usr/bin/python3
'''class Rectangle that inherits from Base'''


from models.base import Base


class Rectangle(Base):
    '''rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''setter of width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        '''setter of height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        '''setter of x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        '''setter of y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''return the area'''
        return self.__width * self.__height

    def display(self):
        '''display a rectangle'''
        print(self.__y * "\n", end='')
        for i in range(self.height):
            print(self.__x * ' ', end='')
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        '''overwrite the str method'''
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args):
        '''assigns arguments'''
        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            if count == 1:
                self.__width = arg
            if count == 2:
                self.__height = arg
            if count == 3:
                self.__x = arg
            if count == 4:
                self.__y = arg
            count += 1
