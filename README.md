# Spanning trees in the graph

## Table of contents
* [General info](#general-info)
* [Usage](#usage)

## General info
This project includes an algorithm searching for all spanning trees in the graph and their total number.
	
## Usage
### Instruction
```python
graph = generator.next_graph(graph_type=①, n=②, m=③, percent=④)
```
* ① - type of graph ("complete" - complete graph, "grid" - grid graph (n x m edges), "random" - random graph, "percent" - random graph with a fixed number of edges)
* ② - number of nodes when type of graph equals "complete", number of edges n when type of graph equals "grid"
* ③ - number of edges m when type of graph equals "grid"
* ④ - the percentage of graph edges when type of graph equals "percent"

### Sample results
#### Graph - grid (n=2, m=3)
![example1](./images/st1.png)

![example1](./images/st2.png)

![example1](./images/st3.png)

#### Graph - complete (n=6)
![example1](./images/st4.png)

![example1](./images/st5.png)

![example1](./images/st6.png)
