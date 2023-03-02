package org.example;

public class Ratio extends Digit{

    // Так как рациональные числа являются частным случаем комплексных, наследуем их от комплексных

    public Ratio(float real) {
        super.real = real;
    }



    @Override
    public String toString() {
        return Float.toString(real);
    }
}
