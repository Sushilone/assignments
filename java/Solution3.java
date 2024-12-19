// Write a program to show polymorphism.


//Output: 
/*

Calling sum 1
9
Calling sum 2
9.5

*/


public class Solution3 {

    public static void main(String[] args) {

        System.out.println(sum(4,5));
        System.out.println(sum(4.0,5.5));
    }

    static int sum(int a,int b) {
        System.out.println("Calling sum 1");
        return (a+b);
    }
    static double sum(double a,double b) {
        System.out.println("Calling sum 2");
        return (a+b);
    }
}