package org.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Date;

public class Logger {
    public static void log(Complex a, Complex b, String move, Complex result) {
        Date now  = new Date();
        try {
            FileWriter file = new FileWriter("log.txt", true);
            file.write(now + ": " + a.toString() + move + b.toString() + "=" + result.toString() + "\n");
            file.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
