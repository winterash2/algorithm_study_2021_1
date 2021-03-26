package shortestpath;

import java.util.*;
import java.io.*;

public class 복습_전보 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for(int i = 0; i < n + 1; ++i) graph.add(new ArrayList<>());
        for(int i = 0; i < e; ++i){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph.get(from).add(new Node(to, cost));
        }

        PriorityQueue<Node> heapq = new PriorityQueue<>((a, b) ->{
            if(a.cost == b.cost){
                return a.to - b.to;
            } else return a.cost - b.cost;
        });

        int[] distance = new int[n + 1];
        for(int i = 0; i < n + 1; ++i) distance[i] = Integer.MAX_VALUE;
        heapq.offer(new Node(start, 0));
        while(!heapq.isEmpty()){
            Node cur = heapq.poll();
            if(distance[cur.to] < cur.cost){
                continue;
            }
            for(Node next : graph.get(cur.to)){
                int cost = cur.cost + next.cost;
                if(distance[next.to] > cost){
                    distance[next.to] = cost;
                    heapq.offer(new Node(next.to, cost));
                }
            }
        }
        int max = Integer.MIN_VALUE;
        int cnt = 0;
        for(int i = 1; i < n + 1; ++i){
            if(i == start) continue;
            if(distance[i] != (int) 1e9){
                if(distance[i] > max) max = distance[i];
                cnt++;
            }
        }
        bw.write(cnt + " " + max + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
3 2 1
1 2 4
1 3 2
 */

