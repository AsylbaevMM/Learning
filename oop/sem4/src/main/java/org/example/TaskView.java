package org.example;

import java.util.Scanner;

public class TaskView {
    public static String  enterString(String name){
        Scanner in = new Scanner(System.in);
        System.out.println("Input description for " + name + ":");

        return in.nextLine();


    }
}
