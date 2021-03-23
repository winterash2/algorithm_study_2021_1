package hash;

import java.util.*;
import java.io.*;

public class 연습2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input = "ZzZz9Z824";

        HashMap<Character, Integer> hashmap = new HashMap<>();

        String special = "~!@#$%^&*";
        for(int i = 0; i < 26; ++i){
            hashmap.put((char)('a' + i), 0);
            hashmap.put((char)('A' + i), 0);
        }
        for(int i = 0; i < 10; ++i){
            hashmap.put((char)('0' + i), 0);
        }
        for(int i = 0; i < special.length(); ++i){
            hashmap.put(special.charAt(i), 0);
        }

        boolean[] check = new boolean[4];
        boolean otherCharacter = false;
        boolean sameCharacterCheck = false;
        int sameCharacterCnt = 1;
        char prev = input.charAt(0);
        for(int i = 0; i < input.length(); ++i){
            char ch = input.charAt(i);

            if(i != 0 && prev == ch){
                sameCharacterCnt++;
                if(sameCharacterCnt >= 4) {
                    sameCharacterCheck = true;
                }
            } else {
                prev = ch;
                sameCharacterCnt = 1;
            }

            if(Character.isDigit(ch)){
                check[0] = true;
            } else if(Character.isUpperCase(ch)){
                check[1] = true;
            } else if(Character.isLowerCase(ch)){
                check[2] = true;
            } else if(special.indexOf(ch) != -1){
                check[3] = true;
            }
            if(!hashmap.containsKey(ch)){
                otherCharacter = true;
                continue;
            } else {
                hashmap.put(ch, hashmap.get(ch) + 1);
            }
        }

        int checkCnt = 0;
        for(int i = 0; i < 4; ++i){
            if(check[i] == true) checkCnt++;
        }

        ArrayList<Integer> answer = new ArrayList<>();
        if(8 > input.length() || input.length() > 15){
            answer.add(1);
        }
        if(otherCharacter){
            answer.add(2);
        }
        if(checkCnt < 3){
            answer.add(3);
        }
        if(sameCharacterCheck){
            answer.add(4);
        }
        for(Map.Entry<Character, Integer> entry : hashmap.entrySet()){
            if(entry.getValue() >= 5){
                answer.add(5);
                break;
            }
        }
        if(answer.size() == 0) answer.add(0);
        for(Integer a : answer){
            bw.write(a + " ");
        }
        bw.write("\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

