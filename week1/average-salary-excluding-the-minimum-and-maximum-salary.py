class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        salaryAV = salary[1:-1]

        av = sum(salaryAV)/len(salaryAV)
        return av