import java.util.ArrayList;
import java.util.PriorityQueue;

class Node implements Comparable<Node>{
    int to, cost;
    public Node(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}


class Solution {
    static final int INF = (int) 1e9;
    static int[] distance;
    static PriorityQueue<Node> pq = new PriorityQueue<>();
    static ArrayList<ArrayList<Node>> edges = new ArrayList<>();
    public static int solution(int n, int[][] edge){
        int answer = 0;
        distance = new int[n + 1];
        for(int i = 0 ; i < n + 1; ++i){
            distance[i] = INF;
        }
        for(int i = 0 ; i < n + 1; ++i){
            edges.add(new ArrayList<>());
        }

        for(int i = 0; i < edge.length; ++i){
            int from = edge[i][0];
            int to = edge[i][1];
            edges.get(from).add(new Node(to, 1));
            edges.get(to).add(new Node(from, 1));
        }

        distance[1] = 0;
        pq.offer(new Node(1, 0));
        while(!pq.isEmpty()){
            Node cur = pq.poll();
            if(distance[cur.to] < cur.cost) continue;
            for(Node next : edges.get(cur.to)){
                int cost = cur.cost + next.cost;
                if(cost < distance[next.to]){
                    distance[next.to] = cost;
                    pq.offer(new Node(next.to, cost));
                }
            }
        }
        int max = 0;
        for(int i = 1; i < n + 1; ++i){
            if(max < distance[i]) max = distance[i];
        }
        for(int i = 1; i < n + 1; ++i){
            if(max == distance[i]) answer++;
        }
        return answer;
    }
}

/*
정확성  테스트
테스트 1 〉	통과 (0.30ms, 52.3MB)
테스트 2 〉	통과 (0.37ms, 53.1MB)
테스트 3 〉	통과 (0.47ms, 52.1MB)
테스트 4 〉	통과 (1.93ms, 51.8MB)
테스트 5 〉	통과 (4.53ms, 54.4MB)
테스트 6 〉	통과 (14.09ms, 59.6MB)
테스트 7 〉	통과 (47.05ms, 76.8MB)
테스트 8 〉	통과 (41.98ms, 74.7MB)
테스트 9 〉	통과 (48.01ms, 78.3MB)
 */