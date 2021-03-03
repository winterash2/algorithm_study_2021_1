package dfsbfs2;

import soma.B;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.Buffer;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 숨바꼭질 {

    static int n, k;
    static boolean[] check = new boolean[100001];
    static int[] dis = new int[100001];

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        Queue<Integer> q = new LinkedList<>();
        dis[n] = 0;
        check[n] = true;
        q.offer(n);
        while(!q.isEmpty()){
            int now = q.poll();
            if(now - 1 >= 0 && ! check[now - 1]){
                dis[now - 1] = dis[now] + 1;
                check[now - 1] = true;
                q.offer(now - 1);
            }
            if(now + 1 <= 100000 && !check[now + 1]){
                dis[now + 1] = dis[now] + 1;
                check[now + 1] = true;
                q.offer(now + 1);
            }
            if(now * 2 <= 100000 && !check[now * 2]){
                dis[now * 2] = dis[now] + 1;
                check[now * 2] = true;
                q.offer(now * 2);
            }
        }
        bw.write(dis[k] + " \n");
        bw.flush();
        bw.close();
        br.close();
    }
}
