package adhoc;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

class 트리의부모찾기{

    static boolean[] visit;
    static int[] p;
    static ArrayList<ArrayList<Integer>> graph;
    public static void dfs(int x){
        visit[x] = true;
        for(Integer child : graph.get(x)){
            if(!visit[child]){
                p[child] = x;
                dfs(child);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        visit = new boolean[N + 1];
        p = new int[N + 1];
        graph = new ArrayList<>();
        for(int i = 0; i < N + 1; ++i) graph.add(new ArrayList<>());
        for(int i = 0; i < N - 1; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        dfs(1);
        for(int i = 2; i <= N; ++i){
            bw.write(p[i] + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
7
1 6
6 3
3 5
4 1
2 4
4 7
 */