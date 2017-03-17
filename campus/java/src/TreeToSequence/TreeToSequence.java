package TreeToSequence;

import java.util.*;

class TreeNode {
	int val = 0;
	TreeNode left = null;
	TreeNode right = null;

	public TreeNode(int val) {
		this.val = val;
	}
}

public class TreeToSequence {
	public String toSequence(TreeNode root) {
		// write code here
		String l = "", r = "";
		if (root.left != null)
			l = toSequence(root.left);
		if (root.right != null)
			r = toSequence(root.right);
		return "(" + l + r + ")";
	}
}