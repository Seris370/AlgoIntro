import java.io.*;
import java.util.*;
import java.util.stream.Stream;

class Solution {

    // You may change this function parameters
    public static double maximumExpectedMoney(int n, int m, double[] p, double[] x, double[] y)  {
        // Participant's code will go here
        ArrayList<Double> ex = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            double expectation = p[i] * x[i] - (1.0 - p[i]) * y[i];
            if (expectation > 0) {
                ex.add(expectation);
            }
        }
        ex.sort(Collections.reverseOrder());
        double res = 0.0;
        for (int i = 0; i < Math.min(m, ex.size()); i++) {
            res += ex.get(i);
        }
        res = Math.round(res * 100);
        res /= 100;
        return res;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException  {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        double[] p = new double[n];
        double[] x = new double[n];
        double[] y = new double[n];
        double result = 0;

        //get input
        for(int i = 0; i < n; i++)
            p[i] = in.nextDouble();
        for(int i = 0; i < n; i++)
            x[i] = in.nextDouble();
        for(int i = 0; i < n; i++)
            y[i] = in.nextDouble();

        result = maximumExpectedMoney(n,m,p,x,y);

        // Do not remove below line
        System.out.println(String.format("%.2f", result));
        // Do not print anything after this line

        in.close();
    }
}