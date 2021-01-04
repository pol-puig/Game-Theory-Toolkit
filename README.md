# Game Theory Toolkit

This project is about making a toolkit to help people interested in Game Theory solve some of the most common topics. The main idea was just to create an interactive matrix that could find pure Nash Equilibria and not much more. But the interest I have in this project has made me try to develop more tools and make the project more complete. Now it is even possible to plot some of the functions covered in Game Theory.

The project is written in Python. I've chosen this language because, in my point of view, it is fairly easy to learn and has extraordinary libraries. It is also my favorite language that I've worked with so far.

The Python libraries that I have used are 'matplotlib' and 'numpy'. For the GUI, I've used 'Tkinter'. Its basic grid system has made it possible to allocate the matrix in the space and easily modify its dimension. I'm aware that some of the code is not well optimized and there are plenty of bad programming practices that I will improve in the future.



## Tools

* Iterated elimination of dominated strategies. Highlights in red the columns and rows that have been eliminated. If there is a solution by applying this method, it shows it.
* Show dominated strategies. Highlights in red the dominated strategies and in orange the weakly dominated strategies. Shows in a message box the strategies that are being dominated and by which strategies are being dominated.
* Find pure Nash Equilibria. Looks for Nash Equilibria and shows their strategies in a message box. It also changes the color of the optimal response of each strategy to yellow in the matrix.
* Find mixed Nash Equilibrium. A message box indicates the mixed Nash Equilibrium (the one that you get by solving the system of equations). It also tells you if the Mixed Nash Equilibrium it is a pure Nash equilibrium or it shows an error if there is no Mixed Nash Equilibrium. Be aware that could be infinite mixed Nash equilibria, plot best response functions for more information.
* Plot optimal response of each player to a mixed strategy. Maximum of 2x2 matrices or matrices that after the IEDS have a dimension of 2. If there is any dominated strategy, it will only be plotted if the original matrix is 2x2 (not possible to plot all the dominated lines)
* Plot best response functions. Plot best response functions depending on the optimal response of each player to a mixed strategy
* Pure security strategies. Shows a message box with the pure security strategies and their respective payoffs.
* Mixed security strategies. Shows strategic profile for both players.
* Plot minimum functions. Finds the minimum functions to have a better understanding of the mixed security strategies that players should follow.


## Future development

* Add tool: Iterated elimination of weakly dominated strategies.
* Add tool: Rationalizable strategies. Colors the matrix and finds solution (if exists).
* Add tool: Pure security strategies (maxminimization). Find payoffs.  **ADDED**
* Add tool: Mixed security strategies. Plot and find probabilities.   **ADDED**
* Improve overall 'badly' written code.
* Improve User Interface by making it more friendly and better color combining. **DONE**
* Add a database containing 'popular' games. **ADDED**
* Add more 'popular' games in the database.



## Known issues

* When plotting best response functions, the main window freezes and is not possible to do anything before closing the figure window.
* Released file is very large. Working on directory optimization to reduce software heaviness.
* Not correctly plotting best response functions when matrix dimension is bigger than 2 and applying IEDS leads to a matrix with a dimension lesser than 2. **SOLVED**
* Some grammar mistakes (mainly in the 'About' message box) **SOLVED**
* Best response functions are not plotted correctly when there is a dominated strategy and matrix of dimension 2. **SOLVED**




## Releases

**Download:** **[Game Theory Toolkit v0.9](https://github.com/Pol-Puig/Game-Theory-Toolkit/releases/download/GTT_0_9/Game_Theory_Toolkit_0_9.zip)**

Download and unzip the file. Then, run the executable file called 'Game_Theory_toolkit.exe' that is inside the folder. An antivirus warning will likely prompt. Ignore it (there are no malicious files, don't worry) and just run the executable.

<b>Note: MacOS is not yet supported although it may be possible to run it using Wine or using a virtual machine.
  
