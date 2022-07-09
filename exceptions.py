#print(5/0)

def example1():

        for i in range(3):
            x = int(input( "enter a number: " ))
            y = int(input( "enter another number: " ))
            try:
                print( x, '/' , y, '=' , x/y )
            except ZeroDivisionError:
                print("Nie mozna dzielic przez zero")
            except ValueError:
                print("musisz wprowadzic liczbe")
            else:
                print(x,'/',y,'=',x/y)

example1()

def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        sumOfPairs.append(L[i]+L[i+1])
        print("sumOfPairs=",sumOfPairs)

L = [10,3,5,6,9,3]
example2(L)
example2([10,3,5 ,6 ,"NA" ,3])


def printUpperFile(fileName):
    file = open("fileName", "r" )
    for line in file:
        print(line.upper())
        file.close()

printUpperFile("doesNotExistYest.txt")
printUpperFile("./Dessssktop/misspelled.txt")