package org.example;

public class Complex {
    float real;
    float imagine;

    public Complex(float real) {  // Конструктор с дефолтной нулевой мнимой частью для наследования рациональными числами
        this.real = real;
        this.imagine = 0;
    }
    public Complex(float real, float imagine) {
        this.real = real;
        this.imagine = imagine;
    }

    public float getReal() {
        return real;
    }

    public float getImagine() {
        return imagine;
    }

    @Override
    public String toString() {
        if (real != 0){
            if (imagine > 0) {
              return real + "+" + imagine + "i";
            } else if (imagine < 0) {
               return real + "-" + Math.abs(imagine) + "i";
            }else{
              return Float.toString(real);
            }
        }else{
            if (imagine != 0) {
                return imagine + "i";
            } else{
                return "0";
            }
        }

    }
}
