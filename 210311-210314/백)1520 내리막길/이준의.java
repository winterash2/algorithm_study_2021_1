// 메모리초과 ..
package dp;

import java.util.*;
import java.io.*;

class Node{
    int x, y;
    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 내리막길 {

    static int[] dx = {0, 0, 1};
    static int[] dy = {1, -1, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] map = new int[n][m];

        for(int i = 0; i < n; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; ++j){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0));
        while(!q.isEmpty()){
            int x = q.peek().x;
            int y = q.peek().y;
            q.poll();
            if(x == n - 1 && y == m - 1){
                answer++;
                continue;
            }
            for(int i = 0; i < 3; ++i){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < n && 0 <= ny && ny < m){
                    if(map[x][y] > map[nx][ny])
                        q.offer(new Node(nx, ny));
                }
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}



//package dp;
//
//import java.util.*;
//import java.io.*;
//
//class Visit{
//    int x,y;
//    public Visit(int x, int y) {
//        this.x = x;
//        this.y = y;
//    }
//}
//
//public class 내리막길 {
//
//    static int n, m;
//    static int[][] map;
//    static HashMap<Visit, Boolean> hashMap = new HashMap<>();
//    static int answer = 0;
//
//    public static void dp(int x, int y){
//        System.out.println(x + " " + y);
//        if(x < 0 || x >= n || y <  0 || y >= m) return;
//        if(x == n - 1 && y == m - 1){
//            answer++;
//        }
//        int cur = map[x][y];
//        if(x + 1 < n && cur > map[x + 1][y]){
//            dp(x + 1, y);
//        }
//        if(y + 1 < m && cur > map[x][y + 1]){
//            dp(x, y+ 1);
//        }
//        if(0 <= y - 1 && cur > map[x][y - 1]){
//            dp(x + 1, y);
//        }
//    }
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        n = Integer.parseInt(st.nextToken());
//        m = Integer.parseInt(st.nextToken());
//        map = new int[n][m];
//
//        for(int i = 0; i < n; ++i){
//            st = new StringTokenizer(br.readLine());
//            for(int j = 0; j < m; ++j){
//                map[i][j] = Integer.parseInt(st.nextToken());
//            }
//        }
//
//        dp(0, 0);
//        bw.write(answer + "\n");
//        bw.flush();
//        bw.close();
//        br.close();
//    }
//}





/*
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
 */