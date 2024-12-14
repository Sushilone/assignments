// Write a program to print any star pattern.

/*

Input:

Enter an integer value: 5

Output:

*
**
***
****
*****

 */

import java.util.Scanner;

public class Solution1 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer value: ");
        int n = scanner.nextInt();
        
        for(int i = 0; i < n; i++) {            
            for(int j = 0; j < i+1; j++) {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}