#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, age,weight,height,lenght,position):
        self.age = age
        self.height = height
        self.weight = weight
        self.lenght = lenght
        self.position = position


    @abstractmethod
    def move_x(self):
        pass

    @abstractmethod
    def move_y(self):
        pass

    @abstractmethod
    def move_z(self):
        pass