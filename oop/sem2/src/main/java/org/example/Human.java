package org.example;

public class Human {

    private String name;
    private String gender;

    public Human(String name, String gender) {
        this.name = name;
        this.gender = gender;
    }

    @Override
    public String toString() {
        return "Human{" +
                "name='" + name + '\'' +
                ", gender='" + gender + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }

    public String getGender() {
        return gender;
    }


}
