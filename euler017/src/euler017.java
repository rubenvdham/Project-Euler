/*If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.*/


import java.util.List;

public class euler017 {

    static List threeLength = List.of(1,2,6,10);
    static List fourLength = List.of(4,5,9);
    static List fiveLength = List.of(3,8);

    static List.....


    static Integer singleLength(Integer n){
        Integer length = 0;
        if (threeLength.contains(n)){
            length+=3;
        }else if (fourLength.contains(n)){
            length+=4;
        } else if (fiveLength.contains(n)){
            length+=5;
        }else {
            length+=6;
        }
        return length;
    }

    static Integer getStringLengthOf(Integer n){
        Integer length = 0;
        int hundreds, tens,ones;
        if (n/100 > 0){
            hundreds = n/100;
            n+=singleLength(hundreds);
            n+=7;//because of "hundred"
            n = n/10;
            if (n%100 == 0){
                return length;
            }
        }
        if (n<=10){
            return length+singleLength(n);
        }
        if (n<=19){

        }
        if (n == 1000){
            return 11;//onethousand
        }
        return length;
    }
    static public void main(String[] args){
        Integer totalLength = 0;
        for (int i = 1;i<=1000;i++){
            totalLength+=getStringLengthOf(i);
        }
        System.out.println(totalLength);
    }
}
