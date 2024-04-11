# import pygame library
import pygame

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((600, 700))

# Title and Icon 
pygame.display.set_caption("SUDOKU SOLVER USING DFS")
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
step = 0
# Default Sudoku Board
grid = [
	[0,0,3,5,1,0,6,2,8],
    [2,9,0,0,0,3,7,0,0],
    [0,0,0,0,4,0,0,0,5],
    [0,4,7,0,3,8,2,0,0],
    [5,1,2,6,0,7,0,4,0],
    [6,0,0,0,0,5,0,9,0],
    [7,8,0,0,0,0,0,6,0],
    [0,0,6,9,0,0,5,0,1],
    [1,0,4,2,7,0,3,0,0]
]

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
	global x
	x = pos[0] // dif
	global y
	y = pos[1] // dif

# Highlight the cell selected
def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 

# Function to draw required lines for making Sudoku grid		 
def draw():
	# Draw the lines
	for i in range (9):
		for j in range (9):
			if grid[j][i] != 0:
				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[j][i]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif))
				
	# Draw lines horizontally and verticallyto form grid		 
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	 

# Fill value entered in cell	 
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 15, y * dif + 15)) 

# Raise error when wrong value entered
def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
	
def checkValid(board, num , pos):
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check row
    for i  in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False 
        
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
         for j in range(box_x * 3, box_x * 3 + 3):
             if board[i][j] == num and (i,j) != pos:
                 return False
             
    return True

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None

# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
	global step
	empty = findEmpty(grid)

	if not empty:
		return True
	else: 
		row, col = empty

	pygame.event.pump() 

	for i in range(1, 10):
		if checkValid(grid, i, empty) == True:
			grid[row][col]= i
			global x, y
			x = col
			y = row

			# white color background
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(1000)
			if solve(grid, row, col) == 1:
				return True
			else:
				grid[row][col] = 0

			# white color background
			screen.fill((255, 255, 255))

			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(100) 
	return False

# Display instruction for the game
def instruction():
	text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
	text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	 
	screen.blit(text2, (20, 540))

# Display options when solved
def result():
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (20, 570)) 
	
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# The loop thats keep the window running
while run:
	# White color background
	screen.fill((255, 255, 255))
	# Loop through the events stored in event.get()
	for event in pygame.event.get():
		# Quit the game window
		if event.type == pygame.QUIT:
			run = False
			
		# Get the mouse position to insert number 
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos)
			
		# Get the number to be inserted if key pressed 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN:
				flag2 = 1
				
			# If R pressed clear the sudoku board
			if event.key == pygame.K_r:
				rs = 0
				error = 0
				flag2 = 0
				grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
				
			# If D is pressed reset the board to default 
			if event.key == pygame.K_d:
				rs = 0
				error = 0
				flag2 = 0
				grid = [
					[0,0,3,5,1,0,6,2,8],
                    [2,9,0,0,0,3,7,0,0],
                    [0,0,0,0,4,0,0,0,5],
                    [0,4,7,0,3,8,2,0,0],
                    [5,1,2,6,0,7,0,4,0],
                    [6,0,0,0,0,5,0,9,0],
                    [7,8,0,0,0,0,0,6,0],
                    [0,0,6,9,0,0,5,0,1],
                    [1,0,4,2,7,0,3,0,0]
				]
    
	if flag2 == 1:
		if solve(grid, 0, 0) == False:
			error = 1
		else:
			rs = 1
		flag2 = 0
		
	if val != 0:		 
		draw_val(val)
		if checkValid(grid, val, (int(x), int(y))) == True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2() 
		val = 0
	
	if error == 1:
		raise_error1() 
		
	if rs == 1:
		result()	
		 
	draw() 
	
	if flag1 == 1:
		draw_box()
			 
	instruction() 

	# Update window
	pygame.display.update() 

# Quit pygame window 
pygame.quit()