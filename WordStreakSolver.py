import itertools as it,pdb


def createstringcombinations(puzzlemap):

	stringcombinations =[]
	for key in puzzlemap:
		for s in createstring(puzzlemap,key):
			stringcombinations.append(s)
	return stringcombinations


def createstring(puzzlemap,coords,startpoint):

# a	c	b	r

# t	h	e	n

# e	f	d	t

# b	r	j	s

# acbrthenefdtbrjs

	


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