---
mainfont: "Helvetica Neue"
sansfont: "Helvetica Neue"
monofont: "Menlo"

header-includes:
  - \usepackage{amssymb}
---

\newpage
# Plan

**Terms + Definitions**  

+ **Spaced Repetition**: Space out lecture topic review sessions using a modified FSRS algorithm, with a dedicated day to master each topic.  
+ **Based Way**: We will use adaptive learning with active, deliberate practice to develop automaticity.  

---

**Battle Plan:**  

+ Skim the whole syllabus and create an Anki deck with basic terms and steps (should take a maximum of one to two days).  
+ Study the Anki deck daily on the go as soon as the deck is created.  
+ Read notes to get the basic gist of each type of algorithm.  
+ Run the practice script to reinforce the algorithm just learned. Would most likely be leetcode style practice problems, or mcq.


**Tools:**  

+ Anki (with FSRS or preset intervals)
+ Markdown for a mistake log
+ Practice script with lots of practice questions
+ This notes for quick look up of information


**Resources**

+ [CP Handbook](https://cses.fi/book/book.pdf)

\newpage
**ToDo**

```

[ ] Skim through all the chapters and add to anki 
[ ] Lecture 1
[ ] Lecture 2
[ ] Lecture 3
[ ] Lecture 4
[ ] Lecture 5
[ ] Lecture 6
[ ] Lecture 7
[ ] Lecture 8
Midterm 
[ ] Lecture 9
[ ] Lecture 10
[ ] Lecture 11
[ ] Lecture 12

[ ] Lecture 13 : CLRS §22.1-22.2
[ ] Lecture 14 : CLRS §22.3
[ ] Lecture 15 : CLRS §22.3
[ ] Lecture 16 : CLRS §22.4-22.5
[ ] Lecture 17 : CLRS §23.1
[ ] Lecture 18 : CLRS §23.2
[ ] Lecture 19 : CLRS §24.3
[ ] Lecture 20 : CLRS §25.2
[ ] Lecture 21 : CLRS §26.3, 26.6

```

-----

\newpage
## Graphs







#### Anki

A graph consist of?
-> Nodes and edges 

What is a path in a graph?
-> A path leads from node a to node b through edges of the graph. 

What is the length of a path in a graph?
-> The length of a path is the number of edges in it. 

What is a cycle?
-> A path is a cycle if the first and the last node is the same.  

What is a simple path?
-> A path is simple if each node apears at most once in the path. 

What is a connected graph?
-> A path is connected if there is a path between any two nodes. 

What are the connected parts of a graph called?
-> Components 

What is a tree?
-> A tree is a connected graph with $n - 1$ edges and there is a unique path between any two nodes of a tree. 

Directed graph?
-> A graph is directed if the edges can be traversed in one direction only. 

What is a weighted graph?
-> In a weighted graph, each edge is assigned a weight. Weights are often interpreted as edge lengths. 

The length of a path in a weighted graph is the?
-> It is the sum of the edge weights on the path. 

What is the shorted path?
-> The length of a path in weighted graph where it is the minimum sum of the edge weights on the path from node a to node b. 

Neighbors or adjacent?
-> Two nodes are neighbors or adjacent if there is an edge between them. 

What is the degree of a node mean?
-> The degree of a node is the number of its neighbors. 

The sum of degree in a graph is always?
-> 2m where m is the number of edges because each edge increase the degree of exactly two nodes by one. 

What is a regular graph?
-> A graph is regular if the degree of every node is a constant d.

What is a complete graph?
-> A graph is complete if the degree of every node is $n - 1$

What is a bipartite graph?
-> A graph that can be colored using two colors where no adjacent nodes have the same color. 


When can a graph be bipartite?
-> When a graph does not contain a cycle with an odd number of edges. 










\newpage
## Minimum Spanning Tree (MST)

Imagine you are an engineer tasked with connecting every single building on campus with a network cable. Each pair of buildings can be joined by an underground conduit that costs money. In this case the longer the conduit the higher the cost. You want 
1. All buildings connected (no isolated building).
2. No unnecessary loops (loops mean wasted cable).
3. Total cost as low as possible. 

A graph is case can model this neatly : 

| Graph Term      | Campus Analogy            |
|------------------|----------------------------|
| Vertex (node)    | A building                 |
| Edge             | An underground conduit     |
| Weight           | The cost/length of that conduit |

An Minimum Spanning Tree (MST) is exactly the cheapest way to fulful the three requirements above. 





#### Anki

What is minum spanning tree?
-> Given a connected, undirected, weighted graph $G = (V,E,w)$, it is a spanning tree that touches every vertex with $|V| - 1$ edges and no cycles. 


What is minimum spanning tree in simple?
-> The minimum spanning tree is the spanning tree whose total edge-weight is minimum.


how to detect a minimum spanning tree?
-> 


### Kruskal Algorithm 






### Prim's Algorithm



## Single-Source Shortest Paths: Dijkstra	


#### Anki


