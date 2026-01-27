package com.example;

class CustomException extends Exception {
    private String message;

    public CustomException(String message) {
        this.message = message;
    }
    @Override
    public String getMessage() {
        return message;
    }
}

public class Activity8 {
    public static void exceptionTest(String str) throws CustomException {
        if (str == null) {
            throw new CustomException("Error: String value cannot be null!");
        } else {
            System.out.println("String is: " + str);
        }
    }

    public static void main(String[] args) {
        try {
            exceptionTest("Hello, world!");
            exceptionTest(null);
        } catch (CustomException e) {
            System.out.println(e.getMessage());
        }
    }
}