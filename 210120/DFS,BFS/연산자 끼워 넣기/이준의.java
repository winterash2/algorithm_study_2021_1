package dfsbfs;

import java.util.Scanner;

public class 연산자끼워넣기 {

    private static int n;
    private static int[] numbers;
    private static int sum, minus, multi, div;
    private static int minVal = (int)1e9 , maxVal = -(int)1e9;

    public static void dfs(int cnt, int total){
        if(cnt == n - 1){
            if(total > maxVal) maxVal = total;
            if(total < minVal) minVal = total;
            return;
        }
        if(sum > 0){
            sum--;
            dfs(cnt + 1, total + numbers[cnt + 1]);
            sum++;
        }
        if(minus > 0){
            minus--;
            dfs(cnt + 1, total - numbers[cnt + 1]);
            minus++;
        }
        if(multi > 0){
            multi--;
            dfs(cnt + 1, total * numbers[cnt + 1]);
            multi++;
        }
        if(div > 0){
            div--;
            int param = total == 0 ? 0 : (int) total / numbers[cnt + 1];
            dfs(cnt + 1, param);
            div++;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        numbers = new int[n];
        for(int i = 0; i < n; ++i){
            numbers[i] = sc.nextInt();
        }
        sum = sc.nextInt();
        minus = sc.nextInt();
        multi = sc.nextInt();
        div = sc.nextInt();

        dfs(0, numbers[0]);

        System.out.println(maxVal);
        System.out.println(minVal);
    }
}
