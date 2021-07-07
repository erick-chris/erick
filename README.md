## Welcome!

My name is Erick and I am currently doing my Physics Bacharelor degree on University of Sao Paulo (USP). I did some projects in Python and then decided to put them all on this repository. Down below you'll find the most interesting ones.

&nbsp;  
# Project 1: Correlation in Sports (NBA)

The idea behind this project was to calculate the win/loss ratio's correlation with the population of the city it is in for the NBA using 2018 data. So here I'd to use some librarys frequently used in data analysis as pandas, numpy, scipy, regex and matplotlib. There were two datasets that I had to store, clean, slice and so on; then I was capable to extract the two lists that I needed to calculate the correlation requested. Right below is the graphic for win/loss ratio versus population of the respective city; in red you see the statistical correlation, which is almost null.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/nba_data.png?raw=True" height="320" width="450">
</p>

In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (nba.py).

&nbsp;  
# Project 2: Energy Usage in the World

This is an almost complete project towards data handling. Here I stored, cleaned, sliced and merged datasets, among other actions. The project itself is about the energy usage over all the countries in the world. I mixed up three datasets about energy usage, GDP (Gross Domestic Product) and scientific presence on energy related topics (Scimago Journal & Country Rank) and then selected the top 15 countries in the Scimago rank (the most active in energy related topics). From this merged dataset I created a scatter plot which synthetizes the overall information contained, as you can see right below. It's a bubble chart showing % Renewable (country's energy production percentage from renewable sources) vs. Rank (Scimago's rank). The size of the bubble corresponds to the countries' 2014 GDP.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/energy_plot.png?raw=True" height="400" width="610">
</p>

In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (energy_data.py).

&nbsp;  
# Project 3: Data Fitting

In this project I developed a code that, from data in a .txt file, drawn a line which connect the points of the graphic such that the parameters of the function f(x) = ax + b are the best. The function that best describes the experimental data will minimize the "chi squared". Chi squared is a statistical quantity that basically takes the difference between each point in the graphic (experimental data) and the function (the model), then sum of all these differences. Therefore is it possible to find out the parameters "a" and "b" which minimize the chi squared. The result is shown below.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/filtro%20de%20wien.png?raw=True" height="300" width="420">
</p>

In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (grafico_data1.py).

&nbsp;  
# Project 4: Pokemon Capture

Here I simulated the pokemons capture through the launch of pokeballs in a planet whose gravity aceleration is about 2 m/s^2 (2 meters per second squared). The main idea is to print out a matrix that simules the pokeball trajectory. Moreover, the matrix should include the trainer's position (the guy that launch the pokeball) and the pokemon's position as well, considering the pokemon's size. From a .txt file it was possible to extract data from pokemon's size (in number of lines and columns), name ("Nidoran", for example) and pokemon's center position. The user establishes the initial velocity and the launch angle of the pokeball. In the image below we see an output example. 

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/pokemon.png?raw=True" height="450" width="320">
</p>

In the image: "T" represents the trainer's position; "o" is the pokeball's trajectory; the numbers from 1 to 3 in the matrix represent the pokemons.
In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (pokemon.py).

&nbsp;  
# Project 5: SIR Model

The SIR model (susceptible, infected and recovered) deal with the statistical modeling of an epidemic/pandemic, like the Covid-19 pandemic. The mathematical model was developed using concepts of probability and statistic. Down below we see a simple representation of this model, which consider only the infection rate and the recover rate. To reach this result I had to establish some initial conditions that are: there are 99 susceptible people and 1 infected person.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/SIR%20model.png?raw=True" height="300" width="420">
</p>

In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (SIR model.py).

&nbsp;  
# Project 6: Particle in a box

Consider the problem of an electron in a cubic box with edge of size L, moving over only one edge (1-dimensional moviment) of the box. The electron feel a potencial V(x) = ax/L (that is, the electron experience a force inside the box). So I wanted to find out the probabilities distribution to the electron with concepts from Quantum Mechanics.

The figure below shows the line graphics from the probabilities curves for an electron moving along the x axis. There are points where the probability of find the electron is high and other points where there's no electron in the box. The states represent the quantized energies of the system; so the ground state is the state where the energy of the system - by system I mean one electron inside the box - is minimum.

<p align="center">
  <img src="https://github.com/erick-chris/erick-chris.github.io/blob/gh-pages/images/particle%20in%20a%20box-3.png?raw=True" height="300" width="420">
</p>

In [this link](https://github.com/erick-chris/erick-chris.github.io/tree/gh-pages/Python) you can find the source code of this project (hamiltoniana.py).
