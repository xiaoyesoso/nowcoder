package MaxGap;

import java.util.*;

public class MaxGap {
	public int findMaxGap(int[] A, int n) {
		// write code here
		int[] B = new int[n];
		int lMax = A[0], rMax = A[n - 1], result = 0;
		for (int i = n - 1; i >= 0; --i) {
			if (A[i] > rMax)
				rMax = A[i];
			B[i] = rMax;
		}
		for (int i = 0; i < n - 1; ++i) {
			if (A[i] > lMax)
				lMax = A[i];
			int Abs = Math.abs(lMax - B[i + 1]);
			if (Abs > result)
				result = Abs;
		}
		return result;
	}
}