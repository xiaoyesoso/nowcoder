package MonoSum;

public class MonoSum {
	public static int merge(int[] A, int bg, int mid, int ed) {
		int i = bg, j = mid + 1, p = bg;
		int[] B = new int[A.length];
		int sum = 0;
		while (i <= mid && j <= ed) {
			if (A[i] <= A[j]) {
				sum += A[i] * (ed - j + 1);
				B[p++] = A[i++];
			} else {
				B[p++] = A[j++];
			}
		}
		while (j <= ed)
			B[p++] = A[j++];
		while (i <= mid)
			B[p++] = A[i++];
		for (int k = bg; k < p; ++k) {
			A[k] = B[k];
		}
		return sum;
	}

	public static int mergeSort(int[] A, int bg, int ed) {
		int result = 0;
		if (bg >= ed)
			return result;
		int mid = bg + (ed - bg) / 2;
		result += mergeSort(A, bg, mid);
		result += mergeSort(A, mid + 1, ed);
		return result + merge(A, bg, mid, ed);
	}

	public int calcMonoSum(int[] A, int n) {
		return mergeSort(A, 0, n - 1);
	}
}