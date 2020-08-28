# Consider a staircase of size :

#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

def staircase(n):
    for i in range(1, n + 1):
        step = "#" * i
        print(step.rjust(n))
