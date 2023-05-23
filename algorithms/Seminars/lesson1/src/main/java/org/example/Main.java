package org.example;

import java.util.Date;

public class Main {


    public static void main(String[] args) {
        for (int i = 10; i < 100; i+= 10) {


            Date start1 = new Date();
            fib1(i);
            Date stop1 = new Date();

            Date start2 = new Date();
            fib(i);
            Date stop2 = new Date();
            System.out.println("+++++"+ i);
            System.out.println(stop1.getTime() - start1.getTime());
            System.out.println(stop2.getTime() - start2.getTime());
        }
    }

    public static void fib1(int num){
        int first = 1;
        int second = 1;

        for (int i = 2; i < num ; i++) {

            int third = first + second;
            first = second;
            second = third;

        }
        System.out.println(second);
    }

    public static int fib(int n){

        if(n <=2 ){

            return 1;
        }
        else {
            return fib(n-1) + fib(n-2);
        }
    }
}