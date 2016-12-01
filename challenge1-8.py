import binascii
import itertools


def score(line):
	block =[]
	i=0
	k = 16
	blocks = [line[i:i+k] for i in range(0, len(line), k)]

	pairs = itertools.combinations(block,2)
	same_count =0;

	for i in pairs:
		if p[0]==p[1]:
			same_count += 1

	return same_count

# line number = 0
num=0
lines = open("file1-8.txt",'r')
for line in lines:
	if line[-1] == '\n':
            line = line[:-1]
	s = binascii.unhexlify(line)
	if score(s)>0:
		print num
	num += 1

