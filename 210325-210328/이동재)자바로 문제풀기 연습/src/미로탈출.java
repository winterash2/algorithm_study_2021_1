import java.util.*;

public class 미로탈출 {
    public static int N;
    public static int M;
    public static int[][] arr;
    public static int[][] visited;

    public static class Pos{
        public int x;
        public int y;
        public Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();
        arr = new int[N][M];
        visited = new int[N][M];
        for(int i=0;i<N;i++){
            String inp = sc.nextLine();
            for(int j=0;j<M;j++){
                arr[i][j] = inp.charAt(j) - '0';
                visited[i][j] = 0;
            }
        }
//        for(int i=0;i<N;i++){
//            for(int j=0;j<M;j++){
//                System.out.print(arr[i][j] + " ");
//            }
//            System.out.println();
//        }
        Queue<Pos> q = new LinkedList<>();
        q.offer(new Pos(0, 0));
        int answer = 0;
        while(!q.isEmpty()){
            answer += 1;
            boolean isEnd = false;
            int qsize = q.size();
            for(int qs=0; qs<qsize;qs++){
                Pos curPos = q.poll();
                int x = curPos.x;
                int y = curPos.y;
                if(x<0 | x >= N | y<0 | y >= M){
                    continue;
                }else if(visited[x][y] == 1 | arr[x][y] == 0){
                    continue;
                }
                if(x == N-1 & y == M-1){
                    isEnd = true;
                    break;
                }
                visited[x][y] = 1;
                q.offer(new Pos(x-1, y));
                q.offer(new Pos(x+1, y));
                q.offer(new Pos(x, y+1));
                q.offer(new Pos(x, y-1));
            }
            if(isEnd) break;
        }
        System.out.println(answer);
    }
}
