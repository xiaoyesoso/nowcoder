package WildMatch;

public class WildMatch {
	public boolean chkWildMatch(String A, int lena, String B, int lenb) {
		boolean[][] b = new boolean[lena + 1][lenb + 1];
		b[0][0] = true;
		for (int i = 1; i <= lena; ++i) {
			for (int j = 1; j <= lenb; ++j) {
				if (B.charAt(j - 1) == '*') {
					b[i][j] = b[i][j - 1] || b[i - 1][j];
				} else if (B.charAt(j - 1) == '.') {
					b[i][j] = b[i - 1][j - 1];
				} else {
					b[i][j] = b[i - 1][j - 1]
							&& A.charAt(i - 1) == B.charAt(j - 1);
				}
			}
		}
		return b[lena][lenb];
	}
}
