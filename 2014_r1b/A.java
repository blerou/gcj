import java.io.FileInputStream;
import java.util.Scanner;

public class A {

	private static int getc(String s, char c) {
		int res = 0;
		for(int i = 0; i < s.length() && s.charAt(i) == c; i++)
			res++;
		return res;
	}
	
	private static String process(Scanner in) {
		int N = in.nextInt();
		String[] items = new String[N];
		for(int i = 0; i < N; i++)
			items[i] = in.next();
		int res = 0;
		while ( items[0].length() > 0 ) {
			char c = items[0].charAt(0);
			int[] cnt = new int[N];
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;
			for(int i = 0; i < N; i++) {
				cnt[i] = getc(items[i], c);
				if ( cnt[i] == 0 )
					return "Fegla Won";
				if ( cnt[i] > max )
					max = cnt[i];
				if ( cnt[i] < min )
					min = cnt[i];
				items[i] = items[i].substring(cnt[i]);
			}
			int best = Integer.MAX_VALUE;
			for(int len = min; len <= max; len++) {
				int steps = 0;
				for(int i = 0; i < N; i++) 
					steps += Math.abs(cnt[i] - len);
				if ( steps < best )
					best = steps;
			}
			res += best;
		}
		for(int i = 0; i < N; i++) 
			if ( items[i].length() > 0 )
				return "Fegla Won";
		return Integer.toString(res);
	}

	public static void main(String[] args) throws Exception {
		Scanner in = new Scanner(System.in.available() > 0 ? System.in : 
			new FileInputStream(Thread.currentThread().getStackTrace()[1].getClassName() + ".practice.in"));
		int T = in.nextInt();
		for(int i = 1; i <= T; i++) 
			System.out.format("Case #%d: %s\n", i, process(in));
	}
}
