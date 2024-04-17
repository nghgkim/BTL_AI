from data import  TESTCASE
from searching import SearchPuzzle
import time
import matplotlib.pyplot as plt

class PipesPuzzle:
    def __init__(self):
        self.init_state = None
        self.level = None
        self.create_puzzle()
        self.path = []
        self.dataForPlot = []
    def create_puzzle(self):
        """
        generate level and init_state from GOAL_STATES
        """
        print("Choose level:")
        print("level 1-3: simple")
        print("level 4-5: immediate")
        print("level 6-7  : advance (take too much time (about 10 minute or more)")
        self.level = int(input())
        if self.level > 7:
            quit()
        testcase = TESTCASE[f"level{self.level}"]
        self.init_state = testcase
    def solve(self, solve_choice):
        solver = SearchPuzzle()
        startTime = time.time()
        print("Please wait....")
        if solve_choice == "1":
            self.path = solver.solve_dfs(self.init_state)
        elif solve_choice == "2":
            temp = solver.solve_Astar(self.init_state)
            self.dataForPlot = temp[0]
            self.path = temp[1]
        else:
            print("You must choose 1 for DFS or 2 for A*.")
            exit(1)
        executeTime = time.time() - startTime
        print("Time for searching: ", str(round(executeTime, 4)))
        ##
        '''
        solver.append(GOAL_STATES["level3"])
        '''
    def simulatePlot(self):
        plt.bar(*zip(*self.dataForPlot.items()))
        plt.xlabel('Number of step')
        plt.ylabel('Number of searching in step')
        plt.title('Statistics')
        plt.show()       