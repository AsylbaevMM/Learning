package org.example;

import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class TaskManager<ObjectMapper> {
    static HashMap<Integer, Task> taskList = new HashMap<>();

    public int lastID = 1;



    public void  addTask(String name, String author, int priority){   // Создает задачу с уникальным ID
        Task task = new Task(name, author, lastID, priority, TaskView.enterString(name), DeadlineMaker.createDL(name));
        taskList.put(lastID, task);
        lastID++;
        System.out.println("Task " + name+ " by " + author + " created!" );


    }

    public void saveData(){  // Записывает все задачи в файл tasks.json
        try (PrintWriter out = new PrintWriter("tasks.json")) {
            out.append(taskList.toString()+ "\n");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void showTasks(){  //Показывает задачи отсортировав по приоритету
        ArrayList<Task> val = new ArrayList<>(taskList.values());
        Collections.sort(val);
        for (int i = 0; i < val.size(); i++) {
            System.out.println(val.get(i));
        }
    }



    }
