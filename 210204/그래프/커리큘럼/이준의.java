package graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 커리큘럼 {

    static int n;
    static int[] in;
    static int[] times;
    static ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        in = new int[n + 1];
        times = new int[n + 1];

        for(int i = 0; i < n + 1; ++i){
            edges.add(new ArrayList<>());
        }

        for(int i = 1; i < n + 1; ++i){
            int time = sc.nextInt();
            times[i] = time;
            int edge;
            while(true){
                edge = sc.nextInt();
                if(edge == -1) break;
                edges.get(edge).add(i);
                in[i]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i < n + 1; ++i){
            if(in[i] == 0) q.offer(i);
        }

        int[] result = times.clone();

        while(!q.isEmpty()){
            int now = q.poll();
            for(Integer i : edges.get(now)){
                // 이부분 이해가 안됨
                result[i] = Math.max(result[i], result[now] + times[i]);
                in[i]--;
                if(in[i] == 0){
                    q.offer(i);
                }
            }
        }

        for(int i = 1; i < n + 1; ++i){
            System.out.println(result[i]);
        }
    }
}

/*
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
 */
