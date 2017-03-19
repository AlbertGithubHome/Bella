def solutions(x,y,X,Y):
	# print 'X={},Y={}'.format(X,Y)
	return {
			(X,y):'fill X',
			(x,Y):'fill Y',
			((0,y+x) if y+x <=Y else (x-(Y-y),Y)):'X->Y' ,
			((x+y,0) if x+y<=X else (X,y-(X-x))):'Y->X',
			(0,y):'empty x',
			(x,0):'empty y'
			}

res=[]
def pour_problem(X,Y,goal,start=(0,0)):
	print(start)
	if goal in start:
		return [start]
	explored=set([(0,0)])
	frontier=[[start]]
	i=0

	while frontier:
		print("\ni =", i)
		print("frontier =", frontier)
		path=frontier.pop(0)
		(x,y)=path[-1]
		i+=1
		
		print("path =", path)
		print("explored =", explored)

		solu = solutions(x,y,X,Y).items();
		print("solu =", solu)

		for (state,action) in solu:
			if state not in explored:
				explored.add(state)
				path2=path+[action,state]
				if goal in state:
					return path2
				else:
					frontier.append(path2)
					#frontier.insert(0, path2)
					#frontier = path2 + frontier

	return Fail

Fail=[]
#when X water:3,Y water :5 ,goal 4
print('when X water:3,Y water :5 ,goal 4\n=>{}'.format(pour_problem(3,5,4)))

L = { (0,0):'fill X', (0,0):'fill Y', (0,0):'empty x', (0,0):'empty y' }
#print(L)

L = set([(0,0)])
#print(L)
