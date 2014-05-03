import java.io.FileInputStream;
import java.util.Scanner;

// Minesweeper Master
// https://code.google.com/codejam/contest/2974486/dashboard#s=p2

public class C {

	private static String buildResult(int x1, int y1, int w1, int h1, int x2, int y2, int w2, int h2, int exceptx, int excepty, int R, int C) {
		StringBuffer buff = new StringBuffer("\n");
		for(int row = 0; row < R; row++) {
			for(int col = 0; col < C; col++) {
				if ( (col != exceptx || row != excepty) && 
						((col >= x1 && col < x1 + w1 && row >= y1 && row < y1 + h1) ||
						(col >= x2 && col < x2 + w2 && row >= y2 && row < y2 + h2)) )
					buff.append(row == 0 && col == 0 ? "c" : ".");
				else
					buff.append("*");
			}
			buff.append("\n");
		}
		return new String(buff);
	}

	private static String process(Scanner in) {
		int R = in.nextInt();
		int C = in.nextInt();
		int M = in.nextInt();
		int F = R * C - M;
		int x1 = 0, y1 = 0, x2 = 0, y2 = 0, w1 = 0, h1 = 0, w2 = 0, h2 = 0;
		int exceptx = -1, excepty = -1;
		if ( R == 1 || C == 1 ) {
			w1 = C > R ? F : 1;
						h1 = C > R ? 1 : F;
		}
		else if ( F == 1 ) {
			w1 = 1;
			h1 = 1;
		}
		else if ( F == 2 || F == 3 || F == 5 || F == 7)
			w1 = -1;
		else if ( R == 2 || C == 2 ) {
			w1 = -1;
			if ( F % 2 == 0 ) {
				w1 = R == 2 ? F / 2 : 2;
				h1 = R == 2 ? 2 : F / 2;
			}
		}
		else {
			w1 = F / 2 > C ? C : F / 2;
			h1 = F / w1;
			int remaining = F - w1 * h1;
			if ( remaining > 0 ) {
				x2 = 0;
				y2 = h1;
				if ( remaining > 1 ) {
					w2 = remaining;
					h2 = 1;
				}
				else {
					if ( h1 == 2 ) {
						w1--;
						w2 = 3;
						h2 = 1;
					}
					else {
						exceptx = w1 - 1;
						excepty = h1 - 1;
						w2 = 2;
						h2 = 1;
					}
				}
			}
		}
		//System.out.println(R + "x" + C + ", " + M + " - " + w1 + "x" + h1 + ", " + w2 + "x" + h2);
		if ( w1 < 0 )
			return "\nImpossible\n";
		else 
			return buildResult(x1, y1, w1, h1, x2, y2, w2, h2, exceptx, excepty, R, C);
	}

	public static void main(String[] args) throws Exception {
		Scanner in = new Scanner(System.in.available() > 0 ? System.in : 
			new FileInputStream(Thread.currentThread().getStackTrace()[1].getClassName() + ".practice.in"));
		int T = in.nextInt();
		for(int i = 1; i <= T; i++) 
			System.out.format("Case #%d: %s", i, process(in));
	}
}
