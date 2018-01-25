/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?*/

public class euler5 {

    static int smallestDivisableBy(int maxDivider){
        int answer = 0;
        while (true){
            answer +=1;
            if (dividableBy(answer,maxDivider)){
                break;
            }
        }
        return answer;
    }


    static private boolean dividableBy(int number, int maxDivider){
        if (maxDivider <=0){
            return true;
        }
        if (number%maxDivider == 0) {
            return dividableBy(number, maxDivider - 1);
        }else{
            return false;
        }
    }
    public static void main(String[] args){
        System.out.println(smallestDivisableBy(20));

    }
}
