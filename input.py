# !\usr\bin\env python3
# -*- coding: utf-8 -*-
'''
2020/2/21
RE to input information about 
Precision
NodeID,NodeType,ActivePower,ReactivePower,NodeVoltage # every node
...
BranchID,RelevantNodeID_1,RelevantNodeID_2,BranchResistance,BranchReactance # every branch
...
2020/2/22
add a function to check whether the input is legal
'''

__author__ = '60kVTS'

import re 

class RE(object):                 
    def __init__(self,data): 
        self.NodeCount = 0
        self.Nodes = {} #a dict {NodeID:NodeCount}
        self.Branches = {} #a dict {Branches:lines in _s}
        self._s = data
        self._s = re.match(r'^\d[0-9a-zA-Z\.\,\n\-\s]+\d',self._s).group(0)
        self._s = re.split(r'\n',self._s)
        self._s = list(map(lambda s : re.split(r'\,\s*',s),self._s))
        #function to check whether the input is legal
        if len(self._s[0]) != 1:
            raise ValueError('First line does not have more than one arguments')
        for i in range(1,len(self._s)):
            if len(self._s[i]) == 4:
                self.NodeCount += 1
                __ID = int(self._s[i][0])
                __Type = self._s[i][1]
                if __Type == 'PQ':
                    self.Nodes.update({__ID:self.NodeCount})
                elif __Type == 'PV':
                    self.Nodes.update({__ID:self.NodeCount})
                elif __Type == 'V':
                    self.Nodes.update({__ID:self.NodeCount})
                else:
                    self.NodeCount -= 1
                    raise ValueError('Node %d input error or branch %d lost an argument' % (__ID,__ID)) 
            elif len(self._s[i]) == 5:
                __ID = int(self._s[i][0])
                __n1 = int(self._s[i][1])
                __n2 = int(self._s[i][2])
                if __n1 in self.Nodes:
                    if __n2 in self.Nodes:
                        self.Branches.update({__ID:i})
                    else:
                        raise ValueError('Node %d does\'t exist (in branch %d)' % (__n2,__ID))
                else:
                    if __n2 in self.Nodes:
                        raise ValueError('Node %d does\'t exist (in branch %d)' % (__n1,__ID))
                    else:
                        raise ValueError('Node %d,%d does\'t exist (in branch %d)' % (__n1,__n2,__ID))
            else:
                raise ValueError(self._s[i],'is illegal')
    def __str__(self):
        return '%s' % self._s
    __repr__ = __str__
    def __len__(self):
        return len(self._s)
            
if __name__ == '__main__':
    with open('input.txt','r',encoding='utf-8') as f:
        s = RE(f.read())

