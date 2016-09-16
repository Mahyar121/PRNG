#!/usr/bin/python
import sys
# Author: Mahyar Haji Babaie
# Email: mahyarhajibabaie@csu.fullerton.edu
# This file generates a random number
class MyPRNG:
    def __init__(self): #zero-arg constructor for the class
        self.a = 16807 #7^5
        self.m = 2147483647 #2^31 - 1
        self.currentZ = 1
    def next_prn(self): #return the next random number
        self.currentZ = ( self.a * self.currentZ ) % self.m
        return self.currentZ
    def seed(self, rseed): # seed the generator with the given rseed
        self.currentZ = rseed