// Write a program to illustrate the concept of Inheritance.

// Output:
// Id: 123
// Name: Sushil
// Role: Front-end

public class Solution7 {

    public static void main(String[] args) {

        WebDeveloper web = new WebDeveloper(123,"Sushil","Front-end");
        web.getWebDeveloper();
    }
}

class Employee {
    int id;
    String name;
    Employee(int id,String name) {
        this.id = id;
        this.name = name;
    }
}

class WebDeveloper extends Employee {
    String role;
    WebDeveloper(int id,String name,String role) {
        super(id,name);
        this.role = role;
    }
    void getWebDeveloper() {
        System.out.println("Id: "+this.id);
        System.out.println("Name: "+this.name);
        System.out.println("Role: "+this.role);
    }
}