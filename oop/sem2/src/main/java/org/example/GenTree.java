package org.example;

import java.util.ArrayList;

public interface GenTree {

    void wedding(String husband1, String husband2) ;


    void birth(String parent, String child);

    void makeParent(Person parent, Person child);

    ArrayList getChildren(String name);

    void showChildren(String name);

    ArrayList getParents(String name);

    void showParents(String name);

}
