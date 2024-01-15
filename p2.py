 def missingNumber(self,array,n):
        total = (n + 1)*(n)//2  # calculate the sum of all numbers from 1 to n+1 using arithmetic progression formula
        sum_of_A = sum(array)  # calculate the sum of all numbers in the array
        return total - sum_of_A  # return the difference between the total sum and the sum of the array to get the missing number
