import java.util.Scanner;

public class WarmupRev {
  
	public static String cold(String t) {
		return t.substring(17) + t.substring(0, 17);
	}
	
	public static String cool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) + 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
		
	public static String warm(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}
	
	public static String hot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		//String s1 = "";
		for (int i = 0; i < t.length(); i++){
			//System.out.println("adj : " + adj[i]);
			//System.out.println("t  : " + t.charAt(i));
			s += (char) (t.charAt(i) + adj[i]);
			//s1 +=  t.charAt(i) + adj[i];
			//System.out.println("s : " + s);
			//System.out.println("s1 : " + s1);
		}
			
		return s;
	}
	
	public static String cold_sol(String t) {
		return t.substring(17) + t.substring(0, 17);
	}
	
	public static String cool_sol(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) - 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
		
	public static String warm_sol(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}
	
	public static String hot_sol(String t) {
		int[] adj = {72, -7, 58, -2, 33, -1, 102, -65, -13, 64, 
				-21, -14, 45, 11, 48, 7, 1, -3, -47, 65, -3, 18, 
				73, -40, 27, 73, 13, 0, 0, 68, -10, -45, -13};
		String s2 = "";
		String s3 = "";
		for (int i = 0; i < t.length(); i++){
			System.out.println("adj1 : " + adj[i]);
			System.out.println("t1  : " + t.charAt(i));
			s2 += (char) (t.charAt(i) + adj[i]);
			s3 +=  t.charAt(i) + adj[i];
			System.out.println("s2 : " + s2);
			System.out.println("s3 : " + s3);
		}
			
		return s2;
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Let's get warmed up! Please enter the flag: ");
		String flag = in.nextLine();
		String encode = "";
		String match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy";
		if (flag.length() == 33 && hot(warm(cool(cold(flag)))).equals(match))
			System.out.println("You got it!");
		else
			encode = hot(warm(cool(cold(flag))));
			System.out.println("That's not correct, please try again!! " + encode);
		in.close();

		String ans = "";
		ans = cold_sol(cool_sol(warm_sol(hot_sol(match))));
		System.out.println("ans : " + ans );
	}
  
}
