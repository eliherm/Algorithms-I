package algorithm;

import java.io.*;
import java.util.Scanner;

public class TestCase {
	
	private int dimension;
	private int[][] data;
	
	public TestCase() {
		System.out.println("No file was provided");
		System.exit(1);
	}
	
	public TestCase(String filepath) {
		try {
			File file = new File(filepath);
			Scanner fileScanner = new Scanner(file);
			
			dimension = fileScanner.nextInt();
			data = new int[dimension][dimension];
			
			for (int i = 0; i < dimension; i++) {
				for (int j = 0; j < dimension; j++) {
					data[i][j] = fileScanner.nextInt();
				}
			}
			fileScanner.close();
		} catch (FileNotFoundException e) {
			System.out.println("The specified file was not found!");
//			e.printStackTrace();
			System.exit(1);
		}
	}
	
	public int getDimension() {
		return dimension;
	}
	
	public int[][] getArray() {
		return data.clone();
	}
	
	public static void main(String[] args) {
		TestCase graphData = new TestCase("/Users/Elikem/Coding-Courses/cmpe365/lab1/data/data_200.txt");
		Dijkstra graph = new Dijkstra("Case " + graphData.getDimension(), graphData.getDimension(), graphData.getArray());
		System.out.println(graph.toString());
	}

}
