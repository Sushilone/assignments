// Write a program to show method overriding.

// Output: 

// I'm Employee.
// I'm Web Developer.
// I'm App Developer.

public class Solution4 {

    public static void main(String[] args) {
        
        Employee emp = new Employee();
        WebDeveloper web = new WebDeveloper();
        AppDeveloper app = new AppDeveloper();

        emp.getRole();
        web.getRole();
        app.getRole();

    }
}

class Employee {
    
    void getRole() {
        System.out.println("I'm Employee.");
    }
}

class WebDeveloper extends Employee {
    @Override
    void getRole() {
        System.out.println("I'm Web Developer.");
    }
}

class AppDeveloper extends Employee {
    @Override
    void getRole() {
        System.out.println("I'm App Developer.");
    }
}