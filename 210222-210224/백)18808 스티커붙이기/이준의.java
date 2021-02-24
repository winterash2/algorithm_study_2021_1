package bruteforce;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 스티커붙이기 {

    static int[][] noteBook;
    static int[][] sticker;
    static int n, m, k;
    static int sn, sm;

    static int[][] rotate(int[][] orig){
        int[][] ret = new int[sm][sn];
        for(int i = 0; i < sm; ++i){
            for(int j = 0, l = sn - 1; j < sn; ++j, --l){
                ret[i][j] = orig[l][i];
            }
        }
        int tmp = sn;
        sn = sm;
        sm = tmp;
        return ret;
    }

    static boolean putSticker(int x, int y){
        boolean check = true;
        for(int i = 0; i < sn; ++i){
            for(int j = 0; j < sm; ++j){
                if(noteBook[x + i][y + j] == 1 && sticker[i][j] == 1) check = false;
                if(sticker[i][j] == 1) noteBook[x + i][y + j] += 1;
            }
        }
        return check;
    }

    static void removeSticker(int x, int y){
        for(int i = 0; i < sn; ++i){
            for(int j = 0; j < sm; ++j){
                if(sticker[i][j] == 1) noteBook[x + i][y + j] -= 1;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        noteBook = new int[n][m];
        int answer = 0;
        for(int i = 0; i < k; ++i){
            st = new StringTokenizer(br.readLine());
            sn = Integer.parseInt(st.nextToken());
            sm = Integer.parseInt(st.nextToken());
            sticker = new int[sn][sm];
            for(int a = 0; a < sn; ++a){
                st = new StringTokenizer(br.readLine());
                for(int b = 0; b < sm; ++b){
                    sticker[a][b] = Integer.parseInt(st.nextToken());
                }
            }

            for(int rot = 0; rot < 4; ++rot){
                boolean check = false;
                for(int a = 0; a <= n - sn; ++a){
                    for(int b = 0; b <= m - sm; ++b){
                        if(!putSticker(a, b)){
                            removeSticker(a, b);
                        } else {
                            check = true;
                            break;
                        }
                    }
                    if(check) break;
                }
                if(check) break;
                else sticker = rotate(sticker);
            }
        }
        for(int a = 0; a < n; ++a){
            for(int b = 0; b < m; ++b){
                if(noteBook[a][b] == 1) answer++;
            }
        }
        System.out.println(answer);
    }
}


/*
5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0
 */