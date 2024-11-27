def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp array from bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of LCS is dp[m][n]
    lcs_length = dp[m][n]
    
    # Create a list to store the LCS characters
    lcs = []
    
    # Start from the bottom-right corner and backtrack to find the LCS
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()  # The LCS is constructed backwards, so reverse it
    
    return lcs_length, ''.join(lcs)

# Example usage
if __name__ == "__main__":
    X = "cloud"
    Y = "loud"
    
    lcs_length, lcs_sequence = longest_common_subsequence(X, Y)
    print(f"Length of LCS: {lcs_length}")
    print(f"LCS: {lcs_sequence}")


    
def test_no_common_subsequence():
    assert longest_common_subsequence("ABC", "DEF") == 0, "Failed on strings with no common subsequence"


def test_real_world_case():
    assert longest_common_subsequence("dynamicprogramming", "machinelearning") == 6, "Failed on real-world case"

