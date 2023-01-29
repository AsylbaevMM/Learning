package org.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        ex1();
        ex2();
    }

    private static void ex1() {
        ArrayList<Integer> list = new ArrayList<>();
        int size = 50;
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            list.add(random.nextInt(50));
        }
        System.out.println("Original list: " + list);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i)%2 == 0){
                list.remove(i);
                i--;
            }
        };
        System.out.println("Filtered list: " + list);
    }

    private static void ex2(){
        ArrayList<Integer> list = new ArrayList<>();
        int size = 20;
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            list.add(random.nextInt(20));
        }
        System.out.println("List: " + list);
        int total = 0;
        Collections.sort(list);
        for (int i = 0; i < list.size(); i++) {
            total += list.get(i);
        };
        System.out.println("Smallest: " + list.get(0));
        System.out.println("Largest: " + list.get(list.size()-1));
        System.out.println("Average: " + total/list.size());

    }

}