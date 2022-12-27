class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # time complexity O(n) 
        # space complexity O(1)
        min_salary= salary.remove(min(salary))
        max_salary=salary.remove(max(salary))
        den=len(salary)
        total=0
        
        for i in range(len(salary)):
            total+=salary[i]
        return (float(total))/(den)


      
      