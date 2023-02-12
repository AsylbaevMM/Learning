package org.example;

import javax.imageio.metadata.IIOMetadataFormatImpl;
import java.util.LinkedList;

public class Person {
    private String name;
    private int age;
    private LinkedList<Person> parents = new LinkedList<>();

    private LinkedList<Person> childs = new LinkedList<>();
    private Person husband;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public String getName() {
        return name;
    }
    public void isParent(Person name){
        childs.add(name);
    }

    public void isChild(Person name){
        parents.add(name);
    }

    public void showChildrens() {
        System.out.print(name+"'s childs is: ");

        for (int i = 0; i < childs.size(); i++) {
            System.out.print(childs.get(i).getName());
        }
        System.out.println();
    }

    public void showParents(){
        System.out.println(parents);
    }







}
