import itertools as it,pdb,copy,io,sys


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

def rankresults(results):

	lettervalues = {'a':1,'b':4,'c':4,'d':2,'e':1,'f':4,'g':2,'h':3,'i':1,'j':10,'k':3,'l':2,'m':4,'n':2,'o':1,'p':4,'q':8,'r':1,'s':1,'t':1,'u':2,'v':5,'w':4,'x':10,'y':10,'z':10}

	newresults=[]
	for word in results:
		value = 0
		for letter in word:
			value = value + lettervalues[letter]
		newresults.append([value,word])


	return newresults


def createstring(puzzlemap,startpoint,dictionary,index):

	step = 1
	for key in puzzlemap[startpoint].keys(): letter = key
	tracker={step:[letter,startpoint,removefromadjacentcells(puzzlemap,startpoint)]}
	iterator = []
	for key in tracker.keys():iterator.append(key)
	for item in iterator:
		string = tracker[item][0]
		if string == 'q': string = 'qu'
		startpoint = tracker[item][1]
		puzzle = tracker[item][2]
		for coord in puzzle[startpoint][string[-1]]:
			for key in puzzle[coord].keys(): 

				nextletter = key
				if nextletter == 'q': nextletter = 'qu'

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

	stringlength = len(string)

	if stringlength >4: 
		stringlength = 4
	else: 
		if string in index:
			return True,False
		else:
			return False,False

	for word in index[string[0:stringlength]]:
		if word.startswith(string):
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
	
	index={}
	for line in dictionarylist:
		if line[0] in index:
			index[line[0]].append(line)
		else:
			index[line[0]]=[line]

	for line in dictionarylist:
		if line[0:2] in index:
			index[line[0:2]].append(line)
		else:
			index[line[0:2]]=[line]

	for line in dictionarylist:
		if line[0:3] in index:
			index[line[0:3]].append(line)
		else:
			index[line[0:3]]=[line]

	for line in dictionarylist:
		if line[0:4] in index:
			index[line[0:4]].append(line)
		else:
			index[line[0:4]]=[line]

	for line in dictionarylist:
		if line[0:5] in index:
			index[line[0:5]].append(line)
		else:
			index[line[0:5]]=[line]

	print('Index Created')

	return index

solution(sys.argv[1])