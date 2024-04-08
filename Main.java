import java.io.*;
import java.util.*;

public class Main implements Cloneable{

    static int sum = 0;


    //check whether the sodokus are solved or not
    public static boolean solvedOrNot (int[][] Grid){
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (Grid[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean checknumber(int r, int c, int n, int[][]Grid){
        //check if there has the same number for row
        for(int i = 0; i<9; i++) {
            if(Grid[r][i]==n){
                return false;
            }
        }

        //check if there has the same number for column
        for(int i = 0; i<9; i++){
            if(Grid[i][c] == n){
                return false;
            }
        }

        //check for 3x3
        int cr = (r/3)*3;
        int cc = (c/3)*3;
        for (r = cr; r<cr+3; r++){
            for(c = cc; c<cc+3; c++){
                if(Grid[r][c] == n){
                    return false;
                }
            }
        }

    return true;
    }

    /*public static boolean solution(int[][] Grid){
        for(int i = 0; i<9; i++){
            for(int j = 0; j<9; j++){
                if (Grid[i][j] == 0){
                    for(int n =1; n<=9 ;n++){
                        if(checknumber(i, j, n, Grid)){
                            Grid[i][j] = n;

                            if(solution(Grid)){
                                return true;
                            }
                            Grid[i][j] = 0;

                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }*/

    //use dfs to solve
    public static void DFS(Stack<int [][]> stack){
        while(!stack.isEmpty()){
            //get the current sudokus and return it
            int[][] cur = stack.pop();

            boolean emptyCell = false;

            for(int i = 0; i<9; i++){
                for(int j = 0; j<9; j++){
                    if (cur[i][j] == 0){
                        for(int n =1; n<=9 ;n++){
                            if(checknumber(i, j, n, cur)){
                                //input the number
                                cur[i][j] = n;
                                //if sudokus has been solved add up 3 digits number to the total
                                if(solvedOrNot(cur)){
                                    int tdn = cur[0][0]*100 + cur[0][1]*10 + cur[0][2];
                                    sum += tdn;
                                    return;
                                }
                                else{
                                    // make a copy of cur, so we don't change the original
                                    // if one of the branch is wrong, we can go back to one of the parent to go through new branches
                                    int[][] copy = new int[9][9];
                                    for(int z = 0; z < 9; z++){
                                        copy[z] = Arrays.copyOf(cur[z], 9);
                                    }
                                    stack.push(copy);
                                }
                            }
                        }
                        emptyCell = true;
                        break;
                    }
                    if(emptyCell){
                        break;
                    }
                }
            }
        }
    }



    public static void main(String[] args) throws IOException {
        //read the file as the day 1

        File file = new File("src/sudokus.txt");
        BufferedReader sdk;
        try {
            sdk = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        //Store the data into 2d array
        String sdk1 = sdk.readLine();
        int[][] sudokus = new int[9][9];
        int row = 0;
        boolean newGrid = false;
        while (sdk1 != null){
            if(sdk1.startsWith("Grid")){                //use this if every time, when we find a new "Grid", and print the previous one
                if(newGrid){
                    Stack<int[][]> stack = new Stack<>();
                    stack.push(sudokus);
                    DFS(stack);
                    sudokus = new int[9][9];
                    stack.clear();
                    //System.out.println(Arrays.deepToString(sudokus));
                }
                //System.out.println(sdk1);
                //make row 0, so we can refresh the array to next sudokus
                row = 0;
                newGrid = true;
            }
            else{
                for (int i = 0; i < 9; i++) {
                    sudokus[row][i] = Character.getNumericValue(sdk1.charAt(i));
                }
                row++;
            }
            sdk1 = sdk.readLine();
        }

        //when the new grid appear, deal with the new grid
        if(newGrid){
            Stack<int[][]> stack = new Stack<>();
            stack.push(sudokus);
            DFS(stack);
            sum += sudokus[0][0] * 100 + sudokus[0][1] * 10 + sudokus[0][2];
        }

        System.out.println("Sum is: " + sum);



        /*        for(int i = 1; i<9; i++){
                    sudokus[0][0]=i;
                    for(int j =1; j<9; j++){
                        if(sudokus[0][j]==i || sudokus[i][0]==i || sudokus[j][0]==i){
                            sudokus[0][0]=0;
                        }
                    }
                }
        System.out.println(Arrays.deepToString(sudokus));

       Try to print out all the txt content
        if(newGrid){
            System.out.println(Arrays.deepToString(sudokus));
        }*/










    }
}