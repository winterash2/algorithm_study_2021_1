package simulation;

import java.util.ArrayList;

import static org.junit.Assert.assertArrayEquals;

public class 기둥과보설치 {
    public static void main(String[] args){
        int[][] buildFrame = {
                {1, 0, 0, 1},
                {1, 1, 1, 1},
                {2, 1, 0, 1},
                {2, 2, 1, 1},
                {5, 0, 0, 1},
                {5, 1, 0, 1},
                {4, 2, 1, 1},
                {3, 2, 1, 1}
        };
        int[][] result = {
                {1, 0, 0},
                {1, 1, 1},
                {2, 1, 0},
                {2, 2, 1},
                {3, 2, 1},
                {4, 2, 1},
                {5, 0, 0},
                {5, 1, 0}
        };
        assertArrayEquals(solve(5, buildFrame), result);
    }

    static int[][] map = new int[101][101];

    public static boolean check(int x, int y, int a){
        boolean ret = true;
        return ret;
    }

    public static int[][] solve(int n, int[][] buildFrame){
        ArrayList<ArrayList<Integer>> answer = new ArrayList<ArrayList<Integer>>();

        for(int i = 0; i < buildFrame.length; ++i){
            int x = buildFrame[i][0];
            int y = buildFrame[i][1];
            int a = buildFrame[i][2];
            int b = buildFrame[i][3];

            // 설치
            if(b == 1){
                map[x][y] = a + 1;
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(x);
                temp.add(y);
                temp.add(a);
                answer.add(temp);

                // 보
                if(a == 1){
                    if(!(map[x][y - 1] == 1 || map[x + 1][y - 1] == 1 || map[x - 1][y] == 2 || map[x + 1][y] == 2)){
                        answer.remove(answer.size() - 1);
                        map[x][y] = 0;
                    }
                } else {
                    if(!(y == 0 || map[x - 1][y] == 2 || map[x + 1][y] == 2 || map[x][y - 1] == 1)){
                        answer.remove(answer.size() - 1);
                        map[x][y] = 0;
                    }
                }
            } else{
                map[x][y] = 0;
                if(a == 1){

                } else{

                }
            }
// ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

//            // 보
//            if(a == 1){
//                if(map[x][y - 1] == 1 || map[x + 1][y - 1] == 1 || map[x - 1][y] == 2 || map[x + 1][y] == 2){
//                    map[x][y] = a + 1;
//                    ArrayList<Integer> temp = new ArrayList<>();
//                    temp.add(x);
//                    temp.add(y);
//                    temp.add(a);
//                    answer.add(temp);
//                }
//            } else {
//                if(y == 0 || map[x - 1][y] == 2 || map[x + 1][y] == 2 || map[x][y - 1] == 1){
//                    map[x][y] = a + 1;
//                    ArrayList<Integer> temp = new ArrayList<>();
//                    temp.add(x);
//                    temp.add(y);
//                    temp.add(a);
//                    answer.add(temp);
//                }
//            }
        }

        for(int i = 0; i < answer.size(); ++i){
            System.out.println(answer.get(i));
        }

        // 배열로 바꾸어 반환
        int[][] res = new int[answer.size()][3];
//        for (int i = 0; i < answer.size(); i++) {
//            res[i][0] = answer.get(i).getX();
//            res[i][1] = answer.get(i).getY();
//            res[i][2] = answer.get(i).getStuff();
//        }
        return res;
    }
}
