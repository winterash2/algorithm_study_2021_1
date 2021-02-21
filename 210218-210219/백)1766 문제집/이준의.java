package topologysort;

import java.util.*;

public class 문제집 {
    public static void main(String[] args) {
        int v, e;
        Scanner sc = new Scanner(System.in);
        v = sc.nextInt();
        e = sc.nextInt();
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < v + 1; ++i){
            graph.add(new ArrayList<Integer>());
        }
        int[] indegree = new int[v + 1];
        for(int i = 0; i < e; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
            indegree[b] += 1;
        }

        ArrayList<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> q = new PriorityQueue<>();

        for(int i = 1; i < v + 1; ++i){
            if(indegree[i] == 0){
                q.offer(i);
            }
        }

        while(!q.isEmpty()){
            int now = q.poll();
            result.add(now);
            for(Integer i : graph.get(now)){
                indegree[i] -= 1;
                if(indegree[i] == 0){
                    q.offer(i);
                }
            }
        }

        for(Integer i : result){
            System.out.print(i + " ");
        }
    }
}
