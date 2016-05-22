import os

FILENAME = './items.json'

if not os.path.exists(FILENAME):
	print("file %s not exists." % FILENAME)
	exit(1)

f = open(FILENAME, 'r')
itemsList = eval(f.read())
f.close()

allList = []
for item in itemsList:
	vidup = item['vidup']
	vid = item['vid']
	viddown = item['viddown']
	print('%s->%s->%s\n' % (vidup, vid, viddown))
	if vidup not in allList:
		allList.append(vidup)
	if vid not in allList:
		allList.append(vid)
	if viddown not in allList:
		allList.append(viddown)

for ak in allList:
	print ak," "