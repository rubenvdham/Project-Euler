import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class euler036 {


    static boolean isPalindrome(Integer source){
        String decimal = Integer.toString(source);
        String binary = Integer.toBinaryString(source);

        if (checkPalindrome(decimal) && checkPalindrome(binary)){
            return true;
        }
        return false;
    }

    static boolean checkPalindrome(String number){
        String reverse = new StringBuilder(number).reverse().toString();
        if (reverse.equals(number)){
            return true;
        }
        return false;
    }




    public static void main(String[] args){
        List<Integer> palindromes = new ArrayList<Integer>();
        IntStream
                .range(0,1000000)
                .forEach(p-> {
                    if (isPalindrome(p)) {
                        palindromes.add(p);
                    }
                });
        Long sum = palindromes.stream().mapToLong(Integer::longValue).sum();
        System.out.println(sum);


    }

}
