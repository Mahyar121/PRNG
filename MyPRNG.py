#!/usr/bin/python
import sys

class MyPRNG:
    def __init__(self,a,m,z, m_seed, next): #zero-arg constructor for the class
        self.a = 16807 #7^5
        self.m = 2147483647 #2^31 - 1
        self.nextZ = 1
        self.currentZ = 0
    def next_prn(self): #return the next random number
        self.nextZ = ( self.a * self.currentZ ) % self.m
        return self.next
    def seed(self, rseed): # seed the generator with the given rseed
        self.currentZ = rseed