import itertools as it,pdb,copy

# import WordStreakSolver as app
# mypuzzle = app.createpuzzlemap('acbrthenefdtbrjs')
# mytracker = app.createstring(mypuzzle,(1,1))

def createstringcombinations(puzzlemap):

	stringcombinations =[]
	for key in puzzlemap:
		for s in createstring(puzzlemap,key):
			stringcombinations.append(s)
	return stringcombinations


def createstring(puzzlemap,startpoint):

# a	c	b	r

# t	h	e	n

# e	f	d	t

# b	r	j	s

# acbrthenefdtbrjs
	
	#tracker = {step:[string,puzzlemap]}

	step = 1
	letter = puzzlemap[startpoint].keys()[0]
	tracker={step:[letter,startpoint,removefromadjacentcells(puzzlemap,startpoint)]}
	iterator = tracker.keys()
	for item in iterator:
		string = tracker[item][0]
		startpoint = tracker[item][1]
		puzzle = tracker[item][2]
		for coord in puzzle[startpoint][string[-1]]:
			step+=1
			iterator.append(step)
			puzzlecopy = removefromadjacentcells(puzzle,coord)
			nextletter = puzzlecopy[coord].keys()[0]
			tracker[step]=[string+nextletter,coord,puzzlecopy]
			print(string+nextletter)
	return tracker

def removefromadjacentcells(puzzlemap,coordtoremove):

	puzzlecopy = copy.deepcopy(puzzlemap)
	for cell in puzzlemap:
		for letter in puzzlemap[cell]:
			if coordtoremove in puzzlecopy[cell][letter]: puzzlecopy[cell][letter].remove(coordtoremove)
	return puzzlecopy			


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