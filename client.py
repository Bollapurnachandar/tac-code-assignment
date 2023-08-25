#importing the function total_good_pair from tacmain 
from tacmain import total_good_pair
#creating a function user to take user input
def user():
    # 1st unit test T to take no of Test cases
    T=int(input(" Enter the Number of Test cases :"))
    for number in range(T):
        # for first line of each test case taking input as length of an array A 
        N=int(input("Enter the length of an array of A :"))
        #checking the condition length of array is greater than1
        if(N>1):
            # second line of each test case input as N space separated integers
            A=list(map(int,input("enter the elements :").split()))
            #map(int,input().split()) applies int to each element in the input 
            # input is taken as space separated values due to split function
            # the elements of a which is stored in list
                # calling a main function to get the value return by the main function
            no_of_good_pairs=total_good_pair(A)
            # displaying the count or the total no of good pairs
            print(" total good pairs are:",no_of_good_pairs)
        else:
            raise Exception("NO pair")
#calling the user function
user()
