package kruskal;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

class Computer{
    int from, to, cost;
    public Computer(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }
}

public class 불우이웃돕기 {

    static int[] p;

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

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] adj = new int[n][n];
        int answer = 0, total = 0;
        ArrayList<Computer> lans = new ArrayList<>();
        for(int i = 0; i < n; ++i){
            String input = br.readLine();
            char[] charArr = input.toCharArray();
            for(int j = 0; j < n; ++j){
                if(Character.isLowerCase(charArr[j])){
                    adj[i][j] = charArr[j] - 'a' + 1;
                    lans.add(new Computer(i, j, adj[i][j]));
                } else if(Character.isDigit(charArr[j])){
                    adj[i][j] = 0;
                } else {
                    adj[i][j] = charArr[j] - 'A' + 27;
                    lans.add(new Computer(i, j, adj[i][j]));
                }
                total += adj[i][j];
            }
        }

        Collections.sort(lans, (a, b) -> {
            return a.cost - b.cost;
        });
        p = new int[n];
        for(int i = 0; i < n; ++i){
            p[i] = i;
        }

        for(Computer Node: lans){
            int cost = Node.cost;
            int a = Node.from;
            int b = Node.to;
            if(find(a) != find(b)){
                union(a, b);
                answer += cost;
            }
        }

        boolean check = true;
        int parent = p[0];
        for(int i = 0; i < n; ++i){
            if(parent != find(i)) check = false;
        }
        if(check){
            System.out.println(total - answer);
        } else {
            System.out.println(-1);
        }

    }
}

/*
3
ABC
DEF
GHI
 */