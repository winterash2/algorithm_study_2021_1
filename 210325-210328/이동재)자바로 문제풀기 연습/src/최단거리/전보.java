package 최단거리;

import java.util.*;

public class 전보 {
    public static final int INF = (int) 1e9;
    public static int N;
    public static int M;
    public static int C;

    public static class Path implements Comparable<Path>{
        public int dest;
        public int cost;
        Path(int dest, int cost){
            this.dest = dest;
            this.cost = cost;
        }

        @Override
        public int compareTo(Path o) {
            if(this.cost < o.cost){
                return -1;
            }else{
                return 1;
            }
        }
    }
    public static ArrayList<ArrayList<Path>> graph;

    public static int[] dijkstra(int start){
        int[] arr = new int[N+1];
        for (int i = 0; i < N + 1; i++) {
            arr[i] = INF;
        }
        PriorityQueue<Path> q = new PriorityQueue<>();
        q.add(new Path(start, 0));
        while (!q.isEmpty()) {
            Path cur = q.poll();
            int curPos = cur.dest;
            int curCost = cur.cost;
            if (curCost < arr[curPos]) {
                arr[curPos] = curCost;
                for (Path nxt : graph.get(curPos) ) {
//                    System.out.println(nxt.dest + " " + curCost + nxt.cost);
                    q.add(new Path(nxt.dest, curCost + nxt.cost));
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        C = sc.nextInt();

        graph = new ArrayList<ArrayList<Path>>();
        for(int i=0; i<N+1; i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<M; i++){
            int X = sc.nextInt();
            int Y = sc.nextInt();
            int Z = sc.nextInt();
            graph.get(X).add(new Path(Y, Z));
        }
        int[] Cto = dijkstra(C);
        int count = 0;
        int maxLen = 0;
        for (int i : Cto) {
            if (i != INF) {
                count += 1;
                maxLen = Integer.max(maxLen, i);
            }
        }
        System.out.println(count - 1 + " " + maxLen);
    }
}
/*
3 2 1
1 2 4
1 3 2
 */