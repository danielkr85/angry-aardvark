def answer(h,q):

	result = []

	for i in q:
		if i+1 >= 2**h-1:
			result.append(-1)
		else:
			result.append(rootnode(h,i))


	return result

def rootnode(height,i):

	rootlabel = 2**height-1
	label = rootlabel

	if height ==2 and i<=1:

		return label

	else:

		while not (label-1)/2 <= i+1 < label :
			height-=1
			label = 2**height-1

		if i == label-2 or i == int((label-1)/2)-1: return label
		
		while not label - height  < i < label - 1 


height - 1 * 2



# class internalnode():

# 	def __init__(label,height,rootlabel,i):

# 		self.label = label
	
		
		
# 		if height ==2:
			
# 			if self.label == rootlabel:
# 				label = 1
# 			leftnode = leafnode(label,index)
# 			layout[index]=leftnode.label
			
# 			rightnode = leafnode(leftnode.label+1,index)
# 			label = rightnode.label+1
# 			layout[index]=label
		
# 			layout[index]=rightnode.label

# 			del leftnode
# 			del rightnode

# 			for i in layout.keys():
# 				if i not in q:
# 					del layout[i]


# 		else:

# 			leftnode = internalnode(label,height-1,rootlabel,layout,index,q)
# 			layout[index]=leftnode.label
# 			index+=1
# 			rightnode = internalnode(leftnode.label+1,height-1,rootlabel,layout,index,q)
# 			label = rightnode.label+1
# 			layout[index]=label
# 			index+=1
# 			layout[index]=rightnode.label

# 			del leftnode
# 			del rightnode

# 			for i in layout.keys():
# 				if i not in q:
# 					del layout[i]

# class leafnode(tree):

# 	def __init__(self,label,index):

# 		label = label
# 		index = index

