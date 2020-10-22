import sys

def spiral(n):
    spList = []                             # Created a list to ut all the numbers in
    a=0
    #x=0
    print(1)
    for i in range(3, n*n, 2):
        list.append(i)                      # When a number is found add to a list so that you can sum all the numbers together at the end
        a = a + 1
        print(list)
        if (a == 4):
            break
        #while (a > 4):
            #for i in range (i+4, n*n, 4):
                #print(i)
                #x = x + 1
                #if (x == 5):
                    #print("end")
    #solution = sum(spList)                  #add all the number in the list to find the solution
    print(spList)

print(spiral(5))


# The array or grid is spiraling outwards in a clockwise direction
# Every corner digit is being counted starting at 1
# It starts out as every odd number. 1, 3, 5, 7, 9
# Then it skips 11 and goes to 13. And continues to count every other odd number
# 13, 17, 21, 25
# We can infer that every spiral consists of 4 numbers (the 4 corners of the spiral)
# From there it starts off as every odd number, then  after the 8th number its every other odd number, then after 16 numbers its every other other odd number and so on.

#size = 5
#def print_square(square):
    #print("-"*(2*size))
    #for y in range(len(square)):
       #for x in range(len(square[y])):
           #print("{:6}".format(square[x][y]), end="")
       #print()
    #print("-"*(2*size))


#square = [[f"{x}.{y}" for x in range(size)] for y in range(size)]

#print_square(square)
