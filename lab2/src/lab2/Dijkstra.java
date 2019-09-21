package lab2;

import java.util.Stack;

public class Dijkstra {
	
	private String name;
	private int numVertices; // Stores the number of vertices in the graph
	private int[] cost;
	private int[] predecessor;
	private int maxVertex;
	private int maxWeight;
	
	public Dijkstra() {
		name = "";
		numVertices = 0;
		cost = new int[numVertices];
		predecessor = new int[numVertices];
		maxVertex = 0;
		maxWeight = 0;
		
		findPaths(null);
	}
	
	public Dijkstra(String name, int numVertices, int[][] graph) {
		this.name = name;
		this.numVertices = numVertices;
		cost = new int[numVertices];
		predecessor = new int[numVertices];
		maxVertex = 0;
		maxWeight = 0;
		
		findPaths(graph);
	}
		
	private void findPaths(int[][] graph) {
		// Check if the number of vertices were initialized
		if (numVertices <= 0) {
			System.out.println("Error: The graph has no vertices");
			System.exit(1);
		}
		
		int[] estimate = new int[numVertices];
		boolean[] candidate = new boolean[numVertices];
		boolean[] reached = new boolean[numVertices];
		boolean loop = true;
		
		// Initialize the first vertex
		cost[0] = 0;
		estimate[0] = 0;
		candidate[0] = false;
		reached[0] = true;
		
		// Initialize the other vertices
		for (int i = 1; i < numVertices; i++) {
			reached[i] = false;
			
			if (graph[0][i] > 0) {	// Neighbours of vertex
				estimate[i] = graph[0][i];
				candidate[i] = true;
			} else {
				estimate[i] = Integer.MAX_VALUE;
				candidate[i] = false;
			}	
		}
		
		while(loop) {
			// Finding the candidate with the lowest estimate
			int bestEstimate = Integer.MAX_VALUE;
			int index = 0;
			
			for (int i = 0; i < numVertices; i++) {
				if ((candidate[i] == true) && (estimate[i] < bestEstimate)) {
					index = i;
					bestEstimate = estimate[i];
				}
			}
			
			// Set candidate to reached
			cost[index] = estimate[index];
			reached[index] = true;
			candidate[index] = false;
			
			// Update neighbours
			for (int i = 0; i < numVertices; i++) {
				if ((graph[index][i] > 0) && (reached[i] == false)) {
					if ((cost[index] + graph[index][i]) < estimate[i]) {
						estimate[i] = cost[index] + graph[index][i];
						candidate[i] = true;
						predecessor[i] = index;
					}
				}
			}
						
			loop = false;
			for (int i = 0; i < numVertices; i++) {
				if (reached[i] == false) {
					loop = true;
					break;
				}
			}
		}
		findMaxVertex();
	}
	
	private void findMaxVertex() {	
		maxWeight = 0;
		maxVertex = 0;
		
		for (int i = 0; i < numVertices; i++) {
			if (cost[i] > maxWeight) {
				maxVertex = i;
				maxWeight = cost[i];
			}
		}
	}
	
	private String getRoute(int vertex) {
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(vertex);
		
		int index = vertex;
		while(predecessor[index] > 0) {
			stack.push(predecessor[index]);
			index = predecessor[index];
		}
		stack.push(0);
		
		String route = "";
		
		while (stack.size() > 0) {
			route += (stack.pop());
			if (stack.size() != 0) {	// Formats the last route
				route += " -> ";
			}
		}
		return route;
	}
	
	public String toString() {
		String output;
		
		output = name + "\n";
		for (int i = 0; i < name.length(); i++) {
			output += "-";
		}
		output += "\nVertex " + maxVertex + " is the furthest at a distance of " + maxWeight + "\n";
		output += "Shortest route: " + getRoute(maxVertex) + "\n";
		return output;
	}

}
