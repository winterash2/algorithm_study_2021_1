package simulation;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;

public class 자물쇠와열쇠 {
    public static void main(String[] args){
        int[][] key = {
                {0, 0, 0},
                {1, 0, 0},
                {0, 1, 1}
        };
        int[][] lock = {
                {1, 1, 1},
                {1, 1, 0},
                {1, 0, 1}
        };
        assertEquals(solution(key, lock), true);
    }

    public static int[][] rotate(int[][] key){
        int[][] ret = new int[key.length][key.length];
        int n = ret.length;
        for(int i = 0; i < ret.length; ++i){
            for(int j = 0; j < ret.length; ++j){
                ret[i][j] = key[n - 1 - j][i];
            }
        }
        return ret;
    }

    public static boolean check(int[][] lock){
        boolean ret = true;
        int lockLength = lock.length / 3;
        for (int i = lockLength; i < lockLength * 2; ++i) {
            for (int j = lockLength; j < lockLength * 2; ++j) {
                if (lock[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }


    public static boolean solution(int[][] key, int[][] lock) {
        boolean answer = false;
        int n = lock.length;
        int m = key.length;
        int[][] copyKey = key.clone();
        int[][] newLock = new int[3 * n][3 * n];

        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                newLock[i + n][j + n] = lock[i][j];
            }
        }

        for(int rotate = 0; rotate < 4; ++rotate) {
            copyKey = rotate(copyKey);
            for (int x = 0; x < n * 2; ++x) {
                for (int y = 0; y < n * 2; ++y) {
                    // 2차원 배열을 deepcopy 하는 방법 Java8
                    int[][] copyLock = Arrays.stream(newLock).map(int[]::clone).toArray(int[][]::new);
                    for(int i = 0; i < m; ++i){
                        for(int j = 0; j < m; ++j){
                            if(copyKey[i][j] == 1 && copyLock[x + i][y + j] == 0){
                                copyLock[x + i][y + j] = 1;
                                continue;
                            }
                            if(copyKey[i][j] == 1 && copyLock[x + i][y + j] == 1){
                                copyLock[x + i][y + j] = 0;
                            }
                        }
                    }
                    //check
                    if(check(copyLock)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
