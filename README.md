# highest-value-common-subsequence
Aarush Tripathi
Uf id: 86149341

Description:
This program solves the highest value longest common subsequence problem using an optimal dynamic programming solution.
Given two strings A and B, and a value assigned to each character in the alphabet, it outputs:
1. the maximum value of a common subsequence of A and B
2. one optimal subsequence for the value

Instructions to run:
For particular files:
1. go to the hvlcs folder directory (../highest-value-common-subsequence/hvlcs)
2. run the hvlcs_sol.py file and give the particular input file name you want to use. For example, for the input_1.txt file run the command:
python hvlcs_sol.py ../test_files/input_1.txt
3. output should be value and a subsequence printed over 2 lines

For multiple files (generates graph as well):
1. make sure all the input files you want to use are in test_files folder
2. go to main directory (../highest-value-common-subsequence)
3. run the command: python hvlcs/generate_graph.py
4. should pop up a graph and also print file name, value, and subsequence over 3 lines


Assumptions:
Input format follows what was give exactly
Alphabet is unique characters
A and B use characters that are in the alphabet
The input can fit into memory of m*n where m and n are lengths of strings A and B respectively

Questions:
1. The graph is given in runtime_graph.jpg which shows runtime of 10 input files

2. Recurrance
OPT(i,j) = max value of a common subsequence of A[1,..,i] and B[1,..,j]
Recurrance / Base Cases:
If either string is empty, no common subseqeunce so
    OPT(i,0) = 0 for all i
    OPT(0,j) = 0 for all j
If A[i] != B[j] then last chars cant both be in the same subsequence so we pick highest of either
    OPT(i,j) = max(OPT(i-1, j), OPT(i,j-1))
If A[i] == B[j], then we either skip one of the chars (incase total is lower than what we had) or include the match
    OPT(i, j) = max(OPT(i-1, j), OPT(i, j-1), OPT(i-1, j-1) + v(A[i]))
v(c) is value assigned to char c

Correct:
This recurrence works because each sub problem takes all the possible solutions into consideration. Every sol has to fit one of the cases where A[i]==B[j] or not and if it is then we choose whether to skip one side or use the previous value of both plus current value. Since the optimal is true in each case, we can use recurrance to compute all global optimal.

3.
func hvlcs(A,B,v)
    n, m = length of A, length of B
    initialize matrix dp[0,..,n][0,..,m]
    for i=0 to n
        dp[i][0] = 0
    for j=0 to m
        dp[0][j] = 0
    for i=1 to n
        for j=1 to m
            if A[i] = B[j]
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+v(B[j]))
            else if not equal
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]
The agoirthm runs in O(mn) time where m and n are the lengths of the strings that are given. This is because we iterate through a nested loop of length n+1 and m+1 which means (n+1)(m+1) computations dissolving to O(nm). Space is O(mn) too bc the dp matrix is size (n+1)*(m+1) which also simplifies to O(mn).