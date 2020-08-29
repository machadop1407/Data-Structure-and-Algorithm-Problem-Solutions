# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .

# Apple and orange(2).png

# When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.

# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?


def countApplesAndOranges(s, t, a, b, apples, oranges):

    appleAmount = 0
    orangeAmount = 0

    for i in apples:
        if (a + i) >= s and (a+i) <= t:
            appleAmount += 1

    print(appleAmount)

    for i in oranges:
        if (b + i) >= s and (b+i) <= t:
            orangeAmount += 1

    print(orangeAmount)
