**Problem Statement:**
given an array A of length N. 
**-->**A pair (i, j) is said to be good if gcd (A_i, A_j) = lcm(A_i, A_j). Find the total number of good pairs present in the given array.
**input conditions:**
**-->**The ﬁrst line of input will contain a single integer T, denoting the number of test cases
**-->**The ﬁrst line of each test case contains an integer N - the length of the array A.
**-->**The second line of each test case contains N space-separated integers.<br/>
**Note:-**<br/>
**execute the client.py file <br/>client.py and tacmain.py should be in same folder**<br/>

**Approach:-**
s<br/> in **client.py**
 T  is user input for number of test cases<br/>
 in loop take N as input for length of an array<br/>
 if length of array is <1 raise an Exception that "No Pair"<br/>
 enter elements as space separated integers into A by user input<br/>
 call the main function which consists return total no of good pair count print the total good pair count<br/>
  in **tacmain.py**<br/>
create a function for gcd of two numbers<br/>
create a function for lcm of two numbers<br/>
create a mian function which contains condition to become a good pair<br/>
increase the good_pair_count by 1 and return the value
 
