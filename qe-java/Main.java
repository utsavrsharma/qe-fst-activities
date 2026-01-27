
package com.example;

public class Main {
    public static void main(String[] args) {
        Car jaguar = new Car(4,2);
        jaguar.make = 2014;
        jaguar.color = "Black";
        jaguar.transmission = "Manual";
        jaguar.displayCharacteristics();
        jaguar.accelerate();
        jaguar.brake();

    }
}