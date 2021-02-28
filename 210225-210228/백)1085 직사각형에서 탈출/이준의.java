package math;

import java.util.Scanner;

public class 직사각형에서탈출 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, y, w, h;
        x = sc.nextInt();
        y = sc.nextInt();
        w = sc.nextInt();
        h = sc.nextInt();

        int answer = Math.min(Math.min(h - y, y), Math.min(w - x, x));
        System.out.println(answer);
    }
}
