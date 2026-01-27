package com.example;

import java.util.HashSet;

public class Activity10 {
    public static void main(String[] args) {
        HashSet<String> myList=new HashSet<>();
        myList.add("A");
        myList.add("B");
        myList.add("A");
        myList.add("D");
        myList.add("E");
        System.out.println(myList.size());
        System.out.println(myList.remove("D"));
        System.out.println(myList.remove("D"));
        if(myList.contains("A")){
            System.out.println(true);
        }
        System.out.println(myList);
    }
}
