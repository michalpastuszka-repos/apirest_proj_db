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
#             print("To raczej liczba nie jest. Spróbuj ponownie!!!!")
#         else:
#             example1()

# example1()


# def example2(L):
#     try:
#         print("\n\nExample 2")
#         sumOfPairs = []
#         for i in range(len(L)):
#             sumOfPairs.append(L[i]+L[i+1])
#             print("sumOfPairs=",sumOfPairs)
#     except IndexError:
#         print('Koniec listy -> brakuje juz elementow w liscie do dodawania')
#     except TypeError:
#         print("lista [L] zawiera litere nie liczbe -> nie moge dodac liczby do litery")
#     else:
#         example2(L)
#
#
# L = [10,3,5,6,9,3]
# example2(L)
# example2([10,3,5,6,"NA",3])
# example2([10,3,5,6])

def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
        for line in file:
            print(line.upper())
    except FileNotFoundError as e:
        print(f"nie ma takiego pliku {fileName}-> {type(e)}")
    else:
        file.close()

printUpperFile("doesNotExistYest.txt")
printUpperFile("./Dessssktop/misspelled.txt")

