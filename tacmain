''' first of al we need to get input an array A of length N Aim to count the total no of goood pairs  present in the array
 a good pair need to satisfy if gcd(A[i],A[j])==lcm(A[i],A[j]) '''
''' first we need to create a two functions to get gcd(Greatest common divisor) and LCM(least common multiple) of two numbers'''
import math
#function creation to get gcd value
def get_gcd_value(num1,num2):
    #ex:- gcd(2,0) is 2
    if(num2==0):
        return abs(num1)
    else:
        return(get_gcd_value(num2,num1%num2))#gcd=a*b/LCM(a,b)
    
#function creation to get lcm value
def get_lcm_value(num1,num2):
    #lcm=a*b/gcd(a,b)
    return num1*num2//get_gcd_value(num1,num2)
    #we can also get gcd and lcm values using math.gcd(num1,num2) and lcm=(num1*num2)//math.gcd(num1,num2)

#creating a function to check total no of good pair count
def total_good_pair(array):
    #initialisation of good_pair_count to count good_pairs
    good_pair_count=0
    #length of array is same as N
    size=len(array)
    #for loop to iterate over an array 
    for first in range(size):
        #for loop to iterate from first+1 index to end of the array
        for second in range(first+1,size):
            # main condition to satisfy to be a good pair
            if(get_gcd_value(array[first],array[second])==get_lcm_value(array[first],array[second])):
                #increasing good_pair_count by 1
                good_pair_count=good_pair_count+1
    return good_pair_count





