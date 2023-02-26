package org.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        TaskManager taskManager = new TaskManager();

        taskManager.addTask("First test", "Author name", 2);
        taskManager.addTask("Second test", "Author name", 0);

        taskManager.saveData();

        taskManager.showTasks();
    }
}