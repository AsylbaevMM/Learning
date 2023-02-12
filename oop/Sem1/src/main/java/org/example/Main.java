package org.example;

public class Main {
    public static void main(String[] args) {
        Person vasya = new Person("Vasya", 25);
        Person dima = new Person("Dima", 3);

        Relationships vasyaDima = new Relationships();
        vasyaDima.makeParent(vasya, dima);

        vasya.showChildrens();
        dima.showParents();
    }


}