package org.example;

public class Complex extends Digit {

    public Complex(float real, float imagine) {
        super.real = real;
        super.imagine = imagine;
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
