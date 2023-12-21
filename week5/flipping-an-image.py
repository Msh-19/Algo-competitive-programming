class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        column = len(image)
        output = []
        for r in range(row):
            output.append(image[r])
            output[r].reverse()
        
        
        for r in range(len(output)):
            for c in range(len(output[0])):
                output[r][c]^= 1
        return output
