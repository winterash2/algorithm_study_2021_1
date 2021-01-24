package sort;

import java.util.PriorityQueue;
import java.util.Scanner;

public class 카드정렬하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < n; ++i){
            pq.add(sc.nextInt());
        }
        if(pq.size() == 1){
            System.out.println("0");
            return;
        }
        int answer = 0;

        // 힙을 사용하는 이유 : 10 20 30 40 50 => 30 + 30 은 60이 되기때문에 60 40 50 에서 40 + 50 을 먼저 수행하는게 효율적이기 때문에 항상 최소 값 2개 뽑아서 더하는게 효율적임
        while(pq.size() > 1){
            int sum = pq.poll() + pq.poll();
            answer += sum;
            pq.add(sum);
        }

        System.out.println(answer);
    }
}
