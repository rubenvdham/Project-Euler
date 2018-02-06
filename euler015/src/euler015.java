/*Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?*/
public class euler015 {

    static long amountOfGridRoutes(int gridSize) {
        //gridSize+=1; //gridSize amount of edges, gridSize+=1 amount of vertices
        long k = 2*gridSize;
        long paths = 1;

        for (int i = 0; i < gridSize; i++) { //binominal
            paths *= k - i;
            paths /= i + 1;
        }
        return paths;
    }




    public static void main(String[] argv){
        long startTime = System.currentTimeMillis();
        long result = amountOfGridRoutes(20);
        System.out.printf("Amount of routes: %d",result);
        System.out.printf("\nRuntime: %d ms",(System.currentTimeMillis() - startTime));
    }
}