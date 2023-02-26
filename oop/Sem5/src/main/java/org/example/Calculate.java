package org.example;

public class Calculate {


    public Complex sum(Complex a, Complex b) {
        Complex result =  new Complex(a.real + b.real, a.imagine + b.imagine);
        Logger.log(a,b," + ", result);
        return result;
    }

    public Complex dif(Complex a, Complex b) {
        Complex result =  new Complex(a.real - b.real, a.imagine - b.imagine);
        Logger.log(a,b," - ", result);
        return result;
    }

    public Complex mul(Complex a, Complex b) {
        Complex result =  new Complex(a.real*b.real - a.imagine*b.imagine,
                a.imagine*b.real + a.real*b.imagine);
        Logger.log(a,b," * ", result);
        return result;
    }

    public Complex div(Complex a, Complex b) {
        Complex result =  new Complex((a.real*b.real + a.imagine*b.imagine)/(b.real*b.real + b.imagine*b.imagine),
                (a.imagine*b.real - a.real*b.imagine)/(b.real*b.real + b.imagine*b.imagine));
        Logger.log(a,b," / ", result);
        return result;
    }
}
