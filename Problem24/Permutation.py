#Remove first Letter Algo
def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
	
digitAsString = "0123456789"
permuatatedArray = permutations(digitAsString)
print("The permutation at 1000000th position is {0}".format(permuatatedArray[1000000]))