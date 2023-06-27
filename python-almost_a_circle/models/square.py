#!/usr/bin/python3
'''class square that inherits from Rectangle'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor of the square class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overwriting str class'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
