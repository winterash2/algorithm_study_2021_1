package shortestpath;

import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

class City implements Comparable<City>{
    int to;
    int cost;
    public City(int to, int cost){
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(City o) {
        return this.cost - o.cost;
    }
}

public class 전보 {

    static final int INF = (int) 1e9;
    static int n, m, c;
    static int[] distance;
    static ArrayList<ArrayList<City>> graph;
    static PriorityQueue<City> q;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        c = sc.nextInt();
        distance = new int[n + 1];
        graph = new ArrayList<>();
        for(int i = 0; i < n + 1; ++i){
            distance[i] = INF;
        }
        for(int i = 0; i < n + 1; ++i){
            graph.add(new ArrayList<City>());
        }
        for(int i = 0; i < m; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            graph.get(a).add(new City(b, c));
        }

        q = new PriorityQueue<City>();
        distance[c] = 0;
        q.offer(new City(c, 0));
        while(!q.isEmpty()){
            City city = q.poll();
            int dist = city.cost;
            int now = city.to;
            if(distance[now] < dist){
                continue;
            }
            for(City node : graph.get(now)){
                int cost = dist + node.cost;
                if(cost < distance[node.to]){
                    distance[node.to] = cost;
                    q.offer(new City(node.to, cost));
                }
            }
        }

        int count = 0;
        int maxVal = 0;
        for(int i = 1; i < n + 1; ++i){
            if(distance[i] != INF){
                count += 1;
                maxVal = Math.max(maxVal, distance[i]);
            }
        }

        System.out.println(count - 1 + " " + maxVal);
    }
}
