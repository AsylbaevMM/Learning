package org.example;


import java.io.*;
import java.sql.SQLOutput;


public class Main {
    // В этом задании не хватало переменной intArray
    public static void main(String[] args) {
        int[] intArray = new int[]{1,2,3,4,5,6,7,8,9};
        try {
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }

    }
    
}