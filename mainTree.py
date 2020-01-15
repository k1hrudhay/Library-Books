#+======================================================================================+
# |Author           : Kolli Hrudhay
# |Package          : Library Books
# |Module           : mainTree.py
# |Language         : Python 3.7
# |Description      : This module conatins the main methods and their respective 
#                     internal methods of the Library management system.
#                     This module is being imported by the Assignment_code.py module 
#                     and these methods are called according to the imput provided.
#                     
#+======================================================================================+


from bookNode import bookNode
import re
from copy import copy
from BFS import BFS

class mainTree:

    def __init__(self):
        self.books = []
        self.root=None


    
    def createTree(self,books, root, i, n):
        # Method to create the Binary Tree.

        if i < n:
            temp = bookNode(books[i][0], books[i][1])
            if i==0:
                self.root=temp

            root = temp
            # insert left child  
            root.left = self.createTree(books, root.left, 2 * i + 1, n)
            # insert right child  
            root.right = self.createTree(books, root.right, 2 * i + 2, n)

        return root

    
    def preOrdertraversal(self,root): 
        # Method to print the books (elements of) Binary Tree using Pre-Order Traversal.

        if root: 
            print(root.bookID) 
            self.traversal(root.left)  
            self.traversal(root.right)


    
    def _readBookList(self,bkID, availCount):
        ''' This method is triggered when Assignment_code.py module is executed.
            This method reads the book ids and the number of copies available. 
        '''
        
        self.books.append([bkID, availCount])
        root=copy(self.root)
        n = len(self.books)
        root = self.createTree(self.books, root, 0, n)


    
    def traverseCICO(self,bkid,root,inOut,templist):
        # Traversal method for _chkInChkOut method.

        if root:
            if root.bookID==bkid:
                templist.remove(bkid)
                with open('outputPS6.txt','a') as ft:
                    ft.write("===>  "+"The details of book with book id "+str(bkid)+" before the check in/out are : "+'\n'+'\n')
                    ft.write('\t'+"Book id = "+str(root.bookID)+'\n'+'\t'+"Available count = "+str(root.avCntr) + '\n' +'\t'+ "No of times checked out till now = "+str(root.chkOutCntr)+'\n'+'\n')
                    if inOut=='checkOut':
                        if root.avCntr > 0:
                            root.chkOutCntr += 1
                            root.avCntr -= 1
                            ft.write('\t'+"The details of book with book id "+str(bkid)+" after the check out are : "+'\n'+'\n')
                            ft.write('\t'+"Book id = "+str(root.bookID)+'\n'+'\t'+"Available count = "+str(root.avCntr) + '\n' +'\t'+ "No of times checked out till now = "+str(root.chkOutCntr)+'\n'+'\n')
                        else:
                            #with open('outputPS6.txt','a') as ft:
                                ft.write("The book with book id "+str(bkid)+" cannot be checked out as all copies of the book have been checked out."+'\n'+'\n')
                        

                    elif inOut=='checkIn':
                        root.avCntr +=1
                        ft.write('\t'+"The details of book with book id "+str(bkid)+" after the check in are : "+'\n'+'\n')
                        ft.write('\t'+"Book id = "+str(root.bookID)+'\n'+'\t'+"Available count = "+str(root.avCntr) + '\n' + '\t'+"No of times checked out till now = "+str(root.chkOutCntr)+'\n'+'\n')
                        
                
            else:
                self.traverseCICO(bkid,root.left,inOut,templist)
                self.traverseCICO(bkid,root.right,inOut,templist)

        return(templist)


    
    def _chkInChkOut(self, bkID, inOut): 
        ''' This method is triggered when the tags 'checkOut or checkIn' is encountered in the promptsPS6.txt file.
            This method updates the check in / check out status of a book based on the book id 
            and also provide the details of the book before and after the check in/out. 
        '''

        templist=[]
        templist.append(bkID)
        templist=self.traverseCICO(bkID,self.root,inOut,templist)
        for i in templist:
            if i:
                with open('outputPS6.txt','a') as f:
                    f.write("--->  ""Book with book id "+str(i)+" is not available in the Library."+'\n'+'\n')


    
    def traverseGTB(self,root,temp):
        # Traversal method for _getTopBooks method.

        if root:
            if root.chkOutCntr != 0:
                temp.append([root.bookID,root.chkOutCntr])
            self.traverseGTB(root.left,temp)
            self.traverseGTB(root.right,temp)

        return temp


    
    def _getTopBooks(self, bkNode): 
        ''' This method is triggered when the tag 'ListTopBooks' is encountered in the promptsPS6.txt file.
            The method searches through the list of books and the checkout counter and determines
            which are the top three books that have been checked out the most and lists those books and 
            the number of times they have been checked out into the outputPS6.txt file. 
        '''

        root=bkNode
        temp=[]
        temp=self.traverseGTB(root,temp)
        temp.sort(reverse=True,key=lambda x:x[1])
        keys=sorted(list([i[1] for i in temp]),reverse=True)
        keycount=sorted(list([i,keys.count(i)] for i in set(keys)),reverse=True,key=lambda x:x[0])[:3]

        with open('outputPS6.txt','a') as f1:
            f1.write("List of top books that have been checked out :"+'\n')
            cnt=1
            for i in keycount:
                for j in temp:
                    if i[0]==j[1]:
                        text='Top Books '+str(cnt)+': '+j[0]+', '+str(j[1])+'\n'
                        f1.write(text)

                cnt=cnt+1 if cnt<3 else 3

        with open('outputPS6.txt','a') as f1:
            f1.write('\n'+'\n')


    
    def traverseNI(self,bkNode,temp):
        # Traversal method for notIssued method.

        if bkNode:
            if bkNode.chkOutCntr == 0:
                temp.append(bkNode.bookID)

            self.traverseNI(bkNode.left,temp)
            self.traverseNI(bkNode.right,temp)

        return temp


    
    def notIssued(self, bkNode):
        ''' This method is triggered when the tag 'BooksNotIssued' is encountered in the promptsPS6.txt file.
            The method searches the list of books in the system and generates a list of books 
            which have never been checked out. The output of this list is put into the outputPS6.txt file. 
        '''

        temp=[]
        temp=self.traverseNI(bkNode,temp)

        if temp:
            with open('outputPS6.txt','a') as f2:
                f2.write("List of books not issued:"+'\n')
                for i in temp:
                    f2.write(i+'\n')

        else:
            with open('outputPS6.txt','a') as f2:
                f2.write("All books are issued atleast once"+'\n')

        with open('outputPS6.txt','a') as f2:
            f2.write('\n'+'\n')
                

    
    def traverseFB(self,root,bkID,templist,bklist):
        # Traversal method for _findBook method.

        if root:  
            if root.bookID == bkID:
                if root.avCntr > 0 :
                    templist.append([root.bookID,1])
                else:
                    templist.append([root.bookID,0])

            else:
                self.traverseFB(root.left,bkID,templist,bklist)
                self.traverseFB(root.right,bkID,templist,bklist)

        for i in bklist:
            if i in [j[0] for j in templist]:
                bklist.remove(i)
        return templist,bklist
        

    
    def _findBook(self,eNode, bkID):
        ''' This method is triggered when the tag 'findBook' is encountered in the promptsPS6.txt file.
            This method reads the promptsPS6.txt file to get the book id that needs to be 
            searched for availability in the system. The method reads the id from the file 
            promptsPS6.txt where the search id is mentioned with the tag 'findBook'. 
        '''

        bklist=[]
        bklist.append(bkID)
        templist=[]      
        templist,bklist=self.traverseFB(eNode,bkID,templist,bklist)
        
        if bklist:
            with open('outputPS6.txt','a') as f3:
                for i in bklist:
                    f3.write("Book with book id "+str(i)+" is not present in the Library."+'\n')

        if templist:
            with open('outputPS6.txt','a') as f3:
                for i in templist:
                    if i[1] == 0:
                        f3.write("All copies of book id "+str(i[0])+" have been checked out."+'\n')
                    else:
                        f3.write("Book id "+str(i[0])+" is available for checkout."+'\n')
                
        with open('outputPS6.txt','a') as f3:
            f3.write('\n')

    
    def traverseSO(self,eNode,templ):
        # Traversal method for _stockOut method.

        if eNode:
            if eNode.avCntr <= 0:
                templ.append(eNode.bookID)

            self.traverseSO(eNode.left,templ)
            self.traverseSO(eNode.right,templ)

        return templ


    def _stockOut(self, eNode):
        ''' This method is triggered when the tag 'ListStockOut' is encountered in the promptsPS6.txt file.
            This method searches for books for which all the available copies have been checked 
            out and outputs the list into the outputPS6.txt file. 
        '''

        templ=[]
        templ=self.traverseSO(eNode,templ)

        if templ:
            with open('outputPS6.txt','a') as f4:
                f4.write("All available copies of the below books have been checked out:"+"\n")
                for i in templ:
                    f4.write(i+'\n')

        else:
            with open('outputPS6.txt','a') as f4:
                f4.write("None of the books present in the Library have all the copies being checked out."+"\n")
        

        with open('outputPS6.txt','a') as f4:
            f4.write('\n'+'\n')

    
    def printBooks(self, bkNode):
        ''' This method is triggered when the tag 'ListStockOut' is encountered in the promptsPS6.txt file.
            This method prints the list of book ids and the available number of copies 
            in ascending order of book id in the file outputPS6.txt.
        '''

        templist=[]
        bfstraverse=BFS()
        templist=bfstraverse.bfs(self.root)

        with open('outputPS6.txt','a') as f5:
            f5.write("\n"+"There are a total of "+str(len(templist))+" book titles in the library:"+"\n")
        
            for i in templist:
                f5.write(str(i[0])+','+str(i[1])+'\n')
