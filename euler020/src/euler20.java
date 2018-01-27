import java.math.BigInteger;

/*n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!*/
public class euler20 {


    static int sumOfDigitsOfFactorial(int factorial){
        BigInteger result = BigInteger.valueOf(1);
        int sumOfDigits= 0;
        for (int i = factorial;i>=1;i--){
            result = result.multiply(BigInteger.valueOf(i));
        }
        System.out.println(result);
        //String digitString = Long.toString(result);
        long remainder;
        while (!result.equals(BigInteger.valueOf(0))){

            remainder = result.mod(BigInteger.valueOf(10)).longValue();
            System.out.printf("%d",remainder);
            sumOfDigits+=remainder;
            result = result.divide(BigInteger.valueOf(10));
        }
        return sumOfDigits;
    }






    public static void main(String[] argv){
        long startTime = System.currentTimeMillis();
        int result = sumOfDigitsOfFactorial(100);
        System.out.printf("\n\nSum of the factorials digits: %d ",result);
        System.out.printf("\nRuntime: %d ms",(System.currentTimeMillis() - startTime));
    }
}
