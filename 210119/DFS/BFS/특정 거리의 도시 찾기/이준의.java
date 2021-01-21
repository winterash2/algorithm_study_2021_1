package dfsbfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class 특정거리의도시찾기 {
    private static ArrayList<ArrayList<Integer>> list = new ArrayList<>();
    public static int n = 0;
    public static int m = 0;
    public static int k = 0;
    public static int x = 0;
    private static int[] visit;
    private static int[] dist;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        k = sc.nextInt();
        x = sc.nextInt();
        visit = new int[n + 1];
        dist = new int[n + 1];
        for(int i = 0 ; i <= n; ++i){
            dist[i] = (int)1e9;
        }
        for(int i = 0; i <= n; ++i){
            list.add(new ArrayList<Integer>());
        }

        for(int i = 0; i < m; ++i){
            int from = sc.nextInt();
            int to = sc.nextInt();
            list.get(from).add(to);
        }

        Queue<Integer> q = new LinkedList<>();
        q.offer(x);
        visit[x] = 1;
        int cnt = 0;
        dist[x] = 0;
        while(!q.isEmpty()){
            int size = q.size();
            int cur = q.poll();
            for(int j = 0; j < list.get(cur).size(); ++j){
                if(visit[list.get(cur).get(j)] == 0){
                    visit[list.get(cur).get(j)] = 1;
                    dist[list.get(cur).get(j)] = dist[cur] + 1;
                    q.offer(list.get(cur).get(j));
                }
            }
        }

        boolean check = false;
        for(int i = 1; i <= n ; ++i){
            if(dist[i] == k){
                check = true;
                System.out.println(i);
            }
        }
        if(!check) System.out.println("-1");
    }

}
