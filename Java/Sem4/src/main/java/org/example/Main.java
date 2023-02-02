package org.example;

import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ex1();

    }
//    Реализовать консольное приложение, которое:
//    Принимает от пользователя строку вида
//    text~num
//    Нужно рассплитить строку по ~, сохранить text в связный список на позицию num.
//    Если введено print~num, выводит строку из позиции num в связном списке и удаляет её из списка.


    private static void ex1(){
        LinkedList<String> words = new LinkedList<>();

        Scanner input = new Scanner(System.in);
        while(true) {

            System.out.print("Input a string: ");
            String[] str = input.nextLine().split("~");

            if (str[0].equals("print")){
                try {
                    System.out.println(words.get(Integer.parseInt(str[1])));
                    continue;
                } catch (IndexOutOfBoundsException e)  {
                    System.out.println("Несуществующий индекс");
                    continue;
                }
            }

            if (str[0].equals("printall")){
                for (int i = 0; i < words.size(); i++) {
                    System.out.println(words.get(i));
                }
                continue;
            }

            if (str[0].equals("exit")){
                break;
            }

            if (str.length == 1 || Integer.parseInt(str[1]) < 0) {
                System.out.println("Некорректный ввод");
                continue;
            }


            if (str[0].equals("print")) {
               try {
                   System.out.println(words.get(Integer.parseInt(str[1])));
               } catch (IndexOutOfBoundsException e)  {
                   System.out.println("Несуществующий индекс"); 
               }
            } else if (str[0].equals("printall")) {
                for (int i = 0; i < words.size(); i++) {
                    System.out.println(words.get(i));
                }

                } else if (str[0].equals("exit") ){
                    break;
            } else{
                try {
                    words.remove(Integer.parseInt(str[1]));
                    words.add(Integer.parseInt(str[1]), str[0]);
                } catch (IndexOutOfBoundsException e) {
                    for (int i = words.size(); i < Integer.parseInt(str[1]) ; i++) {
                        words.add(null);
                    }
                    words.add(Integer.parseInt(str[1]), str[0]);
                }
            }

                
            }
        }
    }