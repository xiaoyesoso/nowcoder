package countBitDiff;

public class Solution {
	/**
	 * 获得两个整形二进制表达位数不同的数量
	 * 
	 * @param m
	 *            整数m
	 * @param n
	 *            整数n
	 * @return 整型
	 */
	public int countBitDiff(int m, int n) {
		int diff = m ^ n;
		int cnt = 0;
		while (diff > 0) {
			if ((diff & 1) == 1)
				++cnt;
			diff >>= 1;
		}
		return cnt;
	}
}