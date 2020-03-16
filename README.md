# Game-Theory-Toolkit

This project is about making a toolkit to help people interested in Game Theory solve some of the most common topics. The main idea was just to create an interective matrix that could find pure Nash Equilibria and not much more. But the interest I have in this project has made me try to develope more tools and make the project more complete. Now it is even possible to plot some of the functions covered in Game Theory.

The project is written in Python. I've chosen this language because, in my point of view, it is fairly easy to learn and has extraordinary libraries. It is also my favorite language that I've worked with so far.

The Python libraries that I have used are 'matplotlib' and 'numpy'. For the GUI, I've used 'Tkinter'. Its basic grid system has made it possible to allocate the matrix in the space and easily modify its dimension. I'm aware that some of the code is not well optimized and there are plenty of bad programming practices that I will improve in the future.



## Tools

* Iterated elimination of dominated strategies. Marks in red the columns and rows that have been eliminated. If there is a solution by applying this method, it shows it.
* Show dominated strategies. Marks in red the dominated strategies and in orange the weakly dominated strategies. Shows in a message box the strategies that are being dominated and by which strategies are being dominated.
* Find pure Nash Equilibria. Looks for Nash Equilibria and shows their strategies in a message box. It also changes the color of the optimal response of each strategy to yellow in the matrix.
* Find mixed Nash Equilibrium. A message box indicates the mixed Nash Equilibrium. It also tells you if the Mixed Nash Equilibrium it is a pure nash equilibrium or it shows an error if there is no Mixed Nash Equilibrium.
* Plot optimal response of each player to a mixed strategy. Maximum of 2x2 matrices or matrices that after the IEDS have a dimension of 2 or less. If there is any dominated strategy, it will only be plotted if the original matrix is 2x2 (not possible to plot all the dominated lines)
* Plot best response functions. Plot best response functions depending on the optimal response of each player to a a mixed strategy



## Future development

* Add tool: Iterated elimination of weakly dominated strategies.
* Add tool: Rationalizable strategies. Marks on the matrix and finds solution (if exists).
* Add tool: Pure security strategies (maxminimization). Find payoffs.
* Add tool: Mixed security strategies. Plot and find probabilities.
* Improve overall 'badly' written code.
* Improve User Interface by making it more friendly and better color combining.
* Add a database containing 'famous' games.



## Known issues

* When plotting Nash Equilibria in mixed strategies, the main window freezes and is not possible to do anything before closing the figure window.
