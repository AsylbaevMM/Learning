package org.example;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class DeadlineMaker {
    public static Date createDL (String name) {
        System.out.println("How many days to deadline for " + name + "?");
        Scanner in = new Scanner(System.in);
        Calendar calendar = new GregorianCalendar();
        calendar.add(Calendar.DAY_OF_MONTH, in.nextInt());
        return  calendar.getTime();
    }
}
