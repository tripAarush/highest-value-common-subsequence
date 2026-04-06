import sys

# getting the values from the input format
def read_input_file(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        ch, val = lines[i].split()
        values[ch] = int(val)

    a = lines[k + 1]
    b = lines[k + 2]

    return values, a, b

# actual dp solution, we take a 2 by 2 matrix which shows max value for i chars of a and j chars of b
# by the end of the matrix, dp[len(a)][len(b)] gives max value
# we can remake the subsequence by backtracking through the matrix
def solve_hvlcs(values, a, b):
    n = len(a)
    m = len(b)
    # initialize
    dp = [[0 for _ in range(m+1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # if the chars matchs, we have keep max of the cur value and val of char+prev
            if a[i - 1] == b[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + values[a[i - 1]])

    # Remaking
    i, j, subs = n, m, []

    while i > 0 and j > 0:
        # first seeing if we the val is from the matching diagonal chars
        if (a[i - 1] == b[j - 1] and dp[i][j]==dp[i - 1][j - 1] + values[a[i - 1]]):
            subs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    # since we started from back need to reverse
    subs.reverse()
    return (dp[n][m], "".join(subs))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hvlcs.py <input_file>")
        sys.exit()

    input_file = sys.argv[1]
    values, a, b = read_input_file(input_file)
    max_value, subseq = solve_hvlcs(values, a, b)

    print(max_value)
    print(subseq)