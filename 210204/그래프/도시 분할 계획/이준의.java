package graph;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Road{
    int from;
    int to;
    int cost;
    public Road(int from, int to, int cost){
        this.from = from;
        this.to = to;
        this.cost = cost;
    }
}

public class 도시분할계획 {

    static int n, m;
    static int[] p;
    static ArrayList<Road> roads = new ArrayList<>();

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a < b){
            p[b] = a;
        } else {
            p[a] = b;
        }
    }

    static int find(int x){
        if(p[x] != x){
            return p[x] = find(p[x]);
        }
        return p[x];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        p = new int[n + 1];
        for(int i = 1; i < n + 1; ++i) p[i] = i;

        for(int i = 0; i < m; ++i){
            int from = sc.nextInt();
            int to = sc.nextInt();
            int cost = sc.nextInt();
            roads.add(new Road(from, to, cost));
        }

        Collections.sort(roads, (a, b) -> {
            return a.cost - b.cost;
        });


        int result = 0;
        int maxCost = 0;
        for(Road road : roads){
            int a = road.from;
            int b =  road.to;
            if(find(a) != find(b)){
                union(a, b);
                if(road.cost > maxCost) maxCost = road.cost;
                result += road.cost;
            }
        }

        System.out.println(result - maxCost);
    }
}
