from itertools import permutations


def is_prime(n):
	if n <=1:
		return False
	elif n <=3:
		return True
	elif n%2 == 0 or n%3 == 0:
		return False
	i = 5
	if i * i <= val:
		if val % i == 0 or val % (i+2)==0:
			return False
		i +=6
	return True
	
	
def iterToolPerms(word):
	perms = [''.join(p) for p in permutations(word)]
	return perms
	
	
# def permut(word):
    # if len(word)<=1:
        # return [word]
    # #get all permutations of length N-1
    # perms=permutations(word[1:])
    # char=word[0]
    # result=[]
    # #iterate over all permutations of length N-1
    # for perm in perms:
        # #insert the character into every possible location
        # for i in range(len(perm)+1):
            # result.append(perm[:i] + char + perm[i:])
    # return result
	
	
def lexiographAllPrime(val):
	permu = iterToolPerms(str(val))
	permuList = map(lambda x: int(x),permu)
	for val in permuList:
		if(not is_prime(val)):
			return False
	return True
	
primeCounter =0
for val in range(1,1000000):
	if(lexiographAllPrime(val)):
		primeCounter+= 1

print("There are {0} circular primes".format(primeCounter))
	
	