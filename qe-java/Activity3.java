package com.example;

public class Activity3 {


    public static void main(String[] args) {
        double seconds = 1000000000;
        double EarthSeconds = 31557600; 
        double MercurySeconds = 0.2488467;
        double VenusSeconds = 6.61519726;
        double MarsSeconds = 1.8888158;
        double JupiterSeconds = 11.862615;
        double SaturnSeconds = 29.447495;
        double UranusSeconds = 84016846;
        double NeptuneSeconds = 164.79132;
        System.out.println("Age on Earth: " + seconds/EarthSeconds);
        System.out.println("Age on Mercury: " + EarthSeconds/MercurySeconds);
        System.out.println("Age on Venus: " + EarthSeconds/VenusSeconds);
        System.out.println("Age on Mars: " + EarthSeconds/MarsSeconds);
        System.out.println("Age on Jupiter: " + EarthSeconds/JupiterSeconds);
        System.out.println("Age on Saturn: " + EarthSeconds/SaturnSeconds);
        System.out.println("Age on Uranus: " + EarthSeconds/UranusSeconds);
        System.out.println("Age on Neptune: " + EarthSeconds/NeptuneSeconds);
    }

}
