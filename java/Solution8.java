// Write a program to check whether an element is present in array or not.

// Output:
// Present!
public class Solution8 {

    public static void main(String[] args) {

        int[] nums = {1, 2, 3, 5, 7, 11, 13, 17, 19};
        int search = 11;

        for(int i:nums) {
            if(i == search) {
                System.out.println("Present!");
                return;
            }
        }
        System.out.println("Not present!");
    }
}