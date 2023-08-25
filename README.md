**Problem Statement:**
given an array A of length N. 
**-->**A pair (i, j) is said to be good if gcd (A_i, A_j) = lcm(A_i, A_j). Find the total number of good pairs present in the given array.
**input conditions:**
**-->**The ﬁrst line of input will contain a single integer T, denoting the number of test cases
**-->**The ﬁrst line of each test case contains an integer N - the length of the array A.
**-->**The second line of each test case contains N space-separated integers.

i used python programming approach to solve this problem approach
 I creatted a function to get gcd of 2 numbers and another function to get lcm of two numbers
 main function to check gcd==lcm if satisfies the condition  increased the count value by 1 and return thr count value
 i followed unit test cases input conditions first T will be taken as input for number of test cases
 next in the loop for every test case in first i  have taken input N as the length of an aray
 in the second line of every test case input in the form space separated integers as input
 and calling the main function to get checked whether gcd=lcm and printing the count valiue
 
