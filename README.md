# NeighborDist
This code simulates the following scenario: N=100 nodes are uniformly scattered in a 1 by 1 square. Two nodes are connected if their distance is less than R=0.1. A set is a group of nodes which can reach each other either directly or through a number of neighbors. This scenario is executed 3000 times. In the end the mean and variance of the number of sets and the number of neighbors for the first node is calculated. The histogram for the distribution of these values are saved to images. In this implementation Union-Find algorithm is used to find the sets. 

## How to Run the Code
Run the following command to install the matplotlib library:

    pip install matplotlib

Run the code by simply running:

    python prog.py