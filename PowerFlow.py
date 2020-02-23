# !\usr\bin\env py 
# -*- coding: utf-8 -*-
'''
Class BuildY build a Node admittance matrix

'''
__author__ = '60kVTS'

import input 
import numpy as np

class BuildY(object):
    def __init__(self,b,precision=4):
        __n = len(b.Nodes) # n*martix
        self.Y = np.zeros((__n,__n),dtype=complex)
        self.index = [i for i in b.Nodes]
        for k,v in b.Branches.items():
            n1,n2,gg,bb = b.Nodes[int(b._s[v][1])],b.Nodes[int(b._s[v][2])],float(b._s[v][3]),float(b._s[v][4])
            n1 -= 1;n2 -= 1
            y = (1 / complex(gg,bb))
            y= complex(round(y.real,precision),round(y.imag,precision))
            self.Y[n1][n2] = -y
            self.Y[n2][n1] = -y
            self.Y[n1][n1] += y
            self.Y[n2][n2] += y
    def __str__(self):
        return '%s' % self.Y
    __repr__ = __str__
    def _printout(self,precision = 4):
        with open('BuildY.txt','w',encoding='utf-8') as f:
            f.write('%s' % self.Y)

if __name__ == '__main__':
    with open('input.txt','r',encoding='utf-8') as f:
        s = input.RE(f.read())
    y = BuildY(s,2)
    y._printout()

