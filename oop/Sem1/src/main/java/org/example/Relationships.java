package org.example;

public class Relationships {


    public void makeParent(Person parent, Person child){  // метод для добавления связи Родитель - ребенок
        parent.isParent(child);
        child.isChild(parent);
        if (parent.getHusband() != null) {   // Если родитель женат/ замужем, связб автоматически добавляется супругу
            parent.getHusband().isParent(child);
            child.isChild(parent.getHusband());
        }
    }

    public void wedding(Person husband1, Person husband2){    // Метод создания связи между мужем и женой
        if (husband1.getSex().equalsIgnoreCase(husband2.getSex())) {   // Проверяем что бы были разнополыми
            System.out.println("Both of husbands is " + husband1.getSex() + ", they can't be married now.");
        } else {
            husband1.isHusband(husband2);
            husband2.isHusband(husband1);
            //System.out.println(husband1.getName() + " married " + husband2.getName() + ". Congratulations!");
        }
    }

}
