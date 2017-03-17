package LCS;

import java.util.*;

public class LCS {
	public int findLCS(String A, int n, String B, int m) {
        int[][] DP = new int[n+1][m+1];
        DP[0][0] = 0;
        for(int i = 1; i <= n ; ++i){
        	for(int j = 1 ; j <= m ;++j){
        		if(A.charAt(i-1) == B.charAt(j-1)) DP[i][j] = DP[i-1][j-1]+1;
        		else DP[i][j] = DP[i-1][j] > DP[i][j-1] ? DP[i-1][j] :DP[i][j-1];
        	}
        }
        return DP[n][m];
    }
}
