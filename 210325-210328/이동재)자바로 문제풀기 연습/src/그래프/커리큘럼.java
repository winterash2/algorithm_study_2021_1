package 그래프;

import java.util.*;

public class 커리큘럼 {
    public static int N;
    public static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        graph = new ArrayList<>();
        for(int i = 0; i<N+1; i++){
            graph.add(new ArrayList<>());
        }
        int[] times = new int[N + 1];
        int[] degrees = new int[N + 1];
        int[] startTimes = new int[N + 1];
        for(int i = 0; i<N+1; i++){
            degrees[i] = 0;
            startTimes[i] = 0;
        }

        sc.nextLine();
        for (int i = 0; i < N; i++) {
            String inp = sc.nextLine();
            String[] inpSplit = inp.split(" ");
            boolean first = true;
            for (String s : inpSplit) {
                if (Integer.parseInt(s) == -1) {
                    break;
                } else {
                    if (first) {
                        times[i + 1] = Integer.parseInt(s);
                        first = false;
                    } else {
                        int need = Integer.parseInt(s);
                        graph.get(need).add(i + 1);
                        degrees[i + 1] += 1;
                    }
                }
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i < N + 1; i++) {
            if (degrees[i] == 0) {
                q.offer(i);
            }
        }
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int nxt : graph.get(cur)) {
                startTimes[nxt] = Integer.max(startTimes[nxt], startTimes[cur] + times[cur]);
                degrees[nxt] -= 1;
                if (degrees[nxt] == 0) {
                    q.offer(nxt);
                }
            }
        }
        int[] answer = new int[N];
        for (int i = 1; i < N + 1; i++) {
            answer[i-1] = startTimes[i] + times[i];
//            answer = Integer.max(answer, startTimes[i] + times[i]);
        }
        for (int a : answer) {
            System.out.println(a);
        }
    }
}
/*
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
 */