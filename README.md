<h1>pendulum in Python</h1>
<p>To simulate a pendulum in Python, you can use various libraries such as matplotlib for visualization and numpy for numerical computations. Below is an example of how to simulate a simple pendulum using the Euler method for numerical integration.</p>

<h1>Step 1: Install Required Libraries</h1>
<p>First, make sure you have the necessary libraries installed. You can install them using pip:</p>

```pip install numpy matplotlib```

<span>Step 2: Write the Pendulum Simulation Code in this File (Simulation Code.py)</span>


<h1>Explanation:</h1>

- <h3>Parameters:</h3>

<ul>
  <li>g is the acceleration due to gravity.</li>
  <li>L is the length of the pendulum.</li>
  <li>theta0 is the initial angle of the pendulum.</li>
  <li>omega0 is the initial angular velocity.</li>
  <li>t_max is the maximum time for the simulation.</li>
  <li>dt is the time step for the Euler method.</li>
</ul>

<h1>Euler Method:</h1>

<ul>
  <li>The angular acceleration alpha is calculated using the pendulum equation: 
α
=
−
g
L
sin
⁡
(
θ
)
α=− 
L
g
​
 sin(θ).</li>
  <li>The angular velocity omega and angle theta are updated using the Euler method:</li>
  <li>ω
=
ω
+
α
⋅
d
t
ω=ω+α⋅dt</li>
  <li>θ
=
θ
+
ω
⋅
d
t
θ=θ+ω⋅dt</li>
</ul>

<h1>Plotting:</h1>
<li>The angle and angular velocity are plotted against time.</li>


<h1>Step 3: Run the Code</h1>
<p>Run the code in your Python environment. You should see two plots: one showing the angle of the pendulum over time, and the other showing the angular velocity over time.</p>

 <h1>Notes:</h1>

 <li>The Euler method is simple but not the most accurate for long simulations. For better accuracy, consider using more advanced numerical methods like the Runge-Kutta method.</li>
 <li>The simulation assumes a small damping factor (none in this case), which is why the pendulum oscillates indefinitely. In reality, air resistance and friction would cause the pendulum to slow down over time.</li>
