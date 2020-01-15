#+======================================================================================+
# |Author           : Kolli Hrudhay
# |Package          : Library Books
# |Module           : Assignment_code.py
# |Language         : Python 3.7
# |Description      : This is the main module(script file) to be executed which 
#                     will read input from 'inputPS6.txt'file and call the 
#                     functions/methods from their respective modules.
#                     
#+======================================================================================+



from readingFun import readingFun as RF
from bookNode import bookNode
from mainTree import mainTree


books=RF('inputPS6.txt')

with open('outputPS6.txt', 'w') as opf: 
    pass

maintree=mainTree()

for i in books:
    maintree._readBookList(i[0], int(i[1]))


commands1=RF('promptsPS6.txt')


for i in commands1:
    if(i[0] in ['checkOut','checkIn']):
        maintree._chkInChkOut(i[1],i[0])

    elif(i[0] == 'ListTopBooks'):
        maintree._getTopBooks(maintree.root)

    elif(i[0] == 'BooksNotIssued'):
    	maintree.notIssued(maintree.root)

    elif(i[0] == 'findBook'):
    	maintree._findBook(maintree.root,i[1])

    elif(i[0] == 'ListStockOut'):
    	maintree._stockOut(maintree.root)

    elif(i[0] == 'printInventory'):
    	maintree.printBooks(maintree.root)

