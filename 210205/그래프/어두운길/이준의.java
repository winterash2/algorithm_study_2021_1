package graph2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Road{
    int from, to, cost;
    public Road(int from, int to, int cost){
        this.from = from;
        this.to = to;
        this.cost = cost;
    }
}

public class 어두운길 {

    static int n, m;
    static int[] p;
    static ArrayList<Road> edges = new ArrayList<>();

    static int find(int x){
        if(x != p[x]){
            return p[x] = find(p[x]);
        }
        return p[x];
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a < b){
            p[b] = a;
        } else {
            p[a] = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        p = new int[n + 1];
        for(int i = 0; i < n + 1; ++i){
            p[i] = i;
        }
        int sum = 0;
        for(int i = 0; i < m; ++i){
            int from = sc.nextInt();
            int to = sc.nextInt();
            int cost = sc.nextInt();
            sum += cost;
            edges.add(new Road(from, to, cost));
        }

        Collections.sort(edges, (a, b) -> {
            return a.cost - b.cost;
        });

        int sum2 = 0;

        for(Road road : edges){
            int from = road.from;
            int to = road.to;
            int cost = road.cost;
            if(find(from) != find(to)){
                union(from, to);
                sum2 += cost;
            }
        }
        System.out.println(sum - sum2);
    }
}

/*
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
 */