#combotest-2.py
from itertools import permutations
"""
Steps:
1) get input
2) all combinations - isn't that how it should work?
3) sort the combos...
4) open the file for reading - it's already in alpha order
5) grab the first word in the rack
6) scan down the file 'til there's a match - top """

""" 1: GET THE INPUT - should use a try/exept block here. """
#rack = str(input("input the rack: "))

""" 2: All COMBOS - return a list
com = itertools.combinations(rack, len(rack))
for val in com:
	print(*val)

per = itertools.permutations(rack)
print(type(per))

for val in per:
    print(*val)


per_list = list(per)
print(type(per_list))
for j in per_list:
    print(j)
"""
rack = "cat"


def cleanTheList(rack):
    temp = [''.join(i) for i in permutations(rack)]
    return sorted(temp)
    
def check_if_match(cleanList):
    i = 0
    line_number = 0
    # get the first word from rack
    word = cleanList[i]
    ngram = word[0:2]
    print("test")
    # open the dictionary file (sowpods.txt)
    f = open("combo-file.txt", "r")
    line = f.readline(line_number)
   
    print(ngram," ", line[0:2])
    if (ngram < line[0:2]):
        print("LESS")
    else:
        line_number += 1
        line = f.readline(line_number)
        print(line)

    f.close()
    """ with open("combo-file.txt") as f:
        # get the first line from that file:
        for line in f:
            if word[0:2] == line[0:2]:
                    print("\tHIT ", word[0:2], " ", line, end="")
    """   
            
def main():
    cleanList = cleanTheList(rack)
    check_if_match(cleanList)
   # f = open("combo-file.txt", "r")
#    print(f.readline())
    
 #   f.close()

if __name__ == "__main__":
    main()