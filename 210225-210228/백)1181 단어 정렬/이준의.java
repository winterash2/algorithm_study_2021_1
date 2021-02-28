import java.util.*;

public class Main {
    public static void main(String[] args){
        solve();
    }
    public static void solve(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] input = new String[n];

        for(int i = 0; i < n; ++i){
            input[i] = sc.nextLine();
        }

        Arrays.sort(input, (o1, o2) -> {
            return o1.length() == o2.length() ? o1.compareTo(o2) : o1.length() - o2.length();
        });

        System.out.println(input[0]);
        for(int i = 1; i < input.length; ++i){
            if(!input[i].equals(input[i - 1])){
                System.out.println(input[i]);
            }
        }
    }
}