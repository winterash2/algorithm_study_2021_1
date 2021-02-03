package shortestpath2;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

class Node implements Comparable<Node>{
    int to;
    int cost;
    public Node(int to, int cost){
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

public class 숨바꼭질 {
    static int n, m;
    static int[] distance;
    static PriorityQueue<Node> q;
    static ArrayList<ArrayList<Node>> graph;
    static final int INF = (int) 1e9;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        distance = new int[n + 1];
        graph = new ArrayList<ArrayList<Node>>();
        for(int i = 0; i < n + 1; ++i){
            graph.add(new ArrayList<Node>());
        }
        for(int i = 0; i < m; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(new Node(b, 1));
            graph.get(b).add(new Node(a, 1));
        }

        for(int i = 0; i < n + 1; ++i){
            distance[i] = INF;
        }

        distance[1] = 0;
        q = new PriorityQueue<Node>();
        q.offer(new Node(1, 0));
        while(!q.isEmpty()){
            Node cur = q.poll();
            int dist = cur.cost;
            int now = cur.to;
            if(distance[now] < dist) continue;
            for(Node node : graph.get(now)){
                int cost = node.cost + dist;
                if(cost < distance[node.to]){
                    distance[node.to] = cost;
                    q.offer(new Node(node.to, cost));
                }
            }
        }

        int number = 0;
        int count = 0;
        int dist = 0;
        for(int i = 1; i < n + 1; ++i){
            if(distance[i] > dist) {
                number = i;
                dist = distance[i];
            }
        }
        for(int i = 1; i < n + 1; ++i){
            if(dist == distance[i]){
                if(count == 0) number = i;
                count++;
            }
        }

        System.out.println(number + " " + dist + " " + count);
    }
}

/*
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
 */