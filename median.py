listmedian=list(input('list'))
sor=sorted(listmedian,reverse=True)
listlen=len(sor)

if listlen % 2 != 0:
	print('list is odd length')
	median = sor[int(listlen/2-0.5)]
else:
	print('list is even lenghth')
	median=(sor[int(listlen/2)-1]+sor[int(listlen/2)])/2

print(' this is my sorted list %s' %(sor))
print('average of the list is %s' %(median))

