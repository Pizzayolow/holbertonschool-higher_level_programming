#!/usr/bin/python3
'''class square that inherits from Rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor of the square class'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''overwriting str class'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        '''setter of size for square'''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        '''update for square'''
        count = 0
        if not kwargs:
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''dict representation of square'''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
