/**
 * Name: Elikem Hermon
 * Student Number: 20075527
 * I certify that this submission contains my own work, except as noted.
 */

package lab2;

import java.util.Stack;

public class TravelPlanner {
	
	private int numCities;
	private int numEdges;
	private int source;
	private int destination;
	private int[] cost;			
	private int[] predecessor;
	
	public TravelPlanner() {
		// Check if no arguments were passed
		System.out.println("Error: No graph was passed");
		System.exit(1);
	}
	
	public TravelPlanner(int[][] edges, int[] cityIndex, int numCities, int numEdges, int source, int destination) {
		this.numCities = numCities;
		this.numEdges = numEdges;
		this.source = source;
		this.destination = destination;
		cost = new int[numCities];
		predecessor = new int[numCities];
		
		findPaths(edges, cityIndex);
	}
		
	private void findPaths(int[][] edges, int[] cityIndex) {
		// Check for invalid cities
		if ((source > numCities - 1) || (destination > numCities - 1)) {
			System.out.println("Error: Invalid city");
			System.exit(1);
		}
		
		int[] estimate = new int[numCities];
		boolean[] candidate = new boolean[numCities];
		boolean[] reached = new boolean[numCities];
		int currentTime; // The arrival time of the previous flight	
		
		// Initialize the source city
		cost[source] = 0;
		estimate[source] = 0;
		reached[source] = true;
		candidate[source] = false;
		predecessor[source] = -1;
		currentTime = -1;
		
		// Initialize the other cities as not reached
		for (int i = 0; i < numCities; i++) {
			if (i != source) {
				estimate[i] = Integer.MAX_VALUE;
				reached[i] = false;
				candidate[i] = false;
			}
		}
		
		// Update the estimates of the neighbours
		int iterator = cityIndex[source];
		while (edges[iterator][0] == source) {
			// Check if the arrival time is less than the estimate
			if (edges[iterator][3] < estimate[edges[iterator][1]]) { 
				estimate[edges[iterator][1]] = edges[iterator][3];
				candidate[edges[iterator][1]] = true;
				predecessor[edges[iterator][1]] = source;
			}
			
			// Check for the end of the edge array
			if (iterator == (numEdges - 1))
				break;
			
			iterator++;
		}
		
		while (true) {
			int leastArrival = Integer.MAX_VALUE;
			int nextCity = -1;
			
			// Finding the candidate with the lowest estimate
			for (int i = 0; i < numCities; i++) {
				if ((candidate[i] == true) && (estimate[i] < leastArrival)) {
					nextCity = i;
					leastArrival = estimate[i];
				}
			}
						
			// Update the city as reached
			reached[nextCity] = true;
			candidate[nextCity] = false;
			cost[nextCity] = leastArrival;
			currentTime = leastArrival;
			
			// Check if the destination has been reached
			if (reached[destination] == true) {
				break;
			}
									
			// Update the neighbours
			iterator = cityIndex[nextCity];
			while (edges[iterator][0] == nextCity) {
				// 1) Check if the the destination of the edge has not been reached
				// 2) Check if the departure time of the flight is greater than the previous arrival time
				// 2) Check if the arrival time is the less than the estimate
				if (reached[edges[iterator][1]] == false) {
					if ((edges[iterator][3] < estimate[edges[iterator][1]]) && (edges[iterator][2] > currentTime)) {
						estimate[edges[iterator][1]] = edges[iterator][3];
						candidate[edges[iterator][1]] = true;
						predecessor[edges[iterator][1]] = nextCity;
					}
				}
				
				if (iterator == (numEdges - 1))
					break;
				
				iterator++;
			}
		}
	}
	
	// Prints the flight route to the destination city
	private String getRoute() {
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(destination);
		
		int index = destination;
		while(predecessor[index] != -1) {
			stack.push(predecessor[index]);
			index = predecessor[index];
		}
		
		String route = "";
		while (stack.size() > 0) {
			route += (stack.pop());
			if (stack.size() != 0) {	// Formats the last route
				route += " -> ";
			}
		}
		return route;
	}
	
	// Formats the output string for the journey
	public String toString() {
		String output;
		output = "Optimal route from " + source + " to " + destination + "\n";
		
		int headingLength = output.length() - 1;
		for (int i = 0; i < headingLength; i++) {
			output += "-";
		}
		
		output += "\n\nFlight path: " + getRoute() + "\n";
		output += "Arrival time at city " + destination + ": " + cost[destination]; 
		return output;
	}
	
}
