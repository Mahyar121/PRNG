#!/usr/bin/python
import sys

class MyPRNG:
    def __init__(self,z,a,m): #zero-arg constructor for the class
        self.z = 0
        self.a = 0
        self.m = 101
    def next_prn(self): #return the next random number
        nextRandom = ( self.a * self.z ) % self.m
    def seed(rseed): # seed the generator with the given rseed
        asdasdasd