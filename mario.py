import cs50

# initialize height to 0 so the program prompts user at least once
height = 0

# make sure number provided is between 1 and 8
while height < 1 or height > 8:

    # prompt user for a height
    height = cs50.get_int("Enter height: ")
# itarate through height     
for i in range(height):
    # on every line first add spaces
    print(" " * (height - i - 1), end="")
    # on the same line add the hashtag
    print("#" * (i + 1), end="")
    # add the wide space between both pirmids
    print("  ", end="")
    # on the same line add the hashtag
    print("#" * (i + 1), end="")
    # move to the next line
    print("")