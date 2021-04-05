import java.util.*;

class Solution {
    public int maxCount = 0;
    public int maxNode = 0;
    public int N;
    ArrayList<ArrayList<Integer>> graph;

    public void dfs(int start, ArrayList<Integer> passed, int count, int[] passenger) {
        boolean isEnd = true;
        passed.add(start);
        count += passenger[start-1];
        for(int i = 0; i < graph.get(start).size(); i++){
            int nxt = graph.get(start).get(i);
            if(!passed.contains(nxt)){
                isEnd = false;
                dfs(nxt, passed, count, passenger);
            }
        }
        if(isEnd){
            if(count > maxCount){
                maxCount = count;
                maxNode = start;
            } else if (count == maxCount) {
                maxNode = Integer.max(maxNode, start);
            }
        }
        passed.remove(passed.size()-1);
    }

    public int[] solution(int n, int[] passenger, int[][] train) {
        int[] answer = new int[2];
        N = passenger.length;
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < train.length; i++) {
            int a = train[i][0];
            int b = train[i][1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        ArrayList<Integer> passed = new ArrayList<>();
        dfs(1, passed, 0, passenger);
        answer[0] = maxNode;
        answer[1] = maxCount;

        return answer;
    }
}