package simulation;

import java.util.*;

import static org.junit.Assert.assertEquals;

class Pair{
    int sec;
    String direction;
    public Pair(int sec, String direction){
        this.sec = sec;
        this.direction = direction;
    }
    public int getKey(){
        return sec;
    }
    public String getValue(){
        return direction;
    }
}

class Snake{
    int x;
    int y;
    public Snake(int x, int y){
        this.x = x;
        this.y = y;
    }
    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }
}

public class 뱀 {
    public static void main(String[] args){
        assertEquals(solve(), 9);
    }
    public static int solve(){
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[][] map = new int[n + 1][n + 1];
        for(int i = 0; i < k; ++i){
            int x = sc.nextInt();
            int y = sc.nextInt();
            map[x][y] = 1;
        }
        int L = sc.nextInt();
        sc.nextLine();
        List<Pair> list = new ArrayList<>();
        for(int i = 0; i < L; ++i){
            String str = sc.nextLine();
            String[] sarr = str.split(" ");
            list.add(new Pair(Integer.parseInt(sarr[0]), sarr[1]));
        }

        // 동, 남, 서, 북
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int dir = 0;
        Pair nextDir = list.get(0);
        Queue<Snake> snake = new LinkedList<>();
        snake.offer(new Snake(1, 1));
        map[1][1] = 2;
        int x = 1;
        int y = 1;

        for(;;){
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(1 <= nx && nx <= n && 1 <= ny && ny <= n && map[nx][ny] != 2){
                if(map[nx][ny] == 0){
                    map[nx][ny] = 2;
                    snake.offer(new Snake(nx, ny));
                    Snake prev = snake.poll();
                    map[prev.getX()][prev.getY()] = 0;
                }
                if(map[nx][ny] == 1){
                    map[nx][ny] = 2;
                    snake.offer(new Snake(nx, ny));
                }
            } else {
                answer++;
                break;
            }
            x = nx;
            y = ny;
            answer++;
            if(answer == nextDir.getKey()){
                if(nextDir.getValue().equals("L")){
                    dir = dir - 1 < 0 ? 3 : dir - 1;
                } else {
                    dir = (dir + 1) % 4;
                }
                if(!list.isEmpty()){
                    list.remove(0);
                    if(!list.isEmpty())
                        nextDir = list.get(0);
                }
            }
        }
        return answer;
    }
}
