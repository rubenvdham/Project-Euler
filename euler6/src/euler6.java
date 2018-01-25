/*The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.*/
public class euler6 {

    static int differenceSumSquares(int maxValue){
        int sumSquares = 0;
        int squareSum = 0;
        for (int i = 1; i<=maxValue;i++){
            sumSquares+= Math.pow(i,2);
        }
        int sum = 0;
        for (int i = 1; i<=maxValue;i++){
            sum+=i;
        }
        squareSum = (int) Math.pow(sum,2);
        return squareSum - sumSquares;
    }



    public static void main(String[] args){
        System.out.println(differenceSumSquares(100));

    }
}
