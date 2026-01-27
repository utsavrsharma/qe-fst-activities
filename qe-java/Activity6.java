package com.example;


import java.util.ArrayList;
import java.util.Date;

class Plane {
    private int maxPassengers;
    private ArrayList<String> passengers;
    private Date lastTimeLanded;
    public Plane(int maxPassengers) {
        this.maxPassengers = maxPassengers;
        this.passengers = new ArrayList<>();
        this.lastTimeLanded = null;
    }
    public void onboard(String passenger) {
        if (passengers.size() < maxPassengers) {
            passengers.add(passenger);
        } else {
            System.out.println("Plane is full. Cannot add " + passenger);
        }
    }
    public Date takeOff() {
        return new Date();
    }
    public void land() {
        lastTimeLanded = new Date();
        passengers.clear();
    }
    public Date getLastTimeLanded() {
        return lastTimeLanded;
    }
    public ArrayList<String> getPassengers() {
        return passengers;
    }
}
public class Activity6 {
    public static void main(String[] args) {
        try {
            Plane plane = new Plane(10);

            // Onboard passengers
            plane.onboard("shivank");
            plane.onboard("azam bhai");
            plane.onboard("sharma ");
            plane.onboard("ediga bhai");
            System.out.println("Take-off time: " + plane.takeOff());
            System.out.println("Passengers on board: " + plane.getPassengers());
            Thread.sleep(5000);
            plane.land();
            System.out.println("Landing time: " + plane.getLastTimeLanded());
            System.out.println("Passengers after landing: " + plane.getPassengers());

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}