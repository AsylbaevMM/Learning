package org.example;

public class Laptop {
    private String model;
    private int ram;
    private String color;
    private int memory;

    public Laptop(String model, int ram, String color, int memory) {
        this.model = model;
        this.ram = ram;
        this.color = color;
        this.memory = memory;
    }

    @Override
    public String toString() {
        return "Model: " + model + ", memory size: " + memory + ", RAM: " + ram + ", color: " + color;
    }

    public String getModel() {return model;}

    public int getRam() {return ram;}

    public void upgradeRam(int value){this.ram = value;}  //Метод для изменения значения оперативки

    public String getColor() {return color;}

    public int getMemory() {return memory;}

    public void upgradeMemory(int value){this.memory = value;} // Метод для изменения значения памяти

}
