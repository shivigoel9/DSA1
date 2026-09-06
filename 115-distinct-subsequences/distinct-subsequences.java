class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        
        // dp[i][j] = number of distinct subsequences of s[0..i-1] that equals t[0..j-1]
        int[][] dp = new int[m + 1][n + 1];
        
        // An empty t can always be formed from any prefix of s
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    // Use current char or skip it
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // Skip current char
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
}
