class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        x= salary.remove(min(salary))
        y=salary.remove(max(salary))
        den=len(salary)
        total=0
        for i in range(len(salary)):
            total+=salary[i]
        return (float(total))/(den)


      
      