#+======================================================================================+
# |Authors          : Kolli Hrudhay
# |Package          : Library Books
# |Module           : bookNode.py
# |Language         : Python 3.7
# |Description      : This module defines the node of the tree.
#					  When this module is called, an Object of the class bookNode 
#					  will be instantiated with respective attributes(properties).
#					  These objects form the nodes of our Binary Tree.
#
#+======================================================================================+



class bookNode:
    def __init__(self, bkid, availCount):
        self.bookID = bkid
        self.avCntr = availCount
        self.chkOutCntr = 0
        self.left = None
        self.right = None
