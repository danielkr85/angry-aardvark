import itertools as it,pdb,copy,io

def solution(string):

	return createstringcombinations(createpuzzlemap(string))

def createstringcombinations(puzzlemap):

	print('Reading Dictionary')

	dictionary=[]
	fp = open('dictionary.txt')
	for line in fp:
		dictionary.append(line.strip('\n'))
	fp.close()

	index = createindex(dictionary)

	stringcombinations =[]
	for key in puzzlemap:
		for s in createstring(puzzlemap,key,dictionary,index):
			stringcombinations.append(s)
	results = list(set(stringcombinations))
	results.sort(key=len,reverse=True)
	return results

def createstring(puzzlemap,startpoint,dictionary,index):

	step = 1
	for key in puzzlemap[startpoint].keys(): letter = key
	tracker={step:[letter,startpoint,removefromadjacentcells(puzzlemap,startpoint)]}
	iterator = []
	for key in tracker.keys():iterator.append(key)
	for item in iterator:
		string = tracker[item][0]
		startpoint = tracker[item][1]
		puzzle = tracker[item][2]
		for coord in puzzle[startpoint][string[-1]]:
			for key in puzzle[coord].keys(): nextletter = key

			goodstart,completeword = checkdictionary(string+nextletter,dictionary,index)
			if goodstart:
				
				step+=1
				iterator.append(step)
				puzzlecopy = removefromadjacentcells(puzzle,coord)
				tracker[step]=[string+nextletter,coord,puzzlecopy]
				if len(string+nextletter)>2 and completeword: 
					
					yield string+nextletter

def removefromadjacentcells(puzzlemap,coordtoremove):

	puzzlecopy = copy.deepcopy(puzzlemap)
	for cell in puzzlemap:
		for letter in puzzlemap[cell]:
			if coordtoremove in puzzlecopy[cell][letter]: puzzlecopy[cell][letter].remove(coordtoremove)
	return puzzlecopy			

def checkdictionary(string,dictionary,index):

	if string in dictionary:
		
		return True,True

	startline = index[string[0]][0]
	endline = index[index[string[0]][1]][0]
	for i,dictline in enumerate(dictionary):
		if endline > i >= startline:
			if dictline.startswith(string):
				
				return True,False

	return False,False
	


def createpuzzlemap(string):

	puzzlemap={}
	x=1
	y=1
	for s in string:
		if y==5:
			x+=1
			y=1

		puzzlemap[(x,y)]={s:createadjacentcells((x,y))}
		y+=1
	return puzzlemap

def createadjacentcells(coord):

	xrange=()
	yrange=()
	adjacentcells=[]
	if 1 < coord[0] < 4 :
		xrange=(coord[0]-1,coord[0]+2)
	if 1 == coord[0]:
		xrange=(coord[0],coord[0]+2)
	if 4 == coord[0]:
		xrange=(coord[0]-1,coord[0]+1)

	if 1 < coord[1] < 4 :
		yrange=(coord[1]-1,coord[1]+2)
	if 1 == coord[1]:
		yrange=(coord[1],coord[1]+2)
	if 4 == coord[1]:
		yrange=(coord[1]-1,coord[1]+1)

	for n in it.product(range(xrange[0],xrange[1]),range(yrange[0],yrange[1])):
		if coord!=n: adjacentcells.append(n)
	return adjacentcells

def createindex(dictionarylist):
	
	alphabet='abcdefghijklmnopqrstuvwxyz'
	letterindex=0
	index={}
	for i,line in enumerate(dictionarylist):
		if letterindex<26:
			if alphabet[letterindex]==line[0]:
				if alphabet[letterindex]!='z': 
					index[alphabet[letterindex]]=[i,alphabet[letterindex+1]]
				else:
					index[alphabet[letterindex]]=[i,'@']
				letterindex+=1
	index['@']=[i]

	print('Index Created')

	return index