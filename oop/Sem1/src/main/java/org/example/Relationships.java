package org.example;

public class Relationships {


    public void makeParent(Person parent, Person child){
        parent.isParent(child);
        child.isChild(parent);
    }
}
