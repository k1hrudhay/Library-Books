#+======================================================================================+
# |Author           : Kolli Hrudhay
# |Package          : Library Books
# |Module           : BFS.py
# |Language         : Python 3.7
# |Description      : This module is called by the printBooks method from the 
#                     mainTree.py module. This module helps the printBooks method to 
#                     print the list of books present in the Library in ascending 
# 					  order of book id.
# 
#+======================================================================================+


from bookNode import bookNode


class BFS:

	def bfs(self,root):
		templist=[]
		height=self.height(root)
		for i in range(height):
			self.bfsTraverse(root,i,templist)

		return templist

	def height(self,root):
		if root is None:
			return 0

		else:
			lheight=self.height(root.left)
			rheight=self.height(root.right)

			if lheight > rheight:
				return lheight + 1
			else:
				return rheight + 1

	def bfsTraverse(self,root,level,templist):
		if root is None:
			return

		elif level==0:
			temp=root.avCntr
			templist.append(([root.bookID,temp]))

		elif level>0:
			self.bfsTraverse(root.left,level-1,templist)
			self.bfsTraverse(root.right,level-1,templist)
