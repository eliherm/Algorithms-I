package lab2;

import java.util.Stack;

public class TravelPlanner {
	
	private int numCities;		// The number of cities in the graph
	private int source;
	private int destination;
	private int currentTime;	// The arrival time of the previous flight	
	private int currentCity;	
	private int[] cost;			
	private int[] predecessor;
	
	public TravelPlanner() {
		// Check if no arguments were passed
		System.out.println("Error: No graph was passed");
		System.exit(1);
	}
	
	public TravelPlanner(int[][] edges, int numCities, int source, int destination) {
		this.numCities = numCities;
		this.source = source;
		this.destination = destination;
		currentTime = 0;
		currentCity = 0;
		cost = new int[numCities];
		predecessor = new int[numCities];
		
		findPaths(edges); // Find the best route to the destination
	}
		
	private void findPaths(int[][] edges) {
		boolean[] reached = new boolean[numCities]; // Holds the reached status for each city
		
		// Initialize the source city
		currentCity = source;
		cost[source] = 0;
		currentTime = -1;
		reached[source] = true;
		
		// Initialize the other cities as not reached
		for (int i = 0; i < numCities; i++) {
			if (i != source) {
				reached[i] = false;
			}
		}
		
		while(true) {
			int iterator = 0;
			int leastArrival = Integer.MAX_VALUE;
			int nextCity = 0;
			
			// Find the current city within the edge array
			while(edges[iterator][0] != currentCity) {
				iterator ++;
			}
			
			// Select the best edge from the edge array
			while (edges[iterator][0] == currentCity) {
				// 1) Check if the departure time of the flight is greater than the previous arrival time
				// 2) Check if the arrival time is the lowest among the selected city
				// 3) Check if the the destination of the edge has not been reached
				if ((edges[iterator][2] > currentTime) && (edges[iterator][3] < leastArrival) && (reached[edges[iterator][1]] == false)) {
					nextCity = edges[iterator][1];
					leastArrival = edges[iterator][3];
				}
				
				// Check for the end of the edge array
				if (iterator == 13) {
					break;
				}
				
				iterator++;
			}
			
			// Update the city as reached
			reached[currentCity] = true;
			cost[nextCity] = leastArrival;
			predecessor[nextCity] = currentCity;
			
			// Move to the next city
			currentCity = nextCity;
			currentTime = leastArrival;
			
			if (currentCity == destination) {
				break;
			}
		}
	}
	
	// Prints the flight route to the destination city
	private String getRoute() {
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(destination);
		
		int index = destination;
		while(predecessor[index] != source) {
			stack.push(predecessor[index]);
			index = predecessor[index];
		}
		stack.push(source);
		
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
		
		output = "Optimal route from " + destination + " to " + source + "\n";
		
		int headingLength = output.length() - 1;
		for (int i = 0; i < headingLength; i++) {
			output += "-";
		}
		
		output += "\n\nFlight path: " + getRoute() + "\n";
		output += "Arrival time at " + destination + ": " + cost[destination]; 
		return output;
	}

	public static void main(String[] args) {
		
		int[][] testData = { 
				 {0, 1, 1, 2},
				 {0, 1, 3, 6},
				 {0, 2, 2, 8},
				 {0, 3, 4, 8},
				 
				 {1, 2, 7, 9},
				 {1, 3, 3, 4},
				 
				 {2, 0, 1, 2},
				 {2, 1, 2, 4},
				 {2, 3, 1, 4},
				 {2, 3 ,7 ,8},
				 
				 {3, 0, 1, 3},
				 {3, 0, 6, 8},
				 {3, 1, 2, 4},
				 {3, 2, 5, 6} };
		
		TravelPlanner graph = new TravelPlanner(testData, 4, 0, 2);
		System.out.println(graph.toString());
	}
	
}
