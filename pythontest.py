import sys
'''create a dict to store word elements of the textfile passed as command line argument'''
t = {}
argv = sys.argv[1]

'''open, read, and split the textfile to get each str word element'''
f = open(argv)
str = f.read().split()
'''iterate through each word and count the number of occurences'''
for word in str:
    if word in t:
        t[word] += 1 
    else:
        t[word] = 1

'''sorting the elements using lambda anonymous function that takes x as parameter for the second element meaning the number of words, reverse it so that the largest number is at the top '''
sort = sorted(t.items(), key = lambda x:x[1], reverse = True)
print (sort)
