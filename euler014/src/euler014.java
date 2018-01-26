public class euler014 {

    static long[] longest_collatz_chain(long maximum_start_term) {
        long max_terms = 1;
        long max_start_value = 1;
        long result;
        for (long i = 2; i < maximum_start_term; i++) {
            result = collatz_sequences_recursive(i);
            if (result > max_terms) {
                max_start_value = i;
                max_terms = result;
            }

        }
        long[] results = new long[2];
        results[0] = max_start_value;
        results[1] = max_terms;
        return results;
    }


    static long collatz_sequences_looped(long number){
        long terms = 0;
        long newNumber;
        while (true) {
            terms += 1;

            if (number <= 1) {
                break;
            } else {
                if (number % 2 == 0) {
                    number = number / 2;
                } else {
                    number = 3 * number + 1;
                }
            }
        }
        return terms;
    }



    static long collatz_sequences_recursive(long number) {
        long newNumber;
        if (number <= 1) {
            return 1;
        } else {
            if (number % 2 == 0) {
                newNumber = number / 2;
            } else {
                newNumber = 3 * number + 1;
            }
        }
        return 1 + collatz_sequences_recursive(newNumber);
    }


    public static void main(String[] argv){
        long startTime = System.currentTimeMillis();
        long[] results;
        results = longest_collatz_chain(1000000);
        System.out.printf("Number: %d generates the longest sequence of %d terms",results[0],results[1]);
        System.out.printf("\nRuntime: %d ms",(System.currentTimeMillis() - startTime));
    }
}
