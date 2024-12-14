// Write a program to show the concept of class.

public class Solution2 {

    public static void main(String[] args) {

        Student std = new Student();
        std.setStudent("Sushil","BCA",3);
        std.getStudent();
    }
}

class Student {
    String name, course;
    int year;
    void setStudent(String name,String course,int year) {
        this.name = name;
        this.course = course;
        this.year = year;
    }
    void getStudent() {
        System.out.println("Name: "+name);
        System.out.println("Course: "+course);
        System.out.println("Year: "+year);
    }
    
}