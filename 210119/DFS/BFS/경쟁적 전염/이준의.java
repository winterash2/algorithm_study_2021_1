package dfsbfs2;

import java.util.*;

class Virus implements Comparable<Virus>{
    int x;
    int y;
    int val;
    public Virus(int x, int y, int val){
        this.x = x;
        this.y = y;
        this.val = val;
    }

    @Override
    public int compareTo(Virus o) {
        return this.val - o.val;
    }
}

public class 경쟁적전염 {

    private static int n, k, s, x, y;
    private static int[][] map;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        map = new int[n][n];
        ArrayList<Virus> array = new ArrayList<>();
        Queue<Virus> q = new LinkedList<>();

        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j){
                map[i][j] = sc.nextInt();
                if(map[i][j] != 0){
                    array.add(new Virus(i, j, map[i][j]));
                }
            }
        }

        s = sc.nextInt();
        x = sc.nextInt();
        y = sc.nextInt();

        Collections.sort(array);

        for(Virus v : array){
            q.offer(v);
        }

        for(int i = 0; i < s; ++i){
            int size = q.size();
            for(int j = 0; j < size; ++j){
                Virus cur = q.poll();
                for(int k = 0; k < 4; ++k){
                    int nx = cur.x + dx[k];
                    int ny = cur.y + dy[k];
                    if(0 <= nx && nx < n && 0 <= ny && ny < n){
                        if(map[nx][ny] == 0) {
                            map[nx][ny] = cur.val;
                            q.offer(new Virus(nx, ny, cur.val));
                        }
                    }
                }
            }
        }

        System.out.println(map[x - 1][y - 1]);
    }
}
