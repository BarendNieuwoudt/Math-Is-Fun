import math as m, random as r, sys

max, iter = int(sys.argv[1]), int(sys.argv[2])
count = 0

for x in range(iter):
	# count occurences of gcd == 1
	if m.gcd(r.randrange(1, max), r.randrange(1, max)) == 1:
		count = count + 1

# Sqrt(6 / probability(gcd == 1))
# will give you an estimation of the value of Pi
print(str(m.sqrt(6/(count/iter))))