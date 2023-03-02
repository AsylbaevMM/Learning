package org.example;

public class CalculateRatio implements Calculate<Ratio>{
    @Override
    public Ratio sum(Ratio a, Ratio b) {
        return new Ratio(a.real + b.real);
    }

    @Override
    public Ratio dif(Ratio a, Ratio b) {
        return new Ratio(a.real - b.real);
    }

    @Override
    public Ratio mul(Ratio a, Ratio b) {
        return new Ratio(a.real * b.real);
    }

    @Override
    public Ratio div(Ratio a, Ratio b) {
        return new Ratio(a.real / b.real);
    }
}
