row=int(input("Enter the number of rows:"))
boolean = bool(int(input("Enter 0 or 1:")))
if boolean == True:
    n=1
    while n <= row: 
        print(n * "*" , end="\n")
        n=n+1
elif boolean == False:
    while row > 0:
        print(row * "*" , end="\n")
        row=row-1
else:
    print("Incorrect value!!")





# ALTERNATIVE METHOD USING DEF:

# row=int(input("Enter the number of rows:"))
# boolean = bool(int(input("Enter 0 or 1:")))


# def starPattern(row, boolean):
# if boolean == True:
#     n=1
#     while n <= row: 
#         print(n * "*" , end="\n")
#         n=n+1
# elif boolean == False:
#     while row > 0:
#         print(row * "*" , end="\n")
#         row=row-1
# else:
#     print("Incorrect value!!")
# starPattern(row, boolean)




        