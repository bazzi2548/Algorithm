import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    private static final int MAX = 100000001;
    private static boolean[] arr = new boolean[MAX];

    public static void main(String[] args) throws IOException {
        for (int i = 2; i * i < MAX; i++) {
            if (!arr[i]) {
                for (int j = 2 * i; j < MAX; j += i) {
                    arr[j] = true;
                }
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long answer = 1;
        var N = Long.parseLong(st.nextToken());
        for (int i = 2; i <= N; i++) {
            if (!arr[i]) {
                long cnt = 1;
                while (i * cnt <= N) {
                    cnt *= i;
                }
                answer = answer * cnt % 4294967296L;
            }
        }
        System.out.println(answer);
    }
}


