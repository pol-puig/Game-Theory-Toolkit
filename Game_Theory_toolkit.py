from tkinter import *
from tkinter import messagebox
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json

#Load json file containing games info
with open('files/game_db.json') as json_file:
	games = json.load(json_file)


root = Tk()
root.title("Game Theory")
root.geometry("+500+500")
root.iconbitmap("files/logo_upf.ico")

#global variables
rows = 4
columns = 3
matrix = []
row_labels = []
column_labels = []
a_matrix = []
b_matrix = []
a_dicc = {}
b_dicc = {}
ismixed = False
eval_list = []
isatheproblem = True
p_notmixed = "No"


i11 = Entry(root, width=2, font="Verdana 14")
i12 = Entry(root, width=2, font="Verdana 14")
i21 = Entry(root, width=2, font="Verdana 14")
i22 = Entry(root, width=2, font="Verdana 14")

i31 = Entry(root, width=2, font="Verdana 14")
i32 = Entry(root, width=2, font="Verdana 14")
i41 = Entry(root, width=2, font="Verdana 14")
i42 = Entry(root, width=2, font="Verdana 14")


la1 = Label(root, text="a1", font="Verdana 14")
la11 = Label(root, text="(", font="Verdana 14")
la12 = Label(root, text=",", font="Verdana 14")
la13 = Label(root, text=")", font="Verdana 14")

la21 = Label(root, text="(", font="Verdana 14")
la22 = Label(root, text=",", font="Verdana 14")
la23 = Label(root, text=")", font="Verdana 14")

la3 = Label(root, text="a2", font="Verdana 14")
la31 = Label(root, text="(", font="Verdana 14")
la32 = Label(root, text=",", font="Verdana 14")
la33 = Label(root, text=")", font="Verdana 14")

la41 = Label(root, text="(", font="Verdana 14")
la42 = Label(root, text=",", font="Verdana 14")
la43 = Label(root, text=")", font="Verdana 14")

#first row of inputs
la1.grid(row=3, column=1, padx=(15,25), pady=10)
la11.grid(row=3, column=2)
i11.grid(row=3, column=3)
la12.grid(row=3, column=4)
i12.grid(row=3, column=5)
la13.grid(row=3, column=6, padx=(0,20))

la21.grid(row=3, column=7)
i21.grid(row=3, column=8)
la22.grid(row=3, column=9)
i22.grid(row=3, column=10)				
la23.grid(row=3, column=11, padx=(0,20))

#second row of inputs
la3.grid(row=4, column=1, padx=(15,25), pady=10)
la31.grid(row=4, column=2)
i31.grid(row=4, column=3)
la32.grid(row=4, column=4)
i32.grid(row=4, column=5)
la33.grid(row=4, column=6, padx=(0,20))

la41.grid(row=4, column=7)
i41.grid(row=4, column=8)
la42.grid(row=4, column=9)
i42.grid(row=4, column=10)
la43.grid(row=4, column=11, padx=(0,20))

#labels y axis
lb1 = Label(root, text="b1", font="Verdana 14")
lb1.grid(row=2, column=3, columnspan=3)
lb2 = Label(root, text="b2", font="Verdana 14")
lb2.grid(row=2, column=8, columnspan=3)

#create a matrix of each category
matrix = [[[la11,i11,la12,i12,la13],[la21,i21,la22,i22,la23]],[[la31,i31,la32,i32,la33],[la41,i41,la42,i42,la43]]]
row_labels = [la1, la3]
column_labels = [lb1,lb2]

"""
Matrix UI management
"""
#D36779


def add_row():
	global matrix
	global rows
	global columns
	if rows < 25:
		l1 = []
		cont = 0
		for i in range(columns - 1):
			l2 = []

			a = Label(root, text="(", font="Verdana 14")
			a.grid(row=rows+1, column=2+cont)
			l2.append(a)	

			b = Entry(root, width=2, font="Verdana 14")
			b.grid(row=rows+1, column=3+cont, pady=10)
			l2.append(b)

			c = Label(root, text=",", font="Verdana 14")
			c.grid(row=rows+1, column=4+cont)
			l2.append(c)

			d = Entry(root, width=2, font="Verdana 14")
			d.grid(row=rows+1, column=5+cont, padx=0)
			l2.append(d)

			e = Label(root, text=")", font="Verdana 14")			
			e.grid(row=rows+1, column=6+cont, padx=(0,20))
			l2.append(e)
			
			cont += 5
			l1.append(l2)

		matrix.append(l1)
		create_row_label()
		rows += 1


def create_row_label():
	global row_labels
	lab = Label(root, text="a"+str(rows - 1), font="Verdana 14")
	lab.grid(row=rows+1, column=1, pady=10, padx=(15,25))
	row_labels.append(lab)


def delete_row_label():
	global row_labels
	row_labels[-1].destroy()
	del row_labels[-1]


def delete_row():
	global matrix
	global rows
	global columns
	if rows > 4:
		for i in range(len(matrix[-1])):
			matrix[-1][i][4].destroy()
			matrix[-1][i][3].destroy()
			matrix[-1][i][2].destroy()
			matrix[-1][i][1].destroy()
			matrix[-1][i][0].destroy()
		del matrix[-1]
		delete_row_label()
		rows -= 1


def add_column():
	global columns
	global matrix 
	global rows
	if columns < 25:
		for i in range(rows-2):
			l2 = []

			a = Label(root, text="(", font="Verdana 14")
			a.grid(row=3+i, column=columns*4+columns-3)
			l2.append(a)	

			b = Entry(root, width=2, font="Verdana 14")
			b.grid(row=3+i, column=columns*4+columns-3+1)
			l2.append(b)

			c = Label(root, text=",", font="Verdana 14")
			c.grid(row=3+i, column=columns*4+columns-3+2)
			l2.append(c)

			d = Entry(root, width=2, font="Verdana 14")
			d.grid(row=3+i, column=columns*4+columns-3+3, padx=0)
			l2.append(d)

			e = Label(root, text=")", font="Verdana 14")			
			e.grid(row=3+i, column=columns*4+columns-3+4, padx=(0,20))
			l2.append(e)
			
			matrix[i].append(l2)

		create_column_label()
		columns += 1


def create_column_label():
	global column_labels
	global columns
	lab = Label(root, text="b"+str(columns), font="Verdana 14")
	lab.grid(row=2, column=columns*4 + (columns-1)-1, columnspan=3, pady=10)
	column_labels.append(lab)


def delete_column_label():
	global column_labels
	column_labels[-1].destroy()
	del column_labels[-1]

def delete_column():
	global columns
	global matrix
	if columns > 3:
		for i in range(len(matrix)):
			matrix[i][-1][4].destroy()
			matrix[i][-1][3].destroy()
			matrix[i][-1][2].destroy()
			matrix[i][-1][1].destroy()
			matrix[i][-1][0].destroy()
			del matrix[i][-1]
		
		delete_column_label()
		columns -= 1



"""

		TOOLKIT ALGORISMS


"""


def get_a_numbers():
	global a_matrix
	global a_dicc
	ll2 = []
	for row in matrix:
		ll1 = []
		for cell in row:	
			a = cell[1].get()
			if (((a.startswith('-') and a[1:].isdigit()) == False) and ((a.isdigit() == False))):
				messagebox.showerror("ERROR","Some input squares are blank or format is not supported.")
				raise Exception("Some input squares are missing.")
			else:
				ll1.append(int(cell[1].get()))
		ll2.append(ll1)
	a_matrix = ll2
	a_dicc = {}
	create_dicc(a_dicc, a_matrix)
	


def get_b_numbers():
	global b_matrix
	global b_dicc
	ll2 = []
	for j in range(len(matrix[0])):
		ll1 = []
		for i in range(len(matrix)):
			a = matrix[i][j][3].get()
			if (((a.startswith('-') and a[1:].isdigit()) == False) and ((a.isdigit() == False))):
				messagebox.showerror("ERROR","Some input squares are blank or format is not supported.")
				raise Exception("Some input squares are missing.")
			else:
				ll1.append(int(a))
		ll2.append(ll1)
	b_matrix = ll2
	b_dicc = {}
	create_dicc(b_dicc, b_matrix)



def create_dicc(dicc, mat):
	
	for i in range(len(mat)):
		dicc[i] = mat[i]



def clear_dominated_color():
	for item in row_labels:
		item.config(bg="SystemButtonFace")
	for item in column_labels:
		item.config(bg="SystemButtonFace")



def clear_number_color():
	for row in matrix:
		for i in range(len(row)):
			row[i][1].config(bg="White")
			row[i][3].config(bg="White")



def dominated_color(label_matrix, a_or_b_matrix):
	dom_list = create_dominated_list(a_or_b_matrix)
	for i in range(len(dom_list)):
		if "W" in dom_list[i]:
			label_matrix[i].config(bg="orange")	
		if "S" in dom_list[i]:
			label_matrix[i].config(bg="red")



def show_dominated():
	dom = compute_dominated_list()
	msg = ""
	for i in range(2):
		for j in range(len(dom[i])):
			msg = msg + dom[i][j]
		msg = msg + "\n"

	if msg == "\n\n":
		clear_dominated_color()
		messagebox.showinfo("Dominated Strategies", "There are no weakly or strictly dominated strategies")
	else:
		clear_dominated_color()
		dominated_color(row_labels, a_matrix)
		dominated_color(column_labels, b_matrix)
		messagebox.showinfo("Dominated Strategies", msg)
	


def compute_dominated_list():
	get_a_numbers()
	get_b_numbers()
	x = create_dominated_list(a_matrix)
	y = create_dominated_list(b_matrix)
	xlist = []
	ylist = []

	for i in range(len(x)):
		count = 1
		for item in x[i]:
			if item == "W":
				xlist.append("a" + str(i+1) + " is weakly dominated by a" + str(count) + "\n")
			elif item == "S":
				xlist.append("a" + str(i+1) + " is strictly dominated by a" + str(count) + "\n")
	
			count += 1


	for j in range(len(y)):
		count = 1
		for item in y[j]:
			if item == "W":
				ylist.append("b" + str(j+1) + " is weakly dominated by b" + str(count) + "\n")
			elif item == "S":
				ylist.append("b" + str(j+1) + " is strictly dominated by b" + str(count) + "\n")
	
			count += 1

	return [xlist, ylist]



def create_dominated_list(matrix1):
	ll1 = []
	count = 0
	for i in range(len(matrix1)):
		ll2 = []
		for j in range(len(matrix1)):
			if i == j:
				count += 1
				ll2.append("s" + str(count))
				continue
			a = is_dominated(matrix1[i], matrix1[j])
			ll2.append(a)
		ll1.append(ll2)
	return ll1



def is_dominated(list1, list2):
	count = 0
	for i in range(len(list1)):
		if list1[i] < list2[i]:
			count += 2
		elif list1[i] > list2[i]:
			count -= 1000000
		else:
			count += 1
	if count == (len(list1) * 2):
		return "S"
	elif count > (len(list1)):
		return "W"
	else:
		return False





#clear inputs of matrix
def clear_matrix():
	for row in matrix:
		for column in row:
			column[1].delete(0,END)
			column[3].delete(0,END)



#randomize inputs of matrix
def randomize():
	clear_matrix()
	clear_dominated_color()
	clear_number_color()
	x = first.get()
	y = last.get()
	for item in [x,y]:	
		if (((item.startswith('-') and item[1:].isdigit()) == False) and ((item.isdigit() == False))):
			messagebox.showerror("ERROR","Some randomize input squares are blank or format is not supported.")
			raise Exception("Some input squares are missing or format not supported.")
	if int(x) > int(y):
		messagebox.showerror("ERROR","Randomize range not supported (upper limit is lower than lower limit)")
		raise Exception("Randomize range not supported.")				

	for row in matrix:
		for column in row:
			column[1].insert(0, random.randint(int(x),int(y)))
			column[3].insert(0, random.randint(int(x),int(y)))



#get pure NE and highlight the best responses in yellow
def find_pure_ne():
	clear_number_color()
	get_a_numbers()
	get_b_numbers()
	clear_dominated_color()
	la = []
	lb = []
	max_a_matrix = []
	max_b_matrix = []

	#swap columns and rows of a_matrix and b_matrix for computing max number of each
	for j in range(len(a_matrix[0])):
		max_a_matrix.append([])
		for i in range(len(a_matrix)):
			max_a_matrix[-1].append(a_matrix[i][j])
			
	for j in range(len(b_matrix[0])):
		max_b_matrix.append([])
		for i in range(len(b_matrix)):
			max_b_matrix[-1].append(b_matrix[i][j])


	#get list with best choices of each player (rationalizable) and change color to yellow 		
	for i in range(len(max_a_matrix)):
		la.append([])
		for j in range(len(max_a_matrix[i])):
			if max_a_matrix[i][j] == max(max_a_matrix[i]):
				la[i].append("YES")
				matrix[j][i][1].config(bg="yellow")
			else:
				la[i].append("NO")

	for i in range(len(max_b_matrix)):
		lb.append([])
		for j in range(len(max_b_matrix[i])):
			if max_b_matrix[i][j] == max(max_b_matrix[i]):
				lb[i].append("YES")
				matrix[i][j][3].config(bg="yellow")
			else:
				lb[i].append("NO")

	return [la,lb]


def show_pure_ne():
	#get pure NE
	find_pure = find_pure_ne()
	la = find_pure[0]
	lb = find_pure[1]
	msg = "List of NE strategies: \n\n"
	for i in range(len(lb)):
		for j in range(len(lb[0])):
			if ((la[j][i] == "YES") and (lb[i][j] == "YES")):
				msg = msg + "(a" + str(i+1) + ",b" + str(j+1) + ")\n"

	if (msg == "List of NE strategies: \n\n"):
		messagebox.showinfo("Pure Strategy Nash Equilibria", "No Pure Strategy Nash Equilibria Found")
	else:
		messagebox.showinfo("Pure Strategy Nash Equilibria", msg)


def compute_mixed_ne():
	show_iterated_strongly_dominated_strategies_color()
	global ismixed
	ismixed = False
	global eval_list
	eval_list = []
	global isatheproblem
	isatheproblem = False
	global p_notmixed
	p_notmixed = "No"
	
	try:
		if (len(a_matrix) != len(b_matrix)):
			raise Exception("ERROR - Not a square matrix")
	except:
		return []

	dimension = len(a_matrix) 
	a_eq_list = []
	b_eq_list = []
	for i in range(dimension - 1):
		a_each_eq = []
		b_each_eq = []
		for j in range(dimension):	
			a_each_eq.append(a_matrix[i][j] - a_matrix[i+1][j])
			b_each_eq.append(b_matrix[i][j] - b_matrix[i+1][j])
		a_eq_list.append(a_each_eq)
		b_eq_list.append(b_each_eq)
	prop_sum = [1] * dimension
	a_eq_list.append(prop_sum)
	b_eq_list.append(prop_sum)
	a_array = np.array(a_eq_list)
	b_array = np.array(b_eq_list)
	zeroes = [0] * (dimension - 1)
	zeroes.append(1)
	
	#catch error if there is no mixed nash equilibrium
	try:
		isatheproblem = True
		q = np.linalg.solve(a_array, zeroes)
		isatheproblem = False
		p = np.linalg.solve(b_array, zeroes)

	except:
		if(isatheproblem):
			try:
				p_notmixed = np.linalg.solve(b_array, zeroes)
				p_notmixed = p_notmixed[0]
			except:
				pass
		else:
			p_notmixed = np.linalg.solve(a_array, zeroes)
			p_notmixed = p_notmixed[0]

		if(dimension == 2):
			pa1 = a_matrix[0][1]
			pa2 = a_matrix[1][1]
			pa3 = (a_matrix[0][0] - a_matrix[0][1]) * 1 + a_matrix[0][1]
			pa4 = (a_matrix[1][0] - a_matrix[1][1]) * 1 + a_matrix[1][1]
			eval_list.append(pa1 >= pa2)
			eval_list.append(pa3 >= pa4)
			
			pb1 = b_matrix[0][1]
			pb2 = b_matrix[1][1]
			pb3 = (b_matrix[0][0] - b_matrix[0][1]) * 1 + b_matrix[0][1]
			pb4 = (b_matrix[1][0] - b_matrix[1][1]) * 1 + b_matrix[1][1]
			eval_list.append(pb1 >= pb2)
			eval_list.append(pb3 >= pb4)
		return []
	
	else:
		
		p = list(p)
		q = list(q)
		for i in range(len(p)):
			if (p[i] == int(p[i])):
				p[i] = int(p[i])
			if (q[i] == int(q[i])):
				q[i] = int(q[i])
			p[i] = round(p[i],2)
			q[i] = round(q[i],2)
		
		#check if there is any negative value
		for i in range(len(p)):
			if((p[i] < 0) or (q[i] < 0)):
				return []
		
		#evaluate equations for plotting best responses later (only 2x2 matrices)
		if(dimension == 2):
			pa1 = a_matrix[0][1]
			pa2 = a_matrix[1][1]
			pa3 = (a_matrix[0][0] - a_matrix[0][1]) * 1 + a_matrix[0][1]
			pa4 = (a_matrix[1][0] - a_matrix[1][1]) * 1 + a_matrix[1][1]
			eval_list.append(pa1 >= pa2)
			eval_list.append(pa3 >= pa4)
			
			pb1 = b_matrix[0][1]
			pb2 = b_matrix[1][1]
			pb3 = (b_matrix[0][0] - b_matrix[0][1]) * 1 + b_matrix[0][1]
			pb4 = (b_matrix[1][0] - b_matrix[1][1]) * 1 + b_matrix[1][1]
			eval_list.append(pb1 >= pb2)
			eval_list.append(pb3 >= pb4)

		ismixed = True
		return([p,q])


def show_mixed_ne():
	ne = compute_mixed_ne()
	msg1 = "Player A strategic profile: ("
	msg2 = "Player B strategic profile: ("
	nte = "Note: if there is any strategy that is dominated (in red), it has 0 probability of being played. It won't be shown in the solution but should be considered"
	t1 = False
	t2 = False
	#check if there is no nash equilibria
	if (ne == []):
		messagebox.showinfo("Nash equilibrium in mixed strategies", "There is no Nash Equilibria in mixed strategies or there is an infinite number. Plot best response functions to get better information")
		raise Exception("No nash equilibria")

	#check if it is a pure nash equilibrium
	for i in range(len(ne[0])):
		if (ne[0][i] == 1):
			t1 = True
		if (ne[1][i] == 1):
			t2 = True
		if (t1 and t2):
			messagebox.showinfo("Nash Equilibrium in mixed strategies", "The nash equilibrium in mixed strategies that have been found results to be a pure strategies Nash equilibrium. Use 'Pure NE' function to find it")
			raise Exception("ERROR - Not a mixed strategies NE")

	#show messagebox with the mixed strategies equilibria
	for i in range(len(ne[0])):
		msg1 = msg1 + str(ne[0][i]) + ","
		msg2 = msg2 + str(ne[1][i]) + ","
	msg1 = msg1[:-1] + ")\n\n"
	msg2 = msg2[:-1] + ")"
	messagebox.showinfo("Nash Equilibrium in mixed strategies", msg1 + msg2 + "\n\n\n\n" + nte + "\nAlso, use best response functions function to check if there is an infinite amount of mixed Nash Equilibria")




#change the global variables to consider only the ones that are not dominated
def compute_iterated_strongly_dominated_strategies():
	global a_dicc
	global b_dicc
	clear_number_color()
	get_a_numbers()
	get_b_numbers()
	clear_dominated_color()
	am = create_dominated_list(a_matrix)
	bm = create_dominated_list(b_matrix)
	a = a_matrix
	b = b_matrix
	changes = True

	#do the statments while there are still changes. Finish when no more changes are possible
	while (changes):
		changes = False
		for i in range(len(a)):
			if (changes):
				break
			if ("S" in am[i]):
				del a[i]
				del a_dicc[sorted(list(a_dicc.keys()))[i]]
				for j in range(len(bm)):
					b[j].pop(i)
					
				changes = True

		for i in range(len(b)):
			if (changes):
				break
			if ("S" in bm[i]):
				del b[i]
				del b_dicc[sorted(list(b_dicc.keys()))[i]]
			
				for j in range(len(am)):
					a[j].pop(i)
			
				changes = True		

		#create the dominated list again with all the rows and columns minus the ones that have been deleted
		am = create_dominated_list(a)
		bm = create_dominated_list(b)
		


#change color of matrix by checking the dictionary keys
def show_iterated_strongly_dominated_strategies_color():
	compute_iterated_strongly_dominated_strategies()
	al = list(a_dicc.keys())
	bl = list(b_dicc.keys())

	for i in range(len(row_labels)):
		if i not in al:
			row_labels[i].config(bg="red")

	for j in range(len(column_labels)):
		if j not in bl:
			column_labels[j].config(bg="red")


def show_iterated_strongly_dominated_strategies_message():
	show_iterated_strongly_dominated_strategies_color()
	msg = ""
	if (len(a_matrix) == 1):
		msg = msg + "Player A will always choose strategy a" + str(list(a_dicc.keys())[0] + 1) + "\n\n"

	if (len(b_matrix) == 1):
		msg = msg + "Player B will always choose strategy b" + str(list(b_dicc.keys())[0] + 1) + "\n\n"

	if ((len(a_matrix) == 1) and (len(b_matrix) == 1)):
		msg = msg + "Iterated elimination of dominated strategies equilibrium is (" + str(a_matrix[0][0]) + "," + str(b_matrix[0][0]) + ")"
	else:
		msg = msg + "The game isn't dominance solvable (there is no IEDS equilibrium)"


	messagebox.showinfo("Iterated Dominated Strategies", msg)



#compute all NE that will be used to plot. Only 2x2 matrices or less are allowed
def compute_plot_equilibria():
	
	pure = find_pure_ne()
	mixed = compute_mixed_ne()

	if ((len(list(a_dicc.keys())) > 2) or (len(list(b_dicc.keys())) > 2)):
		messagebox.showerror("ERROR", "Can't plot functions: maximum of 2x2 matrices allowed (or matrices that result into a 2x2 matrix by elimination of dominated strategies)")
		raise Exception("Not a 2x2 matrix or less")

	nashs = []
	pstrats = []
	for i in range(len(pure[1])):
		for j in range(len(pure[1][0])):
			if ((pure[0][j][i] == "YES") and (pure[1][i][j] == "YES")):
				nashs.append([i,j])

	
	for i in range(len(nashs)):
		
		if (sorted(list(a_dicc.keys()))[0] == nashs[i][0]):
			pstrats.append([1])
		else:
			pstrats.append([0])

		if (sorted(list(b_dicc.keys()))[0] == nashs[i][1]):
			pstrats[i].append(1)
		else:
			pstrats[i].append(0)

	#don't add empty list of mixed strategies nash equilibrium 
	if mixed == []:
		return pstrats
	else:
		pstrats.append([])
		pstrats[-1].append(mixed[0][0])
		pstrats[-1].append(mixed[1][0])
		return pstrats



#Plot optimal responses of each player to a mixed strategy
def compute_optimal_line():
	show_iterated_strongly_dominated_strategies_color()
	anydominated = False

	if ((len(list(a_dicc.keys())) > 2) or (len(list(b_dicc.keys())) > 2)):
		messagebox.showerror("ERROR", "Can't plot functions: only matrix maximum dimension of 2 or 1 allowed (or matrices that result into a 2x2 matrix or lesser by elimination of dominated strategies)")
		raise Exception("Not a 2x2 matrix or less")

	fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(11,7))
	fig.suptitle("Optimal responses of each player to a mixed strategy", fontsize=20)
	x = np.linspace(0,1,1000)

	
	ax1.set_title("Player A", fontsize=15)
	ax2.set_title("Player B", fontsize=15)
	ax1.set(xlabel="q", ylabel='$U_A$')
	ax2.set(xlabel='p', ylabel='$U_B$')
	ax1.grid(linestyle="--")
	ax2.grid(linestyle="--")
	fig.subplots_adjust(wspace=0.3, hspace=1.5)

	#show dominated strategies if the input matrix is 2x2
	if((rows == 4) and (columns == 3)):
		get_a_numbers()
		get_b_numbers()

		item1 = get_prop_equation(a_matrix[0])
		ax1.plot(x, x*item1[0] + item1[1], label="$U_A$(a" + str(list(a_dicc.keys())[0]+1) + ",q)", linewidth=4, linestyle="-.", color="g")
	
		item2 = get_prop_equation(a_matrix[1])
		ax1.plot(x, x*item2[0] + item2[1], label="$U_A$(a" + str(list(a_dicc.keys())[1]+1) + ",q)" ,linewidth=4, linestyle="--", color="r")
		try:
			x1 = (item1[1]-item2[1])/(item2[0]-item1[0])
			y1 = (item1[0]*x1)+ item1[1]
			if(not ((x1 < -0.000001) or (x1 > 1))):
				ax1.scatter(x1,y1, label="Intersection : ("+str(round(x1,2))+","+str(round(y1))+")", color='black')
				
		except:
			pass
		ax1.legend(loc="lower right")

		item1 = get_prop_equation(b_matrix[0])
		ax2.plot(x, x*item1[0] + item1[1], label="$U_B$(p,b" + str(list(b_dicc.keys())[0]+1) + ")", linewidth=4, linestyle="-.", color="g")
		ax2.legend(loc="lower right")
		
		item2 = get_prop_equation(b_matrix[1])
		ax2.plot(x, x*item2[0] + item2[1], label="$U_B$(p,b" + str(list(b_dicc.keys())[1]+1) + ")", linewidth=4, linestyle="--", color="r")
		ax2.legend(loc="lower right")
		try:
			x1 = (item1[1]-item2[1])/(item2[0]-item1[0])
			y1 = (item1[0]*x1)+ item1[1]
			if(not ((x1 < -0.000001) or (x1 > 1))):
				ax2.scatter(x1,y1, label="Intersection : ("+str(round(x1,2))+","+str(round(y1,2))+")", color='black')
				ax2.legend(loc="lower right")
		except:
			pass
			
		fig.show()
		raise Exception("Dominated strategies are plotted")


	#for all the other cases, not a 2x2 matrix input
	item1 = get_prop_equation(a_matrix[0])
	ax1.plot(x, x*item1[0] + item1[1], label="$U_A$(a" + str(list(a_dicc.keys())[0]+1) + ",q)", linewidth=4, linestyle="-.", color="g")
	
	if (len(a_matrix) == 2):
		item2 = get_prop_equation(a_matrix[1])
		ax1.plot(x, x*item2[0] + item2[1], label="$U_A$(a" + str(list(a_dicc.keys())[1]+1) + ",q)" ,linewidth=4, linestyle="--", color="r")
		try:
			x1 = (item1[1]-item2[1])/(item2[0]-item1[0])
			y1 = (item1[0]*x1)+ item1[1]
			if(not ((x1 < -0.000001) or (x1 > 1))):
				ax1.scatter(x1,y1, label="Intersection : ("+str(round(x1,2))+","+str(round(y1))+")", color='black')
			
		except:
			anydominated = True
			pass
	ax1.legend(loc="lower right")


	item1 = get_prop_equation(b_matrix[0])
	ax2.plot(x, x*item1[0] + item1[1], label="$U_B$(p,b" + str(list(b_dicc.keys())[0]+1) + ")", linewidth=4, linestyle="-.", color="g")
	ax2.legend(loc="lower right")
	if (len(b_matrix) == 2):
		item2 = get_prop_equation(b_matrix[1])
		ax2.plot(x, x*item2[0] + item2[1], label="$U_B$(p,b" + str(list(b_dicc.keys())[1]+1) + ")", linewidth=4, linestyle="--", color="r")
		ax2.legend(loc="lower right")
		try:
			x1 = (item1[1]-item2[1])/(item2[0]-item1[0])
			y1 = (item1[0]*x1)+ item1[1]
			if(not ((x1 < -0.000001) or (x1 > 1))):
				ax2.scatter(x1,y1, label="Intersection : ("+str(round(x1,2))+","+str(round(y1,2))+")", color='black')
				ax2.legend(loc="lower right")
		except:
			anydominated = True
			pass
		
	fig.show()
	if(anydominated):
		messagebox.showinfo("NOTE", "Dominated strategies are not plotted and their probabilities (0) are not considered.\nOnly dominated strategies in a 2x2 matrix will be plotted")



#get equation to use for the system of equations
def get_prop_equation(l_eq):
	if (len(l_eq) == 1):
		return [l_eq[0],0]
	else:
		for i in range(len(l_eq)):
			return [l_eq[0] - l_eq[1], l_eq[1]]


#Plot Nash Equilibria in mixed strategies
def plot_best_response():
	ne = compute_plot_equilibria()
	ne_a = []
	ne_b = []
	anychange = False
	for i in range(len(ne)):
		ne_a.append(ne[i][0])
		ne_b.append(ne[i][1])
	
	fig, ax1 = plt.subplots()
	ax1.set(xlabel="p")
	plt.ylabel("q",rotation=0)
	blue_patch = patches.Patch(color="blue", label="Player A")
	red_patch = patches.Patch(color="red", label="Player B")
	plt.legend(handles=[blue_patch,red_patch], loc="lower right")
	fig.suptitle("Best Response Functions", fontsize="18")

	#if we have a 2x2 matrix on the start and any row/column is being dominated, also plot them
	if((rows == 4) and (columns == 3) and ((len(list(a_dicc.keys())) == 1) or (len(list(b_dicc.keys())) == 1))):
		


		if((len(list(a_dicc.keys())) == 1) and (len(list(b_dicc.keys())) == 2)):
			anychange = True
			ax1.add_patch(patches.Rectangle((0,0),1,1, color="red"))
			ax1.vlines(1-list(a_dicc.keys())[0],0,1, color="blue", linewidth=4, linestyle="-.")
		
		if((len(list(b_dicc.keys())) == 1) and (len(list(a_dicc.keys())) == 2)):
			anychange = True
			ax1.add_patch(patches.Rectangle((0,0),1,1, color="blue"))
			ax1.hlines(1-list(b_dicc.keys())[0],0,1, color="red", linewidth=4, linestyle="--")
			


	#2x2 matrices 
	if(((len(list(a_dicc.keys())) == 2) and (len(list(b_dicc.keys())) == 2))):
		anychange = True
		#matrices with mixed strategies
		if(ismixed):
			ax1.hlines(ne_b[-1],0,1, color="blue", linewidth=4, linestyle="-.")
			ax1.vlines(ne_a[-1],0,1, color="red", linewidth=4, linestyle="--")
			
			if((eval_list[0] == True) and (eval_list[1] == True) or (eval_list[0] == False) and (eval_list[1] == False)):
				if((eval_list[0] == True) and (eval_list[1] == True)):
					ax1.vlines(1,0,1, color="blue", linewidth=4, linestyle="-.")
				else:
					ax1.vlines(0,0,1, color="blue", linewidth=4, linestyle="-.")
			
			else:
				if(eval_list[0] == True):
					ax1.vlines(1,ne_b[-1],0, color="blue", linewidth=4, linestyle="-.")
					ax1.vlines(0,ne_b[-1],1, color="blue", linewidth=4, linestyle="-.")
				else:
					ax1.vlines(1,ne_b[-1],1, color="blue", linewidth=4, linestyle="-.")
					ax1.vlines(0,ne_b[-1],0, color="blue", linewidth=4, linestyle="-.")



			if((eval_list[2] == True) and (eval_list[3] == True) or (eval_list[2] == False) and (eval_list[3] == False)):
				if((eval_list[2] == True) and (eval_list[3] == True)):
					ax1.hlines(1,0,1, color="red", linewidth=4, linestyle="--")
				else:
					ax1.hlines(0,0,1, color="red", linewidth=4, linestyle="--")

			else:
				if(eval_list[2] == True):
					ax1.hlines(0,ne_a[-1],1, color="red", linewidth=4, linestyle="--")
					ax1.hlines(1,ne_a[-1],0, color="red", linewidth=4, linestyle="--")
				else:
					ax1.hlines(0,ne_a[-1],0, color="red", linewidth=4, linestyle="--")
					ax1.hlines(1,ne_a[-1],1, color="red", linewidth=4, linestyle="--")


		#matrices without mixed strategies (infinite number)
		if((not ismixed) and (p_notmixed != "No")):

			if(isatheproblem):
				ax1.add_patch(patches.Rectangle((0,0),1,1, color="blue"))
				ax1.vlines(p_notmixed,0,1, color="red", linewidth=4, linestyle="--")
				if((eval_list[2] == True) and (eval_list[3] == True) or (eval_list[2] == False) and (eval_list[3] == False)):
					if((eval_list[2] == True) and (eval_list[3] == True)):
						ax1.hlines(1,0,1, color="red", linewidth=4, linestyle="--")
					else:
						ax1.hlines(0,0,1, color="red", linewidth=4, linestyle="--")

				else:
					if(eval_list[2] == True):
						ax1.hlines(0,p_notmixed,1, color="red", linewidth=4, linestyle="--")
						ax1.hlines(1,p_notmixed,0, color="red", linewidth=4, linestyle="--")
					else:
						ax1.hlines(0,p_notmixed,0, color="red", linewidth=4, linestyle="--")
						ax1.hlines(1,p_notmixed,1, color="red", linewidth=4, linestyle="--")

			else:
				ax1.add_patch(patches.Rectangle((0,0),1,1, color="red"))
				ax1.hlines(p_notmixed,0,1, color="blue", linewidth=4, linestyle="-.")
				if((eval_list[0] == True) and (eval_list[1] == True) or (eval_list[0] == False) and (eval_list[1] == False)):
					if((eval_list[0] == True) and (eval_list[1] == True)):
						ax1.vlines(1,0,1, color="blue", linewidth=4, linestyle="-.")
					else:
						ax1.vlines(0,0,1, color="blue", linewidth=4, linestyle="-.")
				
				else:
					if(eval_list[0] == True):
						ax1.vlines(1,p_notmixed,0, color="blue", linewidth=4, linestyle="-.")
						ax1.vlines(0,p_notmixed,1, color="blue", linewidth=4, linestyle="-.")
					else:
						ax1.vlines(1,p_notmixed,1, color="blue", linewidth=4, linestyle="-.")
						ax1.vlines(0,p_notmixed,0, color="blue", linewidth=4, linestyle="-.")



		if((not ismixed) and (p_notmixed == "No")):
			anychange = True
			ax1.add_patch(patches.Rectangle((0,0),1,1, color="purple"))

	if(not anychange):
		messagebox.showerror("ERROR", "Can't plot functions: only matrices with a dimension of 1 or 2 allowed (or matrices that result into a 2x2 matrix by elimination of dominated strategies)")
		raise Exception("Not a 2x2 matrix (with IEDS)")
	plt.show()
	


#shows a messagebox with all pure security strategies
def pure_security_strategies():
	show_iterated_strongly_dominated_strategies_color()

	
	min_a = []
	min_b = []
	max_a = []
	max_b = []
	msg = ""

	#finding the minimum of each row and column and then appending its maximums to a new list
	for item in a_matrix:
		min_a.append(min(item))

	for item in b_matrix:
		min_b.append(min(item))

	for i in range(len(min_a)):
		if(min_a[i] == max(min_a)):
			max_a.append(sorted(list(a_dicc.keys()))[i])

	for i in range(len(min_b)):
		if(min_b[i] == max(min_b)):
			max_b.append(sorted(list(b_dicc.keys()))[i])

	#all rows and columns without IEDS for finding the correct number when printing payoffs
	get_a_numbers()
	get_b_numbers()

	for a_item in max_a:
		for b_item in max_b:

			msg = msg + "(a"+ str(a_item+1)  + ",b" + str(b_item+1) +  ") with a secure payoff of (" + str(a_dicc[a_item][b_item])  + "," +  str(b_dicc[b_item][a_item]) + ")\n\n"

	if(msg==""):
		messagebox.showerror("Pure Security Strategies", "No pure security strategies found")
	else:
		messagebox.showinfo("Pure Security Strategies", msg)




#Same as find_mixed_ne but with swaped rows and columns. Also, only 2x2 matrices are allowed (or 2x2 by applying IEDS).
def find_mixed_security():
	show_iterated_strongly_dominated_strategies_color()
	global ismixed
	ismixed = False
	global eval_list
	eval_list = []
	global isatheproblem
	isatheproblem = False
	global p_notmixed
	p_notmixed = "No"
	sa_matrix = []
	sb_matrix = []

	#swap columns and rows of a_matrix and b_matrix for computing max number of each
	for j in range(len(a_matrix[0])):
		sa_matrix.append([])
		for i in range(len(a_matrix)):
			sa_matrix[-1].append(a_matrix[i][j])
			
	for j in range(len(b_matrix[0])):
		sb_matrix.append([])
		for i in range(len(b_matrix)):
			sb_matrix[-1].append(b_matrix[i][j])


	
	if ((len(a_matrix) != 2) or (len(b_matrix) != 2)):
		messagebox.showerror("ERROR", "Only matrices of dimension 2 are allowed (or larger dimension matrices that become a 2x2 matrix by applying IEDS)")
		raise Exception("ERROR - Not a 2x2 matrix")


	dimension = len(a_matrix) 
	a_eq_list = []
	b_eq_list = []
	for i in range(dimension - 1):
		a_each_eq = []
		b_each_eq = []
		for j in range(dimension):	
			a_each_eq.append(sa_matrix[i][j] - sa_matrix[i+1][j])
			b_each_eq.append(sb_matrix[i][j] - sb_matrix[i+1][j])
		a_eq_list.append(a_each_eq)
		b_eq_list.append(b_each_eq)
	prop_sum = [1] * dimension
	a_eq_list.append(prop_sum)
	b_eq_list.append(prop_sum)
	a_array = np.array(a_eq_list)
	b_array = np.array(b_eq_list)
	zeroes = [0] * (dimension - 1)
	zeroes.append(1)
	
	#catch error if there is no mixed security equilibrium
	try:
		isatheproblem = True
		p = np.linalg.solve(a_array, zeroes)
		isatheproblem = False
		q = np.linalg.solve(b_array, zeroes)

	except:
		if(isatheproblem):
			try:
				p_notmixed = np.linalg.solve(b_array, zeroes)
				p_notmixed = p_notmixed[0]
				#check if there is any negative value
				if((p_notmixed < 0) or (p_notmixed > 1)):
					if(eval_list[2]):
						if((sb_matrix[1][1]) > ((sb_matrix[1][0] - sb_matrix[1][1]) + sb_matrix[1][1])):
							p_notmixed = 0
						elif((sb_matrix[1][1]) < ((sb_matrix[1][0] - sb_matrix[1][1]) + sb_matrix[1][1])):
							p_notmixed = 1

					else:
						if((sb_matrix[0][1]) > ((sb_matrix[0][0] - sb_matrix[0][1]) + sb_matrix[0][1])):
							p_notmixed = 0
						elif((sb_matrix[0][1]) < ((sb_matrix[0][0] - sb_matrix[0][1]) + sb_matrix[0][1])):
							p_notmixed = 1

			except:
				pass
		else:
			p_notmixed = np.linalg.solve(a_array, zeroes)
			p_notmixed = p_notmixed[0]
		#check if there is any negative value
			if((p_notmixed < 0) or (p_notmixed > 1)):
				if(eval_list[0]):
					if((sa_matrix[1][1]) > ((sa_matrix[1][0] - sa_matrix[1][1]) + sa_matrix[1][1])):
						p_notmixed = 0
					elif((sa_matrix[1][1]) < ((sa_matrix[1][0] - sa_matrix[1][1]) + sa_matrix[1][1])):
						p_notmixed = 1

				else:
					if((sa_matrix[0][1]) > ((sa_matrix[0][0] - sa_matrix[0][1]) + sa_matrix[0][1])):
						p_notmixed = 0
					elif((sa_matrix[0][1]) < ((sa_matrix[0][0] - sa_matrix[0][1]) + sa_matrix[0][1])):
						p_notmixed = 1

		if(dimension == 2):
			pa1 = sa_matrix[0][1]
			pa2 = sa_matrix[1][1]
			pa3 = (sa_matrix[0][0] - sa_matrix[0][1]) * 1 + sa_matrix[0][1]
			pa4 = (sa_matrix[1][0] - sa_matrix[1][1]) * 1 + sa_matrix[1][1]
			eval_list.append(pa1 >= pa2)
			eval_list.append(pa3 >= pa4)
			
			pb1 = sb_matrix[0][1]
			pb2 = sb_matrix[1][1]
			pb3 = (sb_matrix[0][0] - sb_matrix[0][1]) * 1 + sb_matrix[0][1]
			pb4 = (sb_matrix[1][0] - sb_matrix[1][1]) * 1 + sb_matrix[1][1]
			eval_list.append(pb1 >= pb2)
			eval_list.append(pb3 >= pb4)
		return []
	
	else:
		
		p = list(p)
		q = list(q)
		for i in range(len(p)):
			if (p[i] == int(p[i])):
				p[i] = int(p[i])
			if (q[i] == int(q[i])):
				q[i] = int(q[i])
			p[i] = round(p[i],2)
			q[i] = round(q[i],2)
		
		
		#evaluate equations for plotting best responses later (only 2x2 matrices)
		if(dimension == 2):
			pa1 = sa_matrix[0][1]
			pa2 = sa_matrix[1][1]
			pa3 = (sa_matrix[0][0] - sa_matrix[0][1]) * 1 + sa_matrix[0][1]
			pa4 = (sa_matrix[1][0] - sa_matrix[1][1]) * 1 + sa_matrix[1][1]
			eval_list.append(pa1 >= pa2)
			eval_list.append(pa3 >= pa4)
			
			pb1 = sb_matrix[0][1]
			pb2 = sb_matrix[1][1]
			pb3 = (sb_matrix[0][0] - sb_matrix[0][1]) * 1 + sb_matrix[0][1]
			pb4 = (sb_matrix[1][0] - sb_matrix[1][1]) * 1 + sb_matrix[1][1]
			eval_list.append(pb1 >= pb2)
			eval_list.append(pb3 >= pb4)


		#check if there is any negative value
		if((p[0] < 0) or (p[1] < 0)):
			if(eval_list[0]):
				if((sa_matrix[1][1]) > ((sa_matrix[1][0] - sa_matrix[1][1]) + sa_matrix[1][1])):
					p = [0,1]
				elif((sa_matrix[1][1]) < ((sa_matrix[1][0] - sa_matrix[1][1]) + sa_matrix[1][1])):
					p = [1,0]
				else:
					return []

			else:
				if((sa_matrix[0][1]) > ((sa_matrix[0][0] - sa_matrix[0][1]) + sa_matrix[0][1])):
					p = [0,1]
				elif((sa_matrix[0][1]) < ((sa_matrix[0][0] - sa_matrix[0][1]) + sa_matrix[0][1])):
					p = [1,0]
				else:
					return []

		if((q[0] < 0) or (q[1] < 0)):
			if(eval_list[2]):
				if((sb_matrix[1][1]) > ((sb_matrix[1][0] - sb_matrix[1][1]) + sb_matrix[1][1])):
					q = [0,1]
				elif((sb_matrix[1][1]) < ((sb_matrix[1][0] - sb_matrix[1][1]) + sb_matrix[1][1])):
					q = [1,0]
				else:
					return []

			else:
				if((sb_matrix[0][1]) > ((sb_matrix[0][0] - sb_matrix[0][1]) + sb_matrix[0][1])):
					q = [0,1]
				elif((sb_matrix[0][1]) < ((sb_matrix[0][0] - sb_matrix[0][1]) + sb_matrix[0][1])):
					q = [1,0]
				else:
					return []

		ismixed = True
		return([p,q])


def show_mixed_security():
	ms = find_mixed_security()
	msg1 = "Player A strategic profile: ("
	msg2 = "Player B strategic profile: ("
	nte = "Note: if there is any strategy that is dominated (in red), it has 0 probability of being played. It won't be shown in the solution but should be considered"
	t1 = False
	t2 = False
	#check if there is no mixed security equilibria
	if (ms == []):
		messagebox.showinfo("Mixed Security Strategies", "There is no mixed security strategy or there is an infinite number. You will get better information by plotting")
		raise Exception("No mixed security strategies")

	#check if it is a pure security equilibrium
	for i in range(len(ms[0])):
		if (ms[0][i] == 1):
			t1 = True
		if (ms[1][i] == 1):
			t2 = True
		if (t1 and t2):
			messagebox.showinfo("Mixed Security Strategies", "The mixed security strategy that have been found results to be a pure security strategy. Use 'Pure Security Strategies' to find it")
			raise Exception("ERROR - Not a Mixed Security Strategies")

	#show messagebox with the mixed strategies equilibria
	for i in range(len(ms[0])):
		msg1 = msg1 + str(ms[0][i]) + ","
		msg2 = msg2 + str(ms[1][i]) + ","
	msg1 = msg1[:-1] + ")\n\n"
	msg2 = msg2[:-1] + ")"
	messagebox.showinfo("Mixed Security Strategies", msg1 + msg2 + "\n\n\n\n" + nte + "\n\nAlso, use plot function to check if there is an infinite number of mixed security strategies")





#Plot minimum functions for mixed security strategies
def plot_mixed_security():
	ms = find_mixed_security()
	anydominated = False


	fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(11,7))
	fig.suptitle("Plot minimum functions for mixed security strategies", fontsize=20)
	x = np.linspace(0,1,1000)

	
	ax1.set_title("Player A", fontsize=15)
	ax2.set_title("Player B", fontsize=15)
	ax1.set(xlabel="p", ylabel='$U_A$')
	ax2.set(xlabel='q', ylabel='$U_B$')
	ax1.grid(linestyle="--")
	ax2.grid(linestyle="--")
	fig.subplots_adjust(wspace=0.3, hspace=1.5)
	sa_matrix = []
	sb_matrix = []

	blue_patch = patches.Patch(color="blue", label="W1(p)")
	red_patch = patches.Patch(color="red", label="W2(q)")
	ax1.legend(handles=[blue_patch], loc="lower right")
	ax2.legend(handles=[red_patch], loc="lower right")
	
	#swap columns and rows of a_matrix and b_matrix for computing max number of each
	for j in range(len(a_matrix[0])):
		sa_matrix.append([])
		for i in range(len(a_matrix)):
			sa_matrix[-1].append(a_matrix[i][j])
			
	for j in range(len(b_matrix[0])):
		sb_matrix.append([])
		for i in range(len(b_matrix)):
			sb_matrix[-1].append(b_matrix[i][j])



	if(ms == []):
		
		if(p_notmixed=='No'):
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(x, x*item1[0] + item1[1], linewidth=4, color="b")
			item2 = get_prop_equation(sb_matrix[0])
			ax2.plot(x, x*item2[0] + item2[1], linewidth=4, color="r")
			
			fig.show()
			raise Exception("Finished, already solved")

		if(isatheproblem):
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(x, x*item1[0] + item1[1], linewidth=4, color="b")
			if(p_notmixed == 1):
				if(eval_list[2]):
					item1 = get_prop_equation(sb_matrix[1])
					ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
				else:
					item1 = get_prop_equation(sb_matrix[0])
					ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
			
			elif(p_notmixed == 0):
				if(eval_list[3]):
					item1 = get_prop_equation(sb_matrix[1])
					ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
				else:
					item1 = get_prop_equation(sb_matrix[0])
					ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
			else:
				linx1 = np.linspace(0,p_notmixed,1000)
				linx2 = np.linspace(p_notmixed,1,1000)
				if(eval_list[2]):
					item1 = get_prop_equation(sb_matrix[1])
					ax2.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="r")
					item1 = get_prop_equation(sb_matrix[0])
					ax2.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="r")
				else:
					item1 = get_prop_equation(sb_matrix[0])
					ax2.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="r")
					item1 = get_prop_equation(sb_matrix[1])
					ax2.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="r")

			fig.show()
			raise Exception("Finished, already solved")


		if((not isatheproblem) and (not ismixed)):
			item1 = get_prop_equation(sb_matrix[0])
			ax2.plot(x, x*item1[0] + item1[1], linewidth=4, color="r")
			if(p_notmixed == 1):
				if(eval_list[0]):
					item1 = get_prop_equation(sa_matrix[1])
					ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
				else:
					item1 = get_prop_equation(sa_matrix[0])
					ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
			
			elif(p_notmixed == 0):
				if(eval_list[1]):
					item1 = get_prop_equation(sa_matrix[1])
					ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
				else:
					item1 = get_prop_equation(sa_matrix[0])
					ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
			else:
				linx1 = np.linspace(0,p_notmixed,1000)
				linx2 = np.linspace(p_notmixed,1,1000)
				if(eval_list[0]):
					item1 = get_prop_equation(sa_matrix[1])
					ax1.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="b")
					item1 = get_prop_equation(sa_matrix[0])
					ax1.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="b")
				else:
					item1 = get_prop_equation(sa_matrix[0])
					ax1.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="b")
					item1 = get_prop_equation(sa_matrix[1])
					ax1.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="b")

			fig.show()
			raise Exception("Finished, already solved")

	#left graph (player A)
	if(ms[0][0] == 1):
		if(eval_list[0]):
			item1 = get_prop_equation(sa_matrix[1])
			ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
		else:
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")


	elif(ms[0][0] == 0):
		if(eval_list[1]):
			item1 = get_prop_equation(sa_matrix[1])
			ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
		else:
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(x,x*item1[0] + item1[1], linewidth=4, color="b")
	
	else:	

		linx1 = np.linspace(0,ms[0][0],1000)
		linx2 = np.linspace(ms[0][0],1,1000)
		if(eval_list[0]):
			item1 = get_prop_equation(sa_matrix[1])
			ax1.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="b")
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="b")
		else:
			item1 = get_prop_equation(sa_matrix[0])
			ax1.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="b")
			item1 = get_prop_equation(sa_matrix[1])
			ax1.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="b")



	#right graph (player B)
	if(ms[1][0] == 1):
		if(eval_list[2]):
			item1 = get_prop_equation(sb_matrix[1])
			ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
		else:
			item1 = get_prop_equation(sb_matrix[0])
			ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")


	elif(ms[1][0] == 0):
		if(eval_list[3]):
			item1 = get_prop_equation(sb_matrix[1])
			ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
		else:
			item1 = get_prop_equation(sb_matrix[0])
			ax2.plot(x,x*item1[0] + item1[1], linewidth=4, color="r")
	
	else:	

		linx1 = np.linspace(0,ms[1][0],1000)
		linx2 = np.linspace(ms[1][0],1,1000)
		if(eval_list[2]):
			item1 = get_prop_equation(sb_matrix[1])
			ax2.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="r")
			item1 = get_prop_equation(sb_matrix[0])
			ax2.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="r")
		else:
			item1 = get_prop_equation(sb_matrix[0])
			ax2.plot(linx1,linx1*item1[0] + item1[1], linewidth=4, color="r")
			item1 = get_prop_equation(sb_matrix[1])
			ax2.plot(linx2,linx2*item1[0] + item1[1], linewidth=4, color="r")



	fig.show()




"""

BUTTONS AND LAYOUT

"""



#Creates Window with all the information of the games
def create_games_window():
	window = Toplevel(root)
	window.iconbitmap("files/logo_upf.ico")
	window.title("Choose an option")
	

	description = Label(window, text=" ", wraplength=500, font='Verdana 10', justify="center", width=70)
	description.grid(row=0, column=5, columnspan=50, rowspan=5)

	#When hover over the button, show the detailed description
	def on_enter(e):
		description['text'] = games[buttons.index(e.widget)]['Description']
		
	def on_leave(e):
   		description['text'] = ' '

	def click(e):
		write_game(buttons.index(e.widget))

	def quit_games_window():
   		window.destroy()

   	#Make the matrix ready to insert the numbers and insert them 
	def write_game(game_index):

		clear_matrix()
		clear_dominated_color()
		clear_number_color()
		row_size = games[game_index]["Size"]
		col_size = games[game_index]["Size"]
		
		while ((rows - 2) > row_size):
			delete_row()
		while ((rows - 2) < row_size):
			add_row()		
		while ((columns - 1) > col_size):
			delete_column()
		while ((columns - 1) < col_size):
			add_column()
		

		value_list = games[game_index]["Value"].split(",")
		j = 0
		for row in matrix:
			for column in row:
				column[1].insert(0, int(value_list[j]))
				j += 1
				column[3].insert(0, int(value_list[j]))
				j += 1



	#Create a button for each game using the JSON file
	buttons = []
	for i in range(len(games)):
		button_frame1 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
		buttonframe1 = button_frame1.grid(padx=5, pady=5, row=i, column=1)
		btn = Button(button_frame1, text=games[i]['Name'], command=lambda:[quit_games_window()], width=15, height=4, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
		btn.grid()		
		buttons.append(btn)
		btn.bind("<Enter>", on_enter)
		btn.bind("<Leave>", on_leave)
		btn.bind("<Button-1>", click)




#Place games button on the grid
button_frame15 = Frame(root, highlightthickness=2, bd=2, bg="#C90A2B")
buttonframe15 = button_frame15.grid(padx=5, pady=5, row=1000, column=10, columnspan=4, rowspan=3)
games_button = Button(button_frame15, text="Games", command=create_games_window, relief="flat", font="Arial 8 bold")
games_button.grid()









#Tools window
def create_button_window():
	window = Toplevel(root)
	window.iconbitmap("files/logo_upf.ico")
	window.title("Choose an option")
	
	button_frame1 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe1 = button_frame1.grid(padx=8, pady=8, row=3, column=1)
	button_frame2 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe2 = button_frame2.grid(padx=8, pady=8, row=3, column=2)
	button_frame3 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe3 = button_frame3.grid(padx=8, pady=8, row=2, column=2)
	button_frame4 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe4 = button_frame4.grid(padx=8, pady=8, row=2, column=1)
	button_frame5 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe5 = button_frame5.grid(padx=8, pady=8, row=1, column=2)
	button_frame6 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe6 = button_frame6.grid(padx=8, pady=8, row=1, column=1)
	button_frame30 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe30 = button_frame30.grid(padx=8, pady=8, row=1, column=3)
	button_frame31 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe31 = button_frame31.grid(padx=8, pady=8, row=2, column=3)
	button_frame32 = Frame(window, highlightthickness=3, bd=3, bg="#C90A2B")
	buttonframe32 = button_frame32.grid(padx=8, pady=8, row=3, column=3)

	def quit_action_window():
		window.destroy()
		

	btn12 = Button(button_frame1, text="Plot optimal responses of each player to a mixed strategy", command=lambda:[quit_action_window(),compute_optimal_line()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn12.grid()

	btn11 = Button(button_frame2, text="Plot Nash Equilibria in mixed strategies (best response functions)", command=lambda:[quit_action_window(),plot_best_response()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn11.grid()

	btn10 = Button(button_frame3, text="Mixed Nash Equilibrium", command=lambda:[quit_action_window(),show_mixed_ne()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn10.grid()

	btn8 = Button(button_frame4, text="Pure Nash Equilibria", command=lambda:[quit_action_window(),show_pure_ne()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn8.grid()

	btn9 = Button(button_frame5, text="Iterated Elimination of Dominated Strategies", command=lambda:[quit_action_window(),show_iterated_strongly_dominated_strategies_message()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn9.grid()

	btn5 = Button(button_frame6, text="Dominated Strategies", command=lambda:[quit_action_window(),show_dominated()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn5.grid()

	btn30 = Button(button_frame30, text="Pure Security Strategies", command=lambda:[quit_action_window(),pure_security_strategies()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn30.grid()

	btn31 = Button(button_frame31, text="Mixed Security Strategies", command=lambda:[quit_action_window(),show_mixed_security()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn31.grid()		

	btn32 = Button(button_frame32, text="Plot minimum functions for mixed security strategies", command=lambda:[quit_action_window(),plot_mixed_security()], width=20, height=5, justify="center", wraplength=150, font="Verdana 10 bold", relief="flat", activebackground="#D36779")
	btn32.grid()

#About button
def show_about():
	msg = "Hi I'm Pol, the developer of this project. This software began to be developed in January 2020. You are currently using version 0.8 (released March 2020) and there are still some functionalities to be implemented in the future. \n\nCheck out my Github profile for more information:\nwww.github.com/Pol-Puig/Game-Theory-Toolkit\n\nFor any issue related to this program or any other matter, feel free to contact me:\ncontact@polpuig.com\n\n\nThank you for using my software!!!\n\n" 
	messagebox.showinfo("ABOUT", msg)

about_btn = Button(root, text="Created by: Pol Puig", command=show_about, relief="ridge", font="Verdana 7 bold")
about_btn.grid(row=0,column=1000, sticky=NE)



button_frame7 = Frame(root, highlightthickness=3, bd=3, bg="#C90A2B")
buttonframe7 = button_frame7.grid(padx=8, pady=8, row=1000, column=6, columnspan=5, rowspan=3)
button_frame8 = Frame(root, highlightthickness=3, bd=1, bg="#C90A2B")
buttonframe8 = button_frame8.grid(padx=8, pady=8, row=1000, column=2, columnspan=5)
button_frame9 = Frame(root, highlightthickness=3, bd=1, bg="#C90A2B")
buttonframe9 = button_frame9.grid(padx=8, pady=8, row=1000, column=1, columnspan=3)
button_frame10 = Frame(root, highlightthickness=3, bd=1, bg="#C90A2B")
buttonframe10 = button_frame10.grid(padx=8, pady=0, row=1, column=1000, rowspan=2, sticky=S)
button_frame11 = Frame(root, highlightthickness=3, bd=1, bg="#C90A2B")
buttonframe11 = button_frame11.grid(padx=8, pady=(0,30), row=3, column=1000, rowspan=1, sticky=N)
button_frame12 = Frame(root, highlightthickness=3, bd=1, bg="#C90A2B")
buttonframe12 = button_frame12.grid(padx=8, pady=8, row=4, column=1000, rowspan=2)
button_frame13 = Frame(root, highlightthickness=3, bd=5, bg="#C90A2B")
buttonframe13 = button_frame13.grid(padx=8, pady=8, row=0, column=0, columnspan=10, rowspan=2)


#title
title_label = Label(button_frame13, text="Normal Form Game", font="Arial 18 bold")
title_label.grid()


action_button = Button(button_frame7, text="Tools", command=create_button_window, relief="flat", font="Arial 12 bold")
action_button.grid()

btn1 = Button(button_frame8, text="Delete Row", command=delete_row, relief="flat")
btn1.grid()

btn2 = Button(button_frame9, text="Add Row",command=add_row, relief="flat")
btn2.grid()

btn3 = Button(button_frame10, text="Add Column", command=add_column, relief="flat")
btn3.grid()

btn4 = Button(button_frame11, text="Delete Column", command=delete_column, relief="flat")
btn4.grid()

btn7 = Button(button_frame12, text="Clear matrix", command=clear_matrix, relief="flat", bg="#D36779")
btn7.grid()


#Randomize grid
frame = LabelFrame(root, text="Randomize numbers")
frame.grid(row=1000, column=1000)

btn6 = Button(frame, text="Randomize", command=randomize)
btn6.grid(row=2, column=1, rowspan=2)

rand_label = Label(frame, text="Write range:")
rand_label.grid(sticky=E, columnspan=2, row=1, column=2)

rand_label1 = Label(frame, text="Lower limit:")
rand_label1.grid(row=2, column=2)

rand_label2 = Label(frame, text="Upper limit:")
rand_label2.grid(row=3, column=2)

first = Entry(frame, width=3)
first.grid(row=2, column=3)

last = Entry(frame, width=3)
last.grid(row=3, column=3)


root.mainloop()
