# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:27:08 2018

@author: mzamp
"""
"""How to create a class called Coordinate"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2  
        return (x_diff_sq + y_diff_sq)**0.5
    
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    def __str__(self):
        return "<" +str(self.x) +"," + str(self.y) + ">"   
    
    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        else:
            return False  
        
    def __repr__(self):
        return ('Coordinate({},{})'.format(self.getX(), self.getY())) 