package org.example;

public class Main {
    public static void main(String[] args) {
        Person.addPerson("Zakhar", 65, "male");
        Person.addPerson("Ludmila", 60, "female");
        Person.addPerson("Prohor", 90, "male");

        Person.addPerson("Vasya", 25, "male");
        Person.addPerson("Masha", 25, "female");
        Person.addPerson("Dima", 5, "male");
        Person.addPerson("Dasha", 3, "female");

        Person.addPerson("Lera", 30, "female");
        Person.addPerson("Vitya", 35, "male");
        Person.addPerson("Maks", 6, "male");
        Person.addPerson("Sonya", 4, "female");

        Relationships wedding = new Relationships();
        wedding.wedding(Person.getPersonList().get("Zakhar"), Person.getPersonList().get("Ludmila"));
        Relationships birth = new Relationships();
        birth.makeParent(Person.getPersonList().get("Zakhar"), Person.getPersonList().get("Vasya"));
        Person.getPersonList().get("Vasya").showParents();



    }


}