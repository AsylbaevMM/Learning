package org.example;

public class Main {
    public static void main(String[] args) {
        Relationships event = new Relationships();
        event.newPerson("Vasya", "male");
        event.newPerson("Masha", "female");
        event.newPerson("Zahar", "male");
        event.newPerson("Dima", "male");

        event.wedding("Vasya", "Masha");
        event.birth("Zahar", "Vasya");
        event.birth("Vasya", "Dima");
        System.out.println("Vasya's husband is " + event.persons.get("Vasya").getHusband().getName());
        event.showParents("Dima");
        event.showChildren("Zahar");
    }
}