import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

class A {
static String solve(int n, int m[][]) {
    int t = 0;
    int r = 0;
    int c = 0;
    int i;
    for (i = 0; i < n; i++) {
        t += m[i][i];
        Set<Integer> rs = new HashSet<>();
        Set<Integer> cs = new HashSet<>();
        for (int j = 0; j < n; j++) {
            rs.add(m[i][j]);
            cs.add(m[j][i]);
        }
        if (rs.size() != n) r++;
        if (cs.size() != n) c++;
    }
    return String.format("%d %d %d", t, r, c);
}

public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int i, j, k, n;
    for (i = 1; i <= t; i++) {
        n = sc.nextInt();
        int m[][] = new int[n][n];
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                m[j][k] = sc.nextInt();
            }
        }
        System.out.printf("Case #%d: %s\n", i, solve(n, m));
    }
    
}

}
