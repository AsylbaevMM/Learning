package org.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //ex1();
        ex2();
    }
    private static void ex1() {
        Scanner in = new Scanner(System.in);
        System.out.print("Input string: ");
        String words = in.nextLine();

        StringBuilder check = new StringBuilder();
        for (int i = words.length()-1; i >= 0 ; i--) {
            check.append(words.charAt(i));
        }
        System.out.println(words.equalsIgnoreCase(check.toString()));
    }

    private static void ex2(){
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 100; i++) {
            result.append("TEST");
        }

        try(FileWriter writer = new FileWriter("100TEST.txt", false))
        {
            writer.write(result.toString());
            System.out.println("Success!");
        }
        catch (IOException ex) {
            System.out.println("Something goes wrong");
        }
    }
}