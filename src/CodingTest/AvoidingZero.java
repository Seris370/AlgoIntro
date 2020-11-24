import java.util.*;
import java.util.stream.*;

public class AvoidingZero {
    static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(sc.nextLine());
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextInt();
            }
            solve(arr);
            sc.nextLine();
        }
    }

    static void solve(int[] lst) {
        int[] arr = Arrays.copyOf(lst, lst.length);
        IntStream positive = Arrays.stream(arr).filter(x -> x >= 0);
        int positiveSum = positive.sum();
        IntStream negative = Arrays.stream(arr).filter(x -> x < 0);
        int negativeSum = negative.sum();
        int sum = positiveSum + negativeSum;
        if (sum == 0) {
            System.out.println("NO");
        } else if (sum > 0) {
            System.out.println("YES");
            ArrayList<Integer> list = new ArrayList<>();
            Collections.addAll(list, positive.boxed().collect(Collectors.toList()));
            System.out.println(String.join(" ", ));
        } else {
            System.out.println("YES");
            Stream result = Stream.concat(negative.boxed(), positive.boxed());
            System.out.println(String.join(" ", result.collect(Collectors.toList())));
        }
    }
}
