package StringPattern;

import java.util.*;

public class StringPattern {
	public int findAppearance(String A, int lena, String B, int lenb) {
		// write code here
		int i = 0;
		while (i < lena) {
			if (A.charAt(i) == B.charAt(0)) {
				int j = 0;
				while (i < lena && j < lenb && A.charAt(i) == B.charAt(j)) {
					++j;
					++i;
				}
				if (j == lenb)
					return i - lenb;
			} else
				++i;
		}
		return -1;
	}
}
