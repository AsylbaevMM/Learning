package org.example;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Task implements Comparable<Task>{
    int id;
    String name;

    String description;

    Date created;

    Date deadline;

    Integer priority;

    String author;

    // конструктор интерактивен, запрашивает описание и количество дней на выполнение задачи
    public Task(String name, String author, Integer  id, int priority, String description, Date deadline) {
        this.name = name;
        this.author = author;
        this.id = id;
        this.priority = priority;
        this.created = new Date();
        this.description = description;
        this.deadline = deadline;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public Date getCreated() {
        return created;
    }

    public Date getDeadline() {
        return deadline;
    }

    public int getPriority() {
        return priority;
    }

    public String getAuthor() {
        return author;
    }

    @Override
    public String toString() {
        return "Task{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", created=" + created +
                ", deadline=" + deadline +
                ", priority=" + priority +
                ", author='" + author + '\'' +
                "}";
    }

    @Override
    public int compareTo(Task o) {
        if (this.getPriority() < o.getPriority()){
            return - 1;
        } else if (this.getPriority() < o.getPriority()) {
            return 0;
        }else{return 1;}
    }

}
