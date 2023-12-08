# Get the size of the square from the user
n = int(input("Enter the size of the square: "))

# Draw the square using the print function ????
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end=" ")
        else:
         print(" ", end=" ")
    print("")  # Move to the next line after each row

@@@@@
