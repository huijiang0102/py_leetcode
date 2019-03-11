class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        bmap = collections.defaultdict(list)
        arow = len(A)
        acol = len(A[0])
        bcol = len(B[0])
        brow = len(B)
        res = [[0 for _ in range(bcol)] for _ in range(arow)]
        for row in range(brow):
            for col in range(bcol):
                if B[row][col]:
                    bmap[row].append(col)
        for ar in range(arow):
            for ac in range(acol):
                if A[ar][ac] and bmap[ac]:
                    for bc in bmap[ac]:
                        print(A[ar][ac])
                        print(B[ac][bc])
                        print(A[ar][ac] * B[ac][bc])
                        res[ar][bc] += A[ar][ac] * B[ac][bc]
        return res