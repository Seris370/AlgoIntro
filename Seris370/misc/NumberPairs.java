import java.util.Arrays;
import java.util.Scanner;

public class NumberPairs {

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] segs = input.split(";");
        int sum = Integer.parseInt(segs[1]);
        String[] strs = segs[0].split(",");
        int[] arr = new int[strs.length];
        for (int i = 0; i < strs.length; i++) {
            arr[i] = Integer.parseInt(strs[i]);
        }
        getPairs(arr, sum);
    }

    // Prints number of pairs in arr[0..n-1] with sum equal
    // to 'sum'
    public static void getPairs(int[] arr, int sum)
    {
        StringBuilder result = new StringBuilder();
        int pos = Math.min(Math.abs(Arrays.binarySearch(arr, sum)), arr.length - 1);
        int i = 0;
        int j = pos;
        boolean flag = false;
        while (i < pos) {
            if (arr[i] > sum/2) {
                break;
            }
            if (arr[i] + arr[j] == sum) {
                if (flag) {
                    result.append(";");
                }
                result.append(arr[i] + "," + arr[j]);
                flag = true;
                j--;
                i++;
            } else if (arr[i] + arr[j] > sum) {
                j--;
            } else if (arr[i] + arr[j] < sum) {
                i++;
            }
        }
        if (flag) {
            System.out.println(result);
        } else {
            System.out.println("NULL");
        }
    }
}
