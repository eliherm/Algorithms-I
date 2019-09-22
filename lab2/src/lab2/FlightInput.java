/**
 * Name: Elikem Hermon
 * Student Number: 20075527
 * I certify that this submission contains my own work, except as noted.
 */

package lab2;

import java.io.*;
import java.util.Scanner;

public class FlightInput {

	private int numEdges;
	private int numCities;
	private int[][] data;
	private int[] cityIndex; // Stores indexes for cities
	
	public FlightInput() {
		// Check if a file was provided
		System.out.println("No file was provided");
		System.exit(1);
	}
	
	public FlightInput(String filepath) {
		try {
			File file = new File(filepath);
			Scanner fileScanner = new Scanner(file);
			
			// Read the number of cities from the first line and increment the scanner
			numCities = fileScanner.nextInt();
			fileScanner.nextLine();
			cityIndex = new int[numCities];
			
			String curCity = "";
			int prevCity = -1;
			int cityIdx = 0;

			// Read the number of edges in the graph
			numEdges = 0;
			while (fileScanner.hasNextLine()) {
				curCity = fileScanner.nextLine();
				curCity = curCity.split("\t")[0];
								
				if (prevCity != Integer.parseInt(curCity)) {
					cityIndex[cityIdx++] = numEdges;
					prevCity = Integer.parseInt(curCity);
				}
				
				numEdges++;
			}
			
			// Reset the scanner to read from the beginning of the file
			fileScanner.close();
			fileScanner = new Scanner(file);
			fileScanner.nextInt(); // Ignore the first line
			
			data = new int[numEdges][4];
			for (int i = 0; i < numEdges; i++) {
				for (int j = 0; j < 4; j++) {
					data[i][j] = fileScanner.nextInt();
				}
			}
			fileScanner.close();
		} catch (FileNotFoundException e) {
			System.out.println("The specified file was not found!");
			System.exit(1);
		}
	}
	
	public int getNumEdges() {
		return numEdges;
	}
	
	public int[] getIndex() {
		return cityIndex.clone();
	}
	
	public int getNumCities() {
		return numCities;
	}
	
	public int[][] getEdges() {
		return data.clone();
	}
	
	public static void main(String[] args) {
		FlightInput data = new FlightInput("/Users/Elikem/Coding-Courses/cmpe365/lab2/data/2019_Lab_2_flights_real_data.txt");
		TravelPlanner graph = new TravelPlanner(data.getEdges(), data.getIndex(), data.getNumCities(), data.getNumEdges(), 27, 55);
				
		try {
			// Save output to a file
			PrintWriter graphOutput = new PrintWriter("20075527-output.txt");
			graphOutput.println(graph);
			graphOutput.close();
		} catch (FileNotFoundException e) {
			System.out.println("The output file could not be saved!");
			System.exit(1);
		}
		
		System.out.println(graph);
	}

}
