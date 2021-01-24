package sort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Score implements Comparable<Score> {
    int koreanScore;
    int englishScore;
    int mathScore;
    String name;
    public Score(String name, int koreanScore, int englishScore, int mathScore){
        this.name = name;
        this.koreanScore = koreanScore;
        this.englishScore = englishScore;
        this.mathScore = mathScore;
    }

    @Override
    public int compareTo(Score o) {
        if(this.koreanScore == o.koreanScore){
            if(this.englishScore == o.englishScore){
                if(this.mathScore == o.mathScore){
                    return this.name.compareTo(o.name);
                }
                return o.mathScore - this.mathScore;
            }
            return this.englishScore - o.englishScore;
        }

        return o.koreanScore - this.koreanScore;
    }
}

public class 국영수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        ArrayList<Score> list = new ArrayList<>();
        for(int i = 0; i < n; ++i){
            String[] input = sc.nextLine().split(" ");
            list.add(new Score(input[0], Integer.valueOf(input[1]), Integer.valueOf(input[2]), Integer.valueOf(input[3])));
        }
        Collections.sort(list);
        for(int i = 0; i < list.size(); ++i){
//            System.out.println(list.get(i).name + " " + list.get(i).koreanScore + " " + list.get(i).englishScore + " " + list.get(i).mathScore);
            System.out.println(list.get(i).name);
        }
    }
}
