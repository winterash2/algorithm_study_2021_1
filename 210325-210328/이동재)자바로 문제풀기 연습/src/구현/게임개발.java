import java.util.Scanner;

public class 게임개발 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int d = sc.nextInt();
        int[][] arr = new int[N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr[i][j] = sc.nextInt();
            }
        }
//        for(int i=0; i<N; i++){
//            for(int j=0; j<N; j++){
//                System.out.print(arr[i][j] + " ");
//            }
//            System.out.println();
//        }

        int[] dx = {0, 1, 0, -1};
        int[] dy = {-1, 0, 1, 0};
        int x = A;
        int y = B;
        arr[y][x] = 2;
        int count = 1;
        int answer = 0;
        while(true){
            boolean go = false;
            for(int i=0;i<4;i++){
                d -= 1;
                if(d < 0) d = 3;
                int nx = x + dx[d];
                int ny = y + dy[d];
                if(arr[ny][nx] == 0){
                    x = nx;
                    y = ny;
                    arr[y][x] = 2;
                    go = true;
                    count += 1;
                    break;
                }
            }
            if(go){
                continue;
            }
            int nx = x - dx[d];
            int ny = y - dy[d];
            if(arr[ny][nx] == 1){
                break;
            }else{
                x = nx;
                y = ny;
            }
        }
        System.out.println(count);
    }
}
/*
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
 */

/*
5 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 1 1 0 1
1 1 1 0 1
1 1 1 1 1
 */