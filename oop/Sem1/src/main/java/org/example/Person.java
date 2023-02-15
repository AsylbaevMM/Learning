package org.example;

import javax.imageio.metadata.IIOMetadataFormatImpl;
import javax.sound.midi.Soundbank;
import java.util.LinkedList;

public class Person extends Tree{
    private String name;
    private int age;

    private String sex;
    private LinkedList<Person> parents = new LinkedList<>();

    private LinkedList<Person> childs = new LinkedList<>();
    private Person husband;

    public Person(String name, int age, String sex ) {
        this.name = name;
        this.age = age;
        this.sex = sex;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public String getName() { return name; }
    public void isParent(Person name){
        childs.add(name);
    }

    public void isChild(Person name){
        parents.add(name);
    }

    public void isHusband(Person name) {this.husband = name; }

    public Person getHusband() {return husband;}

    public  String getSex() {return sex; }

    public LinkedList<Person> getParents() {return parents;}

    public LinkedList<Person> getChilds() {return childs;}

    public void showChildrens() {       //Метод для вывода имен всех детей
        System.out.print(name+"'s childs is: ");

        for (int i = 0; i < childs.size(); i++) {
            System.out.print(childs.get(i).getName());
            if (i < childs.size()-1){
            System.out.print(", ");
            }
        }
        System.out.println();
    }

    public void showParents(){       // Метод для вывода имен всех родителей
        System.out.print(name+"'s parents is: ");

        for (int i = 0; i < parents.size(); i++) {
            System.out.print(parents.get(i).getName());
            if (i< parents.size() -1 ){
                System.out.print(", ");
            }
        }
        System.out.println();
    }

    public void showGrandparents() {      //  Метод для вывода имен всех бабушек, дедушек
        System.out.print(name+"'s grandparents is: ");
        for (int i = 0; i < parents.size(); i++) {
            for (int j = 0; j < parents.get(i).getParents().size(); j++) {
                System.out.print(parents.get(i).getParents().get(j).getName());
                if (i < parents.size() - 1 || j < parents.get(i).getParents().size()-1) {
                    System.out.print(", ");
                }
            }
        }
        System.out.println();
    }

    public void showGrandchilds() {   // Метод для вывода имен всех внуков
        System.out.print(name + "'s grandchilds is: ");
        for (int i = 0; i < childs.size(); i++) {
            for (int j = 0; j < childs.get(i).getChilds().size(); j++) {
                System.out.print(childs.get(i).getChilds().get(j).getName());
                if (i < childs.size() - 1 || j < childs.get(i).getChilds().size()-1) {
                    System.out.print(", ");
                }
            }
        }
        System.out.println();
    }

    public void showBrothers() {        //Метод для вывода имен всех братьев и сестер
        LinkedList<Person> temp = new LinkedList<>();
        for (int i = 0; i < parents.size(); i++) {
            for (int j = 0; j < parents.get(i).getChilds().size(); j++) {
                if (this != parents.get(i).getChilds().get(j) && !temp.contains(parents.get(i).getChilds().get(j))){
                    temp.add(parents.get(i).getChilds().get(j));
                }
            }
        }
        System.out.print(name+"'s brothers and sisters are: ");
        for (int i = 0; i < temp.size(); i++) {
            System.out.print(temp.get(i).getName());
            if (i < temp.size()-1){
                System.out.print(", ");
            }
        }
        System.out.println();
    }

/*    public void showUncles() {    // Метод для вывода имен всех дяд и тёть
        LinkedList<Person> temp = new LinkedList<>();
        for (int i = 0; i < parents.size(); i++) {
            for (int j = 0; j < parents.get(i).getParents().size(); j++) {
                for (int k = 0; k < parents.get(i).getParents().get(j).getChilds().size(); k++) {
                    if (!temp.contains(parents.get(i).getParents().get(j).getChilds().get(k)) && !parents.contains(parents.get(i).getParents().get(j).getChilds().get(k))){
                        temp.add(parents.get(i).getParents().get(j).getChilds().get(k));
                        temp.add(parents.get(i).getParents().get(j).getChilds().get(k).getHusband());
                    }
                }
            }
        }
        System.out.print(name+"'s uncles are: ");
        for (int i = 0; i < temp.size(); i++) {
            System.out.print(temp.get(i).getName());
            if (i < temp.size()-1){
                System.out.print(", ");
            }
        }
        System.out.println();


    }*/







}
