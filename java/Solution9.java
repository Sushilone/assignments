// Write a program to demonstrate Arithmetic Exception.

// Input:
// Enter Nomenator: 5
// Enter Denomenator: 0

// Output:
// Your denomenator is 0!
// Ans is infinity!
// Process completed!

import java.util.Scanner;

public class Solution9 {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        
        try {
            System.out.print("Enter Nomenator: ");
            int n = scn.nextInt();
            System.out.print("Enter Denomenator: ");
            int d = scn.nextInt();

            int ans = n / d; // when d=0 gives Arithmetic Exception
            System.out.println("Ans is: "+ans);
        }
        catch(ArithmeticException e) {
            System.out.println("Your denomenator is 0!");
            System.out.println("Ans is infinity!");
        }
        catch(Exception e) {
            System.out.println("Something went wrong!");
        }
        finally {
            System.out.println("Process completed!");
        }
    }
}