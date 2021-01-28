package dp;

public class One {

    static int[] d = new int[30001];

    static int dfs(int n){
        if(n == 1) return 0;
        if(d[n] != 0) return d[n];
        int a1 = 9999, a2 = 9999, a3 = 9999, a4 = 9999;
        if(n % 5 == 0) a4 = dfs(n / 5);
        if(n % 3 == 0) a3 = dfs(n / 3);
        if(n % 2 == 0) a1 = dfs(n / 2);
        a2 = dfs(n - 1);
        return d[n] = Math.min(Math.min(a1, a2), Math.min(a3, a4)) + 1;
    }

    public static void main(String[] args) {
        int x = 30000;
        System.out.println(dfs(x));

        int[] d2 = new int[30001];
        for(int i = 2; i <= x; ++i){
            d2[i] = d2[i - 1] + 1;
            if(i % 2 == 0) d2[i] = Math.min(d2[i], d2[(int) i / 2] + 1);
            if(i % 3 == 0) d2[i] = Math.min(d2[i], d2[(int) i / 3] + 1);
            if(i % 5 == 0) d2[i] = Math.min(d2[i], d2[(int) i / 5] + 1);
        }

        System.out.println(d2[x]);
    }
}
