package com.company;

import net.sourceforge.jFuzzyLogic.FIS;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Farshid Nooshi
 */
public class Main {
    public static void main(String[] args) throws Exception {
        // Load from 'FCL' file
        String[] results = {"cloud_computing", "crypto_network_secu", "Emb_process", "IOT", "ML"};
        ArrayList<FIS> fisArrayList = new ArrayList<>();
        for (var item : results) {
            FIS fis = FIS.load("controller/" + item + ".fcl", true);
            if( fis == null ) {
                System.err.println("Can't load file: '"
                        + item + "'");
                return;
            }
            fisArrayList.add(fis);
        }

        for ( var item : fisArrayList) {
            // Set inputs
            item.setVariable("Maths", 8);
            item.setVariable("Coding", 7);
            item.setVariable("Networking", 4);
            item.setVariable("Embedded", 8);
            item.setVariable("DataBase", 5);
            item.evaluate();
            System.out.println(item.getVariable("output1"));

            System.out.println(item);

        }
        var scanner = new Scanner(System.in);
        String[] arr = {"Maths", "Coding", "Networking", "Embedded", "DataBase"};
        while(true) {
            System.out.println("please enter the scores:");
            for (var item : arr) {
                System.out.printf("please enter %S skills from 1 to 10:\t", item);
                var inp = scanner.nextInt();
                for (var fisItem : fisArrayList) {
                    fisItem.setVariable(item, inp);
                }
            }

            for (int i = 0; i < 5; i++) {
                var fisItem = fisArrayList.get(i);
                var item = results[i];
                System.out.println(item + ":");
                fisItem.evaluate();
                System.out.println(fisItem.getVariable("output1"));
            }

        }
    }
}