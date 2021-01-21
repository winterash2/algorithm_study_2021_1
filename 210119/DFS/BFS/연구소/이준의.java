package dfsbfs;

import java.util.*;

class Node{
    int x;
    int y;
    public Node(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class 연구소 {

    private static int n;
    private static int m;
    private static int[][] map;
    private static int[][] copyMap;
    private static int maxVal = 0;

    private static int[] dx = {0, 0, 1, -1};
    private static int[] dy = {-1, 1, 0, 0};

    private static ArrayList<Node> virus = new ArrayList<>();

    public static void bfs(){
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                copyMap[i][j] = map[i][j];
            }
        }

        Queue<Node> q = new LinkedList<>();
        for(Node node : virus){
            q.offer(node);
        }

        while(!q.isEmpty()){
            Node cur = q.poll();
            for(int i = 0 ; i < 4; ++i){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && copyMap[nx][ny] == 0){
                    copyMap[nx][ny] = 2;
                    q.offer(new Node(nx, ny));
                }
            }
        }

        int cnt = 0;
        for(int i = 0 ; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(copyMap[i][j] == 0) cnt++;
            }
        }
        if(cnt > maxVal) maxVal = cnt;
    }

    public static void wall(int cnt){
        if(cnt == 3){
            bfs();
            return;
        }
        for(int i = 0 ; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(map[i][j] == 0){
                    map[i][j] = 1;
                    wall(cnt + 1);
                    map[i][j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        map = new int[n][m];
        copyMap = new int[n][m];
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                map[i][j] = sc.nextInt();
                if(map[i][j] == 2){
                    virus.add(new Node(i, j));
                }
            }
        }
        wall(0);
        System.out.println(maxVal);
    }
}
