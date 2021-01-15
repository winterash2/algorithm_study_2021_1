package simulation;


import static org.junit.Assert.assertEquals;

public class 게임개발 {
    public static void main(String[] args){
        int N = 4;
        int M = 4;
        int[] character = {1, 1, 0};
        int[][] map = {
                {1, 1, 1, 1},
                {1, 0, 0, 1},
                {1, 1, 0, 1},
                {1, 1, 1, 1}
        };
        assertEquals(solution(N, M, character, map), 3);
    }
    public static int solution(int N, int M, int[] character, int[][] map){
        int answer = 0;
        // 북, 동, 남, 서
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        int[] cur = {character[0], character[1], character[2]};
        int[][] visit = new int[N][M];
        visit[cur[0]][cur[1]] = 1;
        answer++;
        for(;;){
            boolean isMoved = false;
            for(int i = 0; i < 4; ++i){
                int nextDir = cur[2] - 1 < 0 ? 3 : cur[2] - 1;
                int nextX = cur[0] + dx[nextDir];
                int nextY = cur[1] + dy[nextDir];
                cur[2] = nextDir;
                if(nextX < 0 || nextX >= N || nextY < 0 || nextY > M) continue;
                if(map[nextX][nextY] != 1 && visit[nextX][nextY] == 0){
                    visit[nextX][nextY] = 1;
                    isMoved = true;
                    cur[0] = nextX;
                    cur[1] = nextY;
                    cur[2] = nextDir;
                    answer++;
                    break;
                }
                if(isMoved) break;
            }
            if(!isMoved) break;
        }
        return answer;
    }
}
