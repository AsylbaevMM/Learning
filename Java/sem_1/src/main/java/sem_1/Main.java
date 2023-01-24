package sem_1;

import java.awt.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //ex1();
        //ex2();
        ex3();
    }

    private static void  ex1() {
        int[] arr = new int[50];
        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
           arr[i] = random.nextInt(100);
            //System.out.println(arr[i]);
        }
        int largest = arr[0];
        int smallest = arr[0];
        for (int num : arr){
            if (num > largest) {
                largest = num;
            }
            if (num < smallest){
                smallest = num;
            }
        }
        System.out.println("Largest = " + largest);
        System.out.println("Smallest = " + smallest);
    }

    private static void ex2(){
        System.out.println("Year?");
        Scanner in = new Scanner(System.in);
        int year = in.nextInt();
        Boolean result = year % 4 == 0 && year % 100 != 0 || year % 400 == 0;
        System.out.println(result);
    }

    private static void  ex3(){
        int[] arr = new int[10];
        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = random.nextInt(4);
        }
        System.out.println("Original array: " + Arrays.toString(arr));

        int left = 0;
        int right = arr.length - 1;
        while (left < right){
            if (arr[left] == 3 && arr[right] != 3){
                int temp = arr[right];
                arr[right] = arr[left];
                arr[left] = temp;
                left++;
            }
            if (arr[left] != 3) {
                left++;
            }
            if (arr[right] == 3){
                right--;
            }
        }
        System.out.println("Changed array: " + Arrays.toString(arr));
    }
}

