package 그래프;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 도시분할계획 {
    public static int N;
    public static int M;

    public static class Path implements Comparable<Path>{
        int a;
        int b;
        int cost;

        Path(int a, int b, int cost){
            this.a = a;
            this.b = b;
            this.cost = cost;
        }

        @Override
        public int compareTo(Path o) {
            if(this.cost <= o.cost){
                return -1;
            }
            else{
                return 1;
            }
        }
    }

    public static int find(int[] parent, int x){
        if(parent[x] != x){
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
    public static void union(int[] parent, int a, int b) {
        a = find(parent, a);
        b = find(parent, b);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        int[] parent = new int[N+1];
        for (int i = 0; i < N + 1; i++) {
            parent[i] = i;
        }

        PriorityQueue<Path> q = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int C = sc.nextInt();
            q.add(new Path(A, B, C));
        }

        ArrayList<Integer> costs = new ArrayList<>();
        while (!q.isEmpty()) {
            Path path = q.poll();
            int a = path.a;
            int b = path.b;
            int cost = path.cost;
            if (find(parent, a) != find(parent, b)) {
                union(parent, a, b);
                costs.add(cost);
            }
        }

        int answer = 0;
        int past = 0;
        for (int cost : costs) {
            answer += past;
            past = cost;
        }
        System.out.println(answer);
    }
}
/*
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
 */