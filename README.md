# Graph-Coloring
The application colors the vertices of graph using Graph Coloring Algorithm 

The code has two lists, one of the graph vertices and one of the colors(Taking an example of 4 vertices graph and 5 colors)

Adjacent Vertices for each vertex in the graph is specified in the list 'adjvertices{}'

A method named 'can_be_colored(ver, color)' where 'ver' is vertex to be colored and 'color' is the color to be used.
is used to check if color of adjacent vertex is same as that of the color.
This method returns false if color of one of the adjacent vertices is same as the 'color' parameter passed to this method. It returns true otherwise.

Then 'mcolor(ver)' method colors the vertex by checking every color in the 'colors' list for every adjacent vertex by calling the 'can_be_colored' method.


The main method demo() colors every vertex in list 'vertices' by calling method 'mcolor'.
