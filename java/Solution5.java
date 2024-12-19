// Write a program to add two binary strings.

// Output:

// Binary1: 10010
// Binary2: 11001
// Result is: 101011

public class Solution5 {

    public static void main(String[] args) {
        String s1 = "10010";
        String s2 = "11001";

        String res = "";

        int carry = 0;
        int i = s1.length()-1;
        int j = s2.length()-1;

        while(i>=0 || j>=0 || carry!=0) {
            int b1 = (i>=0) ? s1.charAt(i)-'0' : 0;
            int b2 = (j>=0) ? s2.charAt(j)-'0' : 0;

            int sum = b1 + b2 + carry;
            carry = sum/2;
            res += sum % 2;

            i--; j--;
        }
        
        String ans = "";
        for(int k=res.length()-1; k>=0; k--) {
            ans += res.charAt(k);
        }
        System.out.println("Binary1: "+s1);
        System.out.println("Binary2: "+s2);
        System.out.println("Result is: "+ans);
    }
}