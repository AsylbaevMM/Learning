package org.example;

public class Person extends Human {

    private Person husband;

    public Person(String name, String gender) {
        super(name, gender);
    }

    public void setHusband(Person husband) {
        this.husband = husband;
    }

    public Person getHusband() {
        return husband;
    }





}
