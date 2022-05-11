Open command prompt inside the lab directory:

To run the test with the Depth-First Search (DFS), type in command prompt: 
 
Tiny maze: python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs 
Medium maze: python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs 
Big maze: python pacman.py -l bigMaze -p SearchAgent -z .5 -a fn=dfs  

Breadth-First Search (BFS):  

Tiny maze: python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs 
Medium maze: python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs 
Big maze: python pacman.py -l bigMaze -p SearchAgent -z .5 -a fn=bfs  

Uniform Cost Search (UCS):  

Tiny maze: python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs 
Medium maze: python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs 
Big maze: python pacman.py -l bigMaze -p SearchAgent -z .5 -a fn=ucs


Best-First Search (BEFS):

python3 pacman.py -l tinyMaze -p SearchAgent -a fn=befs
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=befs
python3 pacman.py -l bigMaze -p SearchAgent -a fn=befs -z .5

A* Search (astar)

python3 pacman.py -l tinyMaze -p SearchAgent -a fn=astar
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=astar
python3 pacman.py -l bigMaze -p SearchAgent -a fn=astar -z .5

Find The Conner: 

python3 pacman.py -l tinyCorners -p SearchAgent -a fn=befs,prob=CornersProblem
python3 pacman.py -l mediumCorners -p SearchAgent -a fn=befs,prob=CornersProblem

Corners Problem: Heuristic:

python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python3 pacman.py -l mediumCorners -p SearchAgent -a fn=astar,prob=CornersProblem,heuristic=cornersHeuristic

OpenMaze matrix test:
python3 pacman.py -l openMaze -p SearchAgent -a fn=befs
python3 pacman.py -l openMaze -p SearchAgent -a fn=bfs
python3 pacman.py -l openMaze -p SearchAgent -a fn=ucs
python3 pacman.py -l openMaze -p SearchAgent -a fn=dfs
python3 pacman.py -l openMaze -p SearchAgent -a fn=astar

