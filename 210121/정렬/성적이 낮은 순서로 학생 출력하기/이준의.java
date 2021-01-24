package sort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Student implements Comparable<Student>{
    String name;
    int score;
    public Student(String name, int score){
        this.name = name;
        this.score = score;
    }

    @Override
    public int compareTo(Student o) {
        return this.score - o.score;
    }
}

public class 성적이낮은순서로학생출력하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        ArrayList<Student> arr = new ArrayList<>();
        for(int i = 0; i < n; ++i){
            String input = sc.nextLine();
            String[] splitInput = input.split(" ");
            arr.add(new Student(splitInput[0], Integer.valueOf(splitInput[1])));
        }
        Collections.sort(arr);
        for(int i = 0; i < arr.size(); ++i){
            System.out.print(arr.get(i).name + " ");
        }
    }
}
