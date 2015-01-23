import sys
from pprint import pprint
from itertools import *

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(
            combinations(s, r) for r in range(len(s)+1)))

def is_closed(G):
    pass

def is_associative(G):
    pass

def has_identity(G):
    pass

def has_inverses(G):
    pass

def is_group(G):
    return (is_closed(G)
            and is_associative(G)
            and has_identity(G)
            and has_inverses(G))

class Z_mod(object):
    def __init__(self, n):
        self.n = n
        self.classes = [EquivClass(n,i) for i in range(0,n)]
        self.e = self.classes[0]

    def __len__(self):
        return self.n

    def __iter__(self):
        return iter(self.classes)

    def __getitem__(self, k):
        return self.classes(k)

    def sum(self, lst):
        if len(lst) == 0: return
        total = self.e
        for c in lst:
            total += c
        return total

    def find_subgroups(self):
        # subgroups = [s for s in powerset(self.classes)
        #     if len(s) > 0 and self.sum(list(s)).a == 0]
        subgroups = []
        for i,s in enumerate(powerset(self.classes)):
            print '...', float(i/(2**self.n))*100, '\t', i
            if len(s) > 0 and self.sum(list(s)).a == 0:
                subgroups.append(s)
        return subgroups


# def sum_equiv_classes(lst):
#     if len(lst) == 0: return
#     total = EquivClass(lst[0].n, 0)
#     for c in lst:
#         total += c
#     return total

class EquivClass(object):
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def __sub__(self, other):
        assert self.n == other.n
        return EquivClass(self.n, (self.a - other.a) % self.n)

    def __add__(self, other):
        if isinstance(other, EquivClass):
            assert self.n == other.n
            return EquivClass(self.n, (self.a + other.a) % self.n)
        elif isinstance(other,int):
            return self

    def __mul__(self, other):
        if isinstance(other, EquivClass):
            assert self.n == other.n
            return EquivClass(self.n, (self.a * other.a) % self.n)
        elif isinstance(other, int):
            s = EquivClass(self.n, 0)
            for _ in range(other):
                s += self
            return s

    def __repr__(self):
        return '<{}>'.format(self.a)

def main():
    if len(sys.argv) < 2:
        print 'Give me an integer n!'
        return

    n = int(sys.argv[1])
    Z_n = Z_mod(n)

    pprint(Z_n.find_subgroups())

if __name__ == '__main__':
    main()