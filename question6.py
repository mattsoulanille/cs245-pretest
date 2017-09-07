"""
>>> t = TernarySearchTree("root")

>>> t
root

>>> t.insert("rootbeer")
True

>>> t.insert("aardvark")
True

>>> t.middle
['rootbeer']

>>> t.left
aardvark

>>> c = t.NewTreeWithInsertedValue("sierra")

>>> c
root

>>> c.right
sierra

>>> t.right == None
True

>>> c.insert("rootaaa")
True

>>> c.middle
['rootaaa', 'rootbeer']

>>> t.middle
['rootbeer']


"""
from copy import copy

class TernarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = []
        self.right = None

    def getChildren(self):
        return (self.left, self.right)

    def search(self, value):
        if self.value == value:
            return True

        elif self.value == value[0:len(self.value)]:
            # could use the fact that it's a sorted list
            # to make this part faster, but I want this
            # code to be readable

            return value in self.middle

        else:
            if value < self.value:
                # then it's alphabetically before it and we should search left
                return self.left.search(value)
            else:
                # search right
                return self.right.search(value)


    def insert(self, value):
        # Doesn't balance the tree
        # Inserts a value, not an instance of TernarySearchTree
        # Doesn't insert if value already present

        if self.value == value:
            raise Exception("Value already in tree")

        elif self.value == value[0:len(self.value)]:
            if value in self.middle:
                raise Exception("Value already in tree")
            else:
                # could use insertion sort here for O(n) instead of O(nlog(n))
                # since there is only 1 element, but I'm trying to make
                # my code easy to read. Or maybe python's sort is smart enough?

                self.middle.append(value)
                self.middle.sort()
                return True

        else:
            if value < self.value:
                # then it's alphabetically before it and we should insert left

                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = TernarySearchTree(value)
                    return True
            else:
                # insert right

                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = TernarySearchTree(value)
                    return True

    def copy(self):
        # only works if all values are primitives
        treeCopy = TernarySearchTree(self.value)
        treeCopy.middle = copy(self.middle)
        
        if (self.left):
            treeCopy.left = self.left.copy()

        if (self.right):
            treeCopy.right = self.right.copy()

        return treeCopy
                
    def NewTreeWithInsertedValue(self, value):
        # There's a faster way to do this (I think) if you build the tree
        # as you insert the new value, but I don't really have time

        newTree = self.copy()
        newTree.insert(value)
        return newTree
        

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



        

        
        
        
    
