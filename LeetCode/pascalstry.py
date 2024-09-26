class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        tri : list[list[int]] = []

        # first two rows are always just ones
        tri.append([1])
        int_curRow = 1

        while int_curRow < numRows :
            #starts with 1
            tri.append([1])

            for idx in range(1,int_curRow):
                tri[int_curRow].append(tri[int_curRow-1][idx-1] + tri[int_curRow-1][idx])

            #last is also 1
            tri[int_curRow].append(1)

            int_curRow+=1

        return tri


Solution.generate(Solution, 10)
