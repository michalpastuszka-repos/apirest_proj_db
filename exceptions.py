#print(5/0)

# def example1():
#     for i in range(3):
#         try:
#             x = int(input( "enter a number: " ))
#             y = int(input( "enter another number: " ))
#             print( x,'/',y, '=',x/y )
#             print('udalo sie')
#         except ZeroDivisionError:
#             print("Nie mozna dzielic przez zero")
#         except ValueError:
#             print("blad valueError-nie wprowadziles liczby!!!")
#         else:
#             example1()

# example1()


def example2(L):
    print("\n\nExample 2")
    try:
        sum = 0
        sumOfPairs = []
        for i in range(len(L)):
            sumOfPairs.append(L[i]+L[i+1])   #dodaje kolejne elementy listy
            print("sumOfPairs=",sumOfPairs)
    except IndexError:
        ('brakuje juz elementow w liscie')
    except TypeError:
        print("list [L] zawiera litere nie liczbe")



L = [10,3,5,6,9,3]
example2(L)
example2([10,3,5 ,6 ,"NA" ,3])
example2( [ 10 , 3 , 5 , 6 ] )
#



























# def printUpperFile(fileName):
#     file = open("fileName", "r" )
#     for line in file:
#         print(line.upper())
#         file.close()
#
# printUpperFile("doesNotExistYest.txt")
# printUpperFile("./Dessssktop/misspelled.txt")