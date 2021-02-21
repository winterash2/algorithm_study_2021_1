package greedy;

import java.util.ArrayList;
import java.util.Scanner;

public class 멀티탭스케줄링 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, k;
        n = sc.nextInt();
        k = sc.nextInt();
        int[] schedule = new int[k + 1];
        for(int i = 0; i < k; ++i){
            schedule[i] = sc.nextInt();
        }
        ArrayList<Integer> tabs = new ArrayList<>();
        int[] use = new int[n];
        int answer = 0;
        for(int i = 0; i < k; ++i){
            if(tabs.size() < n){
                if(tabs.contains(schedule[i])) continue;
                tabs.add(schedule[i]);
            } else {
                if(tabs.contains(schedule[i])) continue;
                int tIndex = 0;
                int sIndex = 0;
                int nIndex = 0;


                // 가장 늦게 나오는 인덱스를 찾음
                for(int j = 0; j < tabs.size(); ++j){
                    for(int l = i; l < k; ++l){
                        if(tabs.get(j) == schedule[l]){
                            use[j] = l;
                            break;
                        }
                    }
                }

                boolean check = false;
                // 아예 안나오는 인덱스를 찾음
                for(int j = 0; j < tabs.size(); ++j){
                    check = false;
                    for(int l = i; l < k; ++l){
                        if(tabs.get(j) == schedule[l]) {
                            check = true;
                            break;
                        }
                    }
                    if(!check) {
                        nIndex = j;
                        break;
                    }
                }
//                System.out.println(i + " " + check);
                if(!check){
//                    System.out.println(nIndex + " " + tabs.remove(nIndex));
                    tabs.remove(nIndex);
                    tabs.add(schedule[i]);
                    answer++;
                } else {
//                    for(int j = 0; j < use.length; ++j){
//                        System.out.print(use[j] + " ");
//                    }
                    int maxIndex = 0;
                    int maxVal = 0;
                    for(int j = 0; j < use.length; ++j){
                        if(use[j] > maxVal) {
                            maxVal = use[j];
                            maxIndex = j;
                        }
                    }
//                    System.out.println(maxIndex + " " + tabs.remove(maxIndex));
                    tabs.remove(maxIndex);
                    tabs.add(schedule[i]);
                    answer++;
                }

            }
        }

        System.out.println(answer);
    }
}
