import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class b {
		public static void main(String[] args) {
			readAndSolve(args[0], args[0]+".out");
		}

		/**
		 * @param inputName
		 * @param outputName
		 */
		private static void readAndSolve(String inputName, String outputName) {
			BufferedReader input = null;
			BufferedWriter output = null;
			Date d1 = new Date();
			try {
				input = new BufferedReader(new FileReader(inputName));
				output = new BufferedWriter(new FileWriter(outputName));
				String line1 = null;
				String line2 = null;
				String line3 = null;
				int expectedCases = 0;
				int actualCase = -1;
				line1=input.readLine();
				expectedCases = Integer.parseInt(line1);
				for (actualCase = 1; actualCase<=expectedCases; actualCase++) {
					line2 = input.readLine();
					line3 = input.readLine();
					String result = solve(line2, line3);
					output.write("Case #" + actualCase +": " + result + "\n");				
					System.out.println("Case #" + actualCase +": " + result );				
				}
				input.close();
				output.close();
			} catch (Exception e) {
				e.printStackTrace();
			} finally {
				
			}
		}

		private static String solve(String line2, String line3) {
			String[] trains = line3.split(" ");
			int allLeters = findAllLeters(line3);
//			System.out.println(line3 + " size: " + allLeters);
			List<String> trainList = new ArrayList<String>();
			trainList.addAll( Arrays.asList(trains));			
			List<String> actOrder = new ArrayList<String>();
			long result = permute(allLeters, trainList, actOrder, 0);
			return Long.toString(result);
		}

		private static long permute(int allLeters, List<String> trainList, List<String> actOrder, long i) {
			if (trainList.size() == 0) {
				long actLetters = getLetters(actOrder);
				if (actLetters == allLeters) {
					return i+1;
				}
			}
			long result = i;
//			String lastTrain = actOrder.size() == 0 ? null : actOrder.get(actOrder.size()-1);
			for (int j = 0; j < trainList.size(); j++) {
				String actTrain = trainList.get(j);
				trainList.remove(j);
				actOrder.add(actTrain);
				result = permute(allLeters, trainList, actOrder, result);
				actOrder.remove(actOrder.size()-1);
				trainList.add(j, actTrain);
			}
			return result;
		}

		private static long getLetters(List<String> actOrder) {
			if (actOrder.size() == 0) {
				return 0;
			}
			long result = 0;
			Character actChar = null;
			for (int i = 0; i < actOrder.size(); i++) {
				String train = actOrder.get(i);
				for (int j = 0; j<train.length(); j++) {
					if (actChar == null || !actChar.equals(train.charAt(j))) {
						result++;
						actChar = train.charAt(j);
					}
				}
			}
			return result;
		}

		private static int findAllLeters(String line3) {
			Set<Character> letters = new HashSet<Character>();
			for (int i = 0; i < line3.length(); i++) {
				letters.add(line3.charAt(i));
			}
			letters.remove(" ".charAt(0));
			return letters.size();
		}

}
