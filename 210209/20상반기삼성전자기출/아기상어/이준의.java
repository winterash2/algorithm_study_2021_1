package samsung;

import javax.swing.plaf.IconUIResource;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

class Fish implements Comparable<Fish>{
    int x, y;
    public Fish(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Fish o) {
        if(this.x == o.x){
            return this.y - o.y;
        } else {
            return this.x - o.x;
        }
    }
}

class Step{
    int x, y;
    public Step(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 아기상어 {

    static int n;
    static int[][] map;
    static boolean[][] check;

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};

    static PriorityQueue<Fish> pq;
    static Queue<Step> q;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        map = new int[n + 1][n + 1];
        check = new boolean[n + 1][n + 1];

        int startX = 0, startY = 0;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                map[i][j] = sc.nextInt();
                if(map[i][j] == 9){
                    startX = i;
                    startY = j;
                }
            }
        }

        pq = new PriorityQueue<>();
        q = new LinkedList<>();

        q.offer(new Step(startX, startY));
        map[startX][startY] = 0;
        check[startX][startY] = true;

        int sharkSize = 2;
        int needToEat = 2;
        int answer = 0;
        int time = 0;

        while(!q.isEmpty()){
            int size = q.size();
            // 아기상어의 이동
            for(int i = 0; i < size; ++i){
                Step cur = q.poll();
                int curX = cur.x;
                int curY = cur.y;

                // 이동경로에 먹을 수 있는 물고기가 있으면 힙에 추가
                if(map[curX][curY] != 0 && map[curX][curY] < sharkSize){
                    pq.offer(new Fish(curX, curY));
                }

                // 4방향 이동
                for(int j = 0; j < 4; ++j){
                    int nx = curX + dx[j];
                    int ny = curY + dy[j];
                    if(0 <= nx && nx < n && 0 <= ny && ny < n && check[nx][ny] != true
                            && map[nx][ny] <= sharkSize
                    )
                    {
                        check[nx][ny] = true;
                        q.offer(new Step(nx, ny));
                    }
                }
            }

            if(!pq.isEmpty()){
                Fish start = pq.poll();
                startX = start.x;
                startY = start.y;

                map[startX][startY] = 0;
                needToEat--;
                if(needToEat == 0){
                    sharkSize++;
                    needToEat = sharkSize;
                }

                while(!pq.isEmpty()){
                    pq.poll();
                }

                while(!q.isEmpty()){
                    q.poll();
                }

                check = new boolean[n + 1][n + 1];
                check[startX][startY] = true;
                q.offer(new Step(startX, startY));
                answer += time;
                time = 0;
            } else {
                time++;
            }
        }

        System.out.println(answer);
    }
}
/*
3
0 0 0
0 1 0
0 9 0
 */