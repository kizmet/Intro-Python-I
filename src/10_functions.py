# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    result = num%2
    if result == 1:
        result = "odd"
    else:
        result = "even"
    return result


# Read a number from the keyboard
num = input("Enter a number: ")
# num=3
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
print(is_even(num))
# YOUR CODE HERE

