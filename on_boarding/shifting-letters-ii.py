class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        shift_sum = [0] * size

        for shift in shifts:
            start = shift[0]
            end = shift[1]

            if shift[2] == 0:
                shift_sum[start] -= 1

                if end + 1 < size:
                    shift_sum[end + 1] += 1
            else:
                shift_sum[start] += 1

                if end + 1 < size:
                    shift_sum[end + 1] -= 1
                
        for i in range(1,size):
            shift_sum[i] += shift_sum[i-1]

        res = []
        for i in range(size):
            idx = (shift_sum[i] % 26 + (ord(s[i]) - 97)) % 26
            res.append(chr(idx+97))

        return "".join(res)