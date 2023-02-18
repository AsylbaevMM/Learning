package org.example;

public class Main {
    public static void main(String[] args) {
        Relationships event = new Relationships();
        event.newPerson("Vasya", "male");
        event.newPerson("Masha", "female");
        event.newPerson("Zahar", "male");
        event.newPerson("Dima", "male");

        event.wedding(Relationships.persons.get("Vasya"), Relationships.persons.get("Masha"));
        event.birth(Relationships.persons.get("Zahar"), Relationships.persons.get("Vasya"));
        event.birth(Relationships.persons.get("Vasya"), Relationships.persons.get("Dima"));
        System.out.println("Vasya's husband is " + event.persons.get("Vasya").getHusband().getName());
        event.showParents("Dima");
        event.showChildren("Zahar");
    }
}