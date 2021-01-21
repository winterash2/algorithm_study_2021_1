package dfsbfs;

import java.util.*;

class Position{
    int x;
    int y;
    public Position(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class 인구이동 {

    private static int n, l, r;
    private static int[][] map, visit;
    private static int cnt, ans;

    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    private static ArrayList<ArrayList<Position>> union = new ArrayList<>();


    public static void dfs(int x, int y){
        visit[x][y] = 1;
        union.get(cnt).add(new Position(x, y));
        for(int i = 0 ; i < 4; ++i){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < n && 0 <= ny && ny < n && visit[nx][ny] == 0){
                int val = Math.abs(map[x][y] - map[nx][ny]);
                if(l <= val && val <= r){
                    dfs(nx, ny);
                }
            }
        }
    }

    public static boolean move(){
        boolean isEnd = true;
        for(int i = 0; i < cnt; ++i){
            if(union.get(i).size() >= 2){
                isEnd = false;
                double sum = 0;
                for(int j = 0; j < union.get(i).size(); ++j){
                    sum += map[union.get(i).get(j).x][union.get(i).get(j).y];
                }
                for(int j = 0; j < union.get(i).size(); ++j){
                    map[union.get(i).get(j).x][union.get(i).get(j).y] = (int) sum / union.get(i).size();
                }
            }
        }
        if(isEnd) return true;
        else {
            init();
            return false;
        }
    }

    public static void init(){
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                visit[i][j] = 0;
            }
        }
        union.clear();
        for(int i = 0; i < n * n + 1; ++i){
            union.add(new ArrayList<>());
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        l = sc.nextInt();
        r = sc.nextInt();
        map = new int[n][n];
        visit = new int[n][n];

        for(int i = 0; i < n; ++i){
            for(int j = 0 ; j < n ; ++j){
                map[i][j] = sc.nextInt();
            }
        }
        for(int i = 0; i < n * n + 1; ++i){
            union.add(new ArrayList<>());
        }
        while(true){
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < n; ++j){
                    if(visit[i][j] == 0){
                        dfs(i , j);
                        cnt++;
                    }
                }
            }
            if(move() == true){
                System.out.println(ans);
                break;
            } else {
                cnt = 0;
                ans++;
            }

        }
    }
}
