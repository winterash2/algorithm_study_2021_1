package dfsbfs2;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 숨바꼭질2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        boolean[] visit = new boolean[100001];

        visit[n] = true;
        Queue<Integer> q = new LinkedList<>();
        q.offer(n);
        int time = 0;
        int count = 0;
        boolean check = false;
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; ++i){
                int cur = q.poll();
                visit[cur] = true;
                if(cur == k){
                    count++;
                    check = true;
                }
                if(cur - 1 >= 0 && !visit[cur - 1]){
                    q.offer(cur - 1);
                }
                if(cur + 1 <= 100000 && !visit[cur + 1]){
                    q.offer(cur + 1);
                }
                if(cur * 2 <= 100000 && !visit[cur * 2]){
                    q.offer(cur * 2);
                }
            }
            if(check){
                break;
            }
            time++;
        }
        System.out.println(time);
        System.out.println(count);
    }
}

/*
5 17

4
2
 */
