package com.example;

import java.util.ArrayList;

public class Activity9 {
    public static void main(String[] args) {
        ArrayList<String> myList=new ArrayList<>();
        myList.add("A");
        myList.add("B");
        myList.add("c");
        myList.add("D");
        myList.add("E");
        for(int i=0;i<myList.size();i++){
            System.out.println(myList.get(i));
        }
        System.out.println(myList.get(2));
        if(myList.contains("A")){
            System.out.println(true);
        }
        System.out.println(myList.size());
        myList.remove("A");
        System.out.println(myList.size());
    }
}