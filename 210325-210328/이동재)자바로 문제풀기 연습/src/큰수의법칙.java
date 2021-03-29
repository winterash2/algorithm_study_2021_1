import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 큰수의법칙 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        int[] numbers = new int[N];
        for(int i = 0; i < N; i++){
            numbers[i] = sc.nextInt();
        }
        Arrays.sort(numbers);
//        for(int i = 0; i < N; i++){
//            System.out.print(numbers[i] + " ");
//        }
        int first = numbers[N - 1];
        int second = numbers[N - 2];

        int cnt = (M / (K + 1)) * K;
        cnt += M % (K + 1);

        int result = 0;
        result += cnt * first;
        result += (M - cnt) * second;

        System.out.println(result);
    }
}
/*
5 8 3
2 4 5 4 6
 */