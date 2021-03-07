package greedy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Meeting{
    int start, end;
    public Meeting(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class 회의실배정 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        Meeting[] meetings = new Meeting[n];
        for(int i = 0; i < n; ++i){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            meetings[i] = new Meeting(start, end);
        }
        Arrays.sort(meetings, (a, b) -> {
            if(a.end == b.end){
                return a.start - b.start;
            } else {
                return a.end - b.end;
            }
        });

        int answer = 0;
        int cur = 0;

        for(int i = 0; i < meetings.length; ++i){
            if(cur <= meetings[i].start){
                cur = meetings[i].end;
                answer++;
            }
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
 */