package 정렬;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class 성적이낮은순서로학생출력하기 {

    public static class Student implements Comparable<Student>{
        public String name;
        public int score;
        Student(String name, int score){
            this.name = name;
            this.score = score;
        }
        @Override
        public int compareTo(Student other){
            if(this.score > other.score) {
                return 1;
            }else{
                return -1;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        ArrayList<Student> students = new ArrayList<Student>();
        for(int i=0; i<N; i++){
            String inp = sc.nextLine();
            String[] inps = inp.split(" ");
            students.add(new Student(inps[0], Integer.parseInt(inps[1])));
        }
        Collections.sort(students);
        for(int i=0; i<students.size(); i++){
            System.out.print(students.get(i).name + " ");
        }
    }
}
/*
2
홍길동 95
이순신 77
 */