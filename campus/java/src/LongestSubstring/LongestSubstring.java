package LongestSubstring;

public class LongestSubstring {
	public int findLongest(String A, int n, String B, int m) {
		int[][] DP = new int[n + 1][m + 1];
		DP[0][0] = 0;
		int max = -1;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				if (A.charAt(i - 1) == B.charAt(j - 1)) {
					DP[i][j] = DP[i - 1][j - 1] + 1;
					if (DP[i][j] > max)
						max = DP[i][j];
				} else {
					DP[i][j] = 0;
				}
			}
		}
		return max;
	}
}