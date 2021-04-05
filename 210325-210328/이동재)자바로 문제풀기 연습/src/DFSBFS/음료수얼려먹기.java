package DFSBFS;

import java.util.Collections;
import java.util.Scanner;
import java.util.Stack;


public class 음료수얼려먹기 {
    public static int N;
    public static int M;
    public static int[][] arr;

    public static boolean dfs(int x, int y) {
        class Pos {
            int x;
            int y;

            public Pos(int x, int y) {
                this.x = x;
                this.y = y;
            }
        }
        Stack<Pos> stack = new Stack<Pos>();
        stack.push(new Pos(x, y));
        while (!stack.isEmpty()) {
            Pos curPos = stack.pop();
            x = curPos.x;
            y = curPos.y;
            if (x < 0 | x >= N | y < 0 | y >= M) {
                continue;
            }
            if (arr[x][y] == 0) {
                arr[x][y] = 1;
                stack.push(new Pos(x - 1, y));
                stack.push(new Pos(x + 1, y));
                stack.push(new Pos(x, y + 1));
                stack.push(new Pos(x, y - 1));
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        arr = new int[N][M];
        sc.nextLine();
        for (int i = 0; i < N; i++) {
            String inp = sc.nextLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = inp.charAt(j) - '0';
            }
        }
//        for(int i=0; i<N;i++){
//            for(int j=0;j<M;j++){
//                System.out.print(arr[i][j] + " ");
//            }
//            System.out.println();
//        }
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0) {
                    count += 1;
                    dfs(i, j);
//                    System.out.println("-"+i+" "+j);
//                    for (int a = 0; a < N; a++) {
//                        for (int b = 0; b < M; b++) {
//                            System.out.print(arr[a][b] + " ");
//                        }
//                        System.out.println();
//                    }
//                    System.out.println("-");
                }
            }
        }
        System.out.println(count);
    }
}
/*
4 5
00110
00011
11111
00000
 */
/*
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
 */