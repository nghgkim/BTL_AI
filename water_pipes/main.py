
'''
from ui import PuzzleInterface
from puzzle import PipesPuzzle
if __name__ == "__main__":
    solve_choice = input("Solve by BFS or BestFirstSearch? ") # BFS == 1 or BestFirstSearch == 2

    puzzle_pipes = PipesPuzzle()
    puzzle_pipes.solve(solve_choice)
    puzzle_interface = PuzzleInterface(puzzle_pipes)
'''
from puzzle import PipesPuzzle
from ui import PuzzleInterface

if __name__ == "__main__":
  
  
  solve_choice = input("Solve by DFS or BestFirstSearch? (1: DFS, 2: A*") 

  puzzle_pipes = PipesPuzzle()
  puzzle_pipes.solve(solve_choice)
  puzzle_interface = PuzzleInterface(puzzle_pipes)
  puzzle_interface.running()
  if len(puzzle_pipes.dataForPlot) != 0:
    t = input("Shall we show statistics about heuristic searching ?? (Y: Yes, other: No)")
    if t == 'Y' or t =='y':
      puzzle_pipes.simulatePlot()
  '''
  temp = State(GOAL_STATES["level1"])
  print(temp.countBump)
  print(temp.getNoWaterInPipe())
  temp.printState()
  temp = State(GOAL_STATES["level3"])
  print(temp.countBump)
  '''

  


  '''
  ---   ---     
  |       |
  
  |
  ---
  |
  -|-
   |

   |
  -|-

  0--
  --0

  
  '''