package org.example;

import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {


        Laptop HP_n5010 = new Laptop("HP n5010",8, "black", 512 );
        Laptop Lenovo_555 = new Laptop("Lenovo 555", 16, "white", 1024);
        Laptop Asus_nova = new Laptop("Asus nova", 4, "silver", 256);
        Laptop Sony_vaio = new Laptop("Sony_vaio", 32, "black", 1024);
        Laptop Huawei_D15 = new Laptop("Huawei D15", 16, "silver", 512);
        LinkedList<Laptop> allLaptops = new LinkedList<>();
        allLaptops.add(HP_n5010);
        allLaptops.add(Lenovo_555);
        allLaptops.add(Asus_nova);
        allLaptops.add(Sony_vaio);
        allLaptops.add(Huawei_D15);

        System.out.println("All laptops");
        showAllLaptops(allLaptops);
        System.out.println();
        System.out.println("Filter by white color");
        filterByColor(allLaptops, "silver");
        System.out.println();
        System.out.println("Filter by minimal RAM=16 and memory=256");
        filterByMinRamAndMemory(allLaptops, 16, 256);
    }
    public static void showAllLaptops(LinkedList list) {
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i).toString());
        }
    }

    public static void filterByColor(LinkedList<Laptop> list, String color){
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getColor().equals(color)) {
                System.out.println(list.get(i).toString());
            }
        }
    }

    public static void filterByMinRamAndMemory(LinkedList<Laptop> list, int ram, int memory){
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getRam() >= ram && list.get(i).getMemory() >= memory) {
                System.out.println(list.get(i).toString());
            }
        }
    }
}