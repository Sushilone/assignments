// Write a program to find all the prime numbers from 1 to N.


// Input:
// Enter n: 10

// Output:
// Prime numbers: 
// 1 2 3 5 7 

import java.util.Scanner;
import java.util.ArrayList;

public class Solution6 {

    public static void main(String[] args) {
       
       Scanner scn = new Scanner(System.in);
       System.out.print("Enter n: ");
       int n = scn.nextInt();

       ArrayList<Integer> nums = new ArrayList<Integer>();
       for(int i = 1; i <= n; i++) {
            nums.add(i);
       }

       for(int i=1; i<nums.size(); i++) {
            if(nums.get(i)==0) {
                continue;
            }
            for(int j=i+1; j<nums.size(); j++) {
                if(nums.get(j)==0) {
                    continue;
                }
                else if(nums.get(j) % nums.get(i) == 0) {
                    nums.set(j,0);
                }
            }
       }

       System.out.println("Prime numbers: ");
       for(int v:nums) {
            if(v > 0) {
                System.out.print(v+" ");
            }
       }

    }
}