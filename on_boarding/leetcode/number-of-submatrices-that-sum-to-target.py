class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]

        count = 0
        for i in range(n):
            for j in range(i, n):
                prefix_sum = {0: 1}
                cur_sum = 0
                for k in range(m):
                    cur_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += prefix_sum.get(cur_sum - target, 0)
                    prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return count