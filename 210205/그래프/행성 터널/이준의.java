package graph2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Tunnel{
    int from, to, cost;
    public Tunnel(int from, int to, int cost){
        this.from = from;
        this.to = to;
        this.cost = cost;
    }
}

class Node{
    int index;
    int loc;
    public Node(int index, int loc){
        this.index = index;
        this.loc = loc;
    }
}

public class 행성터널 {
    static int n;
    static int[] p;
    static ArrayList<Node> x = new ArrayList<>();
    static ArrayList<Node> y = new ArrayList<>();
    static ArrayList<Node> z = new ArrayList<>();
    static ArrayList<Tunnel> edges = new ArrayList<>();

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
        p = new int[n + 1];
        for(int i = 0; i < n + 1; ++i){
            p[i] = i;
        }

        for(int i = 1; i < n + 1; ++i){
            x.add(new Node(i, sc.nextInt()));
            y.add(new Node(i, sc.nextInt()));
            z.add(new Node(i, sc.nextInt()));
        }
        Collections.sort(x, (a, b) -> { return a.loc - b.loc; });
        Collections.sort(y, (a, b) -> { return a.loc - b.loc; });
        Collections.sort(z, (a, b) -> { return a.loc - b.loc; });
        for(int i = 0; i < n - 1; ++i){
            edges.add(new Tunnel(x.get(i).index, x.get(i + 1).index, Math.abs(x.get(i).loc - x.get(i + 1).loc)));
            edges.add(new Tunnel(y.get(i).index, y.get(i + 1).index, Math.abs(y.get(i).loc - y.get(i + 1).loc)));
            edges.add(new Tunnel(z.get(i).index, z.get(i + 1).index, Math.abs(z.get(i).loc - z.get(i + 1).loc)));
        }

        Collections.sort(edges, (a, b) -> { return a.cost - b.cost; });
//        for(int i = 0; i < edges.size(); ++i){
//            System.out.println(edges.get(i).from + " " + edges.get(i).to + " " + edges.get(i).cost);
//        }
        int answer = 0;
        for(int i = 0 ; i < edges.size(); ++i){
            int a = edges.get(i).from;
            int b = edges.get(i).to;
            int cost = edges.get(i).cost;
            if(find(a) != find(b)){
                union(a, b);
                answer += cost;
            }
        }
        System.out.println(answer);
    }
}
/*
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
 */