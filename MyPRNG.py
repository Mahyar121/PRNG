#!/usr/bin/python
import sys

class MyPRNG:
    def __init__(self,a,m,z): #zero-arg constructor for the class
        self.a = 16807 #7^5
        self.m = 2147483647 #2^31 - 1
        self.z = 0
    def next_prn(self): #return the next random number
        nextRandom = ( self.a * self.z ) % self.m
    def seed(rseed): # seed the generator with the given rseed
