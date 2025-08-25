#!/usr/bin/python
# -*- coding: utf-8 -*-

from Codigo.animal import Animal
from abc import ABC

class Mammal(Animal,ABC):
    def __init__(self,age,weight,height,lenght,position):
        super().__init__(age,weight,height,lenght,position)
        self.fur_type = None
        self.fur_color = None
        self.eye_color = None 

    def fur_type(self,):
        pass
