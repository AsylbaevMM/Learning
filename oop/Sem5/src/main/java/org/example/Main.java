package org.example;

public class Main {
    public static void main(String[] args) {

        Calculate calculateComp = new CalculateComplex();
        Complex a = new Complex(5, 5);
        Complex b = new Complex(3, 6);


        System.out.println("Complex digits calculation:");
        System.out.println(calculateComp.sum(a,b).toString());
        System.out.println(calculateComp.dif(a,b).toString());
        System.out.println(calculateComp.mul(a,b).toString());
        System.out.println(calculateComp.div(a,b).toString());

        Calculate calculateRatio = new CalculateRatio();
        Ratio c = new Ratio(10);
        Ratio d = new Ratio(5);

        System.out.println("Rational digits calculation:");
        System.out.println(calculateRatio.sum(c,d).toString());
        System.out.println(calculateRatio.dif(c,d).toString());
        System.out.println(calculateRatio.mul(c,d).toString());
        System.out.println(calculateRatio.div(c,d).toString());


    }
}