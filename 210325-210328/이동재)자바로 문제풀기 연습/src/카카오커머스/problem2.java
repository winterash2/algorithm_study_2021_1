class Solution {
    public int[] robot;
    public int n;
    public int result = 0;

    public void dfs(int[][] needs, int idx, int r){
        if (idx < n & r > 0) {
            robot[idx] = 1;
            dfs(needs, idx+1, r-1);
            robot[idx] = 0;
            dfs(needs, idx+1, r);
        }else{
            int count = 0;
            for (int[] need : needs) {
                boolean possible = true;
                for (int i = 0; i < n; i++) {
                    if(need[i] == 1 & robot[i] == 0){
                        possible = false;
                        break;
                    }
                }
                if (possible) {
                    count += 1;
                }
            }
            result = Integer.max(result, count);
        }
    }

    public int solution(int[][] needs, int r) {
        int answer = 0;
        n = needs[0].length;

        robot = new int[n];
        for (int i = 0; i < n; i++) {
            robot[i] = 0;
        }
        dfs(needs, 0, r);
        answer = result;

        return answer;
    }
}