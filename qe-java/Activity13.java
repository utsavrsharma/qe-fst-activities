package com.example;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;

public class Activity13 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        Random indexGen = new Random();

        System.out.println("Enter integers (type a non-integer or letter to finish):");

        while (scan.hasNextInt()) {
            list.add(scan.nextInt());
        }

        if (list.isEmpty()) {
            System.out.println("No numbers were entered.");
        } else {
            Integer nums[] = list.toArray(new Integer[0]);

            int randomIndex = indexGen.nextInt(nums.length);

            System.out.println("--- Results ---");
            System.out.println("Generated Index: " + randomIndex);
            System.out.println("Value at this index: " + nums[randomIndex]);
        }
        
        scan.close();
    }
}