package org.example;

public class Ratio extends Complex{

    // Так как рациональные числа являются частным случаем комплексных, наследуем их от комплексных
    float real;
    public Ratio(float real) {
        super(real);
    }



    public float  getValue(){
        return real;
    }

    @Override
    public String toString() {
        return Float.toString(real);
    }
}
