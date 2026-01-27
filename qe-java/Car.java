package com.example;

public class Car {
    String color;
    String transmission;
    int make;
    int tyres;
    int doors;
    Car(int tyres, int doors){
        this.tyres = tyres;
        this.doors = doors;
    }
    void displayCharacteristics(){
        System.out.println(color+" "+tyres+" "+doors);
    }
    void accelerate(){
        System.out.println("Car is moving");;
    }
    void brake(){
        System.out.println("Car has stopped");
    }

}
