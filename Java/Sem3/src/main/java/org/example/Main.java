package org.example;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        ex1();
    }


    private static void ex1() {
        ArrayList<Integer> list = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            list.add(random.nextInt(20));
        }
        System.out.println("Original list: " + list);
        Collections.sort(list);
        System.out.println("Sorted list: " + list);
    }

    private static void ex2() {

        List<String> names = List.of("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun");

        List<String> planets = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 30; i++) {
            planets.add(names.get(random.nextInt(8)));
        }
        System.out.println("Original list: " + planets);

        for (int i = 0; i < 8; i++) {
            int count = 0;
            for (int j = 0; j < 30; j++) {
                if (names.get(i).equals(planets.get(j))){
                    count++;
                }
            }
            System.out.println(names.get(i) + " = " + count );

        }

    }

    private static void ex3() {
        List<String> names = List.of("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun");

        List<String> planets = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 30; i++) {
            planets.add(names.get(random.nextInt(8)));
        }
        System.out.println("Original list: " + planets);

        for (int i = 0; i < 8; i++) {
            int count = 0;

            for (int j = 0; j < planets.size(); j++) {
                if (names.get(i).equals(planets.get(j)) && count < 1){
                    count++;
                    continue;
                }
                if (names.get(i).equals(planets.get(j)) && count == 1){
                    planets.remove(j);
                    j--;
                }
            }
            System.out.println(planets);

        }
        //System.out.println(planets);
    }
}



