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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        '''setter of size for square'''

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = value
            self.height = value
