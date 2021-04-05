class Solution {
    public int solution(int[] gift_cards, int[] wants) {
        int answer = 0;
        int[] gift_counts = new int[100001];
        int[] want_counts = new int[100001];
        for (int i = 0; i < 100001; i++) {
            gift_counts[i] = 0;
            want_counts[i] = 0;
        }
        for (int card : gift_cards) {
            gift_counts[card] += 1;
        }
        for (int want : wants) {
            want_counts[want] += 1;
        }
        for (int i = 0; i < 100001; i++) {
            int count = gift_counts[i] - want_counts[i];
            if (count > 0) {
                answer += count;
            }
        }

        return answer;
    }
}