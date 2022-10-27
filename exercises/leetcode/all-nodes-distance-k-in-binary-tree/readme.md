# all-nodes-distance-k-in-binary-tree

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

## brief

- convert tree to an undirected graph
- start a bfs from the target with distance 0 to k layer
- each bfs neighbor distance++
- when distance == k
  - add it to the solution
  - stop its bfs run
