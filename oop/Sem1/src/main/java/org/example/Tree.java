package org.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

public abstract class Tree {
    private static HashMap<String, Person> personList = new HashMap();

    public static void addPerson(String name, int age, String sex) {
       personList.put(name,  new Person(name, age, sex));
    }

    public static HashMap<String, Person> getPersonList() {return personList; }
   public void showUncles() {    // Метод для вывода имен всех дяд и тёть
        LinkedList<Person> temp = new LinkedList<>();

        for (int i = 0; i < personList.size(); i++) {
            for (int j = 0; j < personList.get(i).getParents().size(); j++) {
                for (int k = 0; k < personList.get(i).getParents().get(j).getChilds().size(); k++) {
                    if (!temp.contains(personList.get(i).getParents().get(j).getChilds().get(k)) ){
                        temp.add(personList.get(i).getParents().get(j).getChilds().get(k));
                        temp.add(personList.get(i).getParents().get(j).getChilds().get(k).getHusband());
                    }
                }
            }
        }
        System.out.print(personList+"'s uncles are: ");
        for (int i = 0; i < temp.size(); i++) {
            System.out.print(temp.get(i).getName());
            if (i < temp.size()-1){
                System.out.print(", ");
            }
        }
        System.out.println();


    }

}
