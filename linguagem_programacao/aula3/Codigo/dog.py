#!/usr/bin/python
# -*- coding: utf-8 -*-

from mammal import Mammal


class Dog(Mammal):
    def __init__(self, age,weight,height,lenght,position):
        super().__init__(age,weight,height,lenght,position)
        self.breed = None

        
    def move_x(self):
        pass

    
    def move_y(self):
        pass

    
    def move_z(self):
        pass