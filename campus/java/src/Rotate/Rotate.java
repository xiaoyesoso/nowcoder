package Rotate;

public class Rotate {
	public int[][] rotateMatrix(int[][] mat, int n) {
		for (int i = 0; i < n ; ++i) {
			for (int j = 0; j < i; ++j) {
				int tmp = mat[i][j];
				mat[i][j] = mat[j][i];
				mat[j][i] = tmp;
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < (n + 1) / 2; ++j) {
				int tmp = mat[i][j];
				mat[i][j] = mat[i][n - 1 - j];
				mat[i][n - 1 - j] = tmp;
			}
		}
		return mat;
	}
}
