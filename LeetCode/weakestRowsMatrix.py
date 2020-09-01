# Given a m * n matrix mat of ones (representing soldiers)
# and zeros (representing civilians), return the indexes
# of the k weakest rows in the matrix ordered from the
# weakest to the strongest.

# A row i is weaker than row j, if the number of
# soldiers in row i is less than the number of soldiers in
# row j, or they have the same number of soldiers but i is
# less than j. Soldiers are always stand in the frontier of a
# row, that is, always ones may appear first and then zeros.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        soldiers = []

        for i in range(len(mat)):
            soldiers.append([sum(mat[i]), i])

        soldiers.sort()

        return [soldiers[i][1]for i in range(k)]
