package org.example;

import java.util.ArrayList;

public interface GenTree {

    void wedding(Person husband1, Person husband2) ;


    void birth(Person parent, Person child);

    void makeParent(Person parent, Person child);



    ArrayList getChildren(String name);

    void showChildren(String name);

    ArrayList getParents(String name);

    void showParents(String name);
}
