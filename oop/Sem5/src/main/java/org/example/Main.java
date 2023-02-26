package org.example;

public class Main {
    public static void main(String[] args) {

        Calculate calculate = new Calculate();
        Complex a = new Complex(5, 5);
        Complex b = new Complex(3, 6);


        System.out.println("Complex digits calculation:");
        System.out.println(calculate.sum(a,b).toString());
        System.out.println(calculate.dif(a,b).toString());
        System.out.println(calculate.mul(a,b).toString());
        System.out.println(calculate.div(a,b).toString());


        Ratio c = new Ratio(10);
        Ratio d = new Ratio(5);

        System.out.println("Rational digits calculation:");
        System.out.println(calculate.sum(c,d).toString());
        System.out.println(calculate.dif(c,d).toString());
        System.out.println(calculate.mul(c,d).toString());
        System.out.println(calculate.div(c,d).toString());

        System.out.println("Mixed Calculation:");
        System.out.println(calculate.sum(b,a).toString());
        System.out.println(calculate.dif(a,d).toString());
        System.out.println(calculate.mul(c,b).toString());
        System.out.println(calculate.div(a,a).toString());
    }
}