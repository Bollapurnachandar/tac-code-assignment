''' first of al we need to get input an array A of length N Aim to count the total no of goood pairs  present in the array
 a good pair need to satisfy if gcd(A[i],A[j])==lcm(A[i],A[j]) '''
''' first we need to create a two functions to get gcd(Greatest common divisor) and LCM(least common multiple) of two numbers'''
import math
def get_gcd_value(num1,num2):#function creation to get gcd value
    if(num2==0):#ex:- gcd(2,0) is 2
        return abs(num1)
    else:
        return(get_gcd_value(num2,num1%num2))#gcd=a*b/LCM(a,b)
def get_lcm_value(num1,num2):#function creation to get lcm value
    return num1*num2//get_gcd_value(num1,num2)#lcm=a*b/gcd(a,b)
#we can also get gcd and lcm values using math.gcd(num1,num2) and lcm=(num1*num2)//math.gcd(num1,num2)

def total_good_pair(array):#creating a function to check total no of good pair count
    good_pair_count=0#initialisation of good_pair_count to count good_pairs
    size=len(array)#length of array is same as N
    for first in range(size):#for loop to iterate over an array 
        for second in range(first+1,size):#for loop to iterate from first+1 index to end of the array
            # main condition to satisfy to be a good pair
            if(get_gcd_value(array[first],array[second])==get_lcm_value(array[first],array[second])):
                good_pair_count=good_pair_count+1#increasing good_pair_count by 1
    return good_pair_count
T=int(input(" Enter the Number of Test cases :"))# 1st unit test T to take no of Test cases
for number in range(T):
    N=int(input("Enter the length of an array of A :"))# for first line of each test case taking input as length of an array A 
    A=list(map(int,input("enter the elements :").split()))# second line of each test case input as N space separated integers
    #map(int,input().split()) applies int to each element in the input 
    # input is taken as space separated values due to split function
    # the elements of a which is stored in list
    no_of_good_pairs=total_good_pair(A)# calling a main function to get the value return by the main function
    print(" total good pairs are:",no_of_good_pairs)# displaying the count or the total no of good pairs

