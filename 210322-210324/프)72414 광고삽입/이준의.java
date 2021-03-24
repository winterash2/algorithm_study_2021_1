// 좀 더 생각해봐야 할듯

package simulation;

import java.util.*;
import java.io.*;

class Log{
    int start, end;
    public Log(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class AD{
    int start, time;
    public AD(int start, int time) {
        this.start = start;
        this.time = time;
    }
}

public class 광고삽입 {

    public static String solution(String play_time, String adv_time, String[] logs) {
        String answer = "";
        if(play_time.equals(adv_time)) return "00:00:00";

        ArrayList<Log> sortedLog = new ArrayList<>();
        for(String log : logs) {
            int start = Integer.parseInt(log.substring(0, 2)) * 3600 + Integer.parseInt(log.substring(3, 5)) * 60 + Integer.parseInt(log.substring(6, 8));
            int end = Integer.parseInt(log.substring(9, 11)) * 3600 + Integer.parseInt(log.substring(12, 14)) * 60 + Integer.parseInt(log.substring(15, 17));
            sortedLog.add(new Log(start, end));
        }
        Collections.sort(sortedLog, (a, b) -> {
            return a.start - b.start;
        });

        int total = Integer.MIN_VALUE;
        int index1 = 0;
        int index2 = 1;
        int advPlayTime = Integer.parseInt(adv_time.substring(0, 2)) * 3600 + Integer.parseInt(adv_time.substring(3, 5)) * 60 + Integer.parseInt(adv_time.substring(6, 8));
        int len = sortedLog.size();
        ArrayList<AD> answers = new ArrayList<>();
        while(index1 < len && index2 < len){
            if(index2 == len - 1 || sortedLog.get(index2 + 1).start > sortedLog.get(index2).end){
                // 누적 시간 계산
                int adStart = sortedLog.get(index1 + 1).start;
                int adEnd = adStart + advPlayTime;
                int sum = 0;
                for(int i = index1; i <= index2; ++i){
                    sum += Math.min(adEnd - sortedLog.get(i).start, sortedLog.get(i).end - adStart);
                }
                answers.add(new AD(adStart, sum));
                index1 = index2 + 1;
                index2 = index1 + 1;
            } else{
                index2++;
            }
        }

        Collections.sort(answers, (a, b) -> {
            if(a.time == b.time){
                return a.start - b.start;
            } else {
                return b.time - a.time;
            }
        });

        for(AD ad : answers){
            System.out.println(ad.time + " " + ad.start);
        }

        int answerTime = answers.get(0).start;
        int hour = answerTime / 3600;
        answerTime %= 3600;
        int minute = answerTime / 60;
        answerTime %= 60;
        int seconds = answerTime;

        answer = Integer.toString(hour) + ":" + Integer.toString(minute) + ":" + Integer.toString(seconds);

        return answer = answer.length() == 8 ? answer : "0" + answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] logs = new String[]{"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"};
        bw.write(solution("99:59:59", "25:00:00", logs));
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
"02:03:55"
"00:14:15"
["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
 */
