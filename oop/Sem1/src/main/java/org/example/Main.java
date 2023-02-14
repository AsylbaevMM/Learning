package org.example;

public class Main {
    public static void main(String[] args) {
        Person zakhar = new Person("Zakhar", 65, "male");
        Person ludmila = new Person("Ludmila", 60, "female");
        Person prohor = new Person("Prohor", 90, "male");

        Person vasya = new Person("Vasya", 25, "male");
        Person masha = new Person("Masha", 25, "female");
        Person dima = new Person("Dima", 5, "male");
        Person dasha = new Person("Dasha", 3, "female");

        Person lera = new Person("Lera", 30, "female");
        Person vitya = new Person("Vitya", 35, "male");
        Person maks = new Person("Maks", 6, "male");
        Person sonya = new Person("Sonya", 4, "female");

        Relationships wedding = new Relationships();
        wedding.wedding(zakhar, ludmila);
        wedding.wedding(lera, vitya);
        wedding.wedding(vasya, masha);
        Relationships birth = new Relationships();
        birth.makeParent(prohor, masha);
        birth.makeParent(zakhar, vasya);
        birth.makeParent(ludmila, vitya);
        birth.makeParent(vitya, maks);
        birth.makeParent(lera, sonya);
        birth.makeParent(vasya, dima);
        birth.makeParent(vasya, dasha);


        lera.showChildrens();
        sonya.showParents();
        sonya.showGrandparents();
        ludmila.showGrandchilds();
        dima.showBrothers();
        dima.showUncles();
    }


}