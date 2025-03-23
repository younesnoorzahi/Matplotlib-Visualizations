import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81  # acceleration due to gravity (m/s^2)
L = 1.0   # length of the pendulum (m)
theta0 = np.pi / 4  # initial angle (radians)
omega0 = 0.0        # initial angular velocity (rad/s)
t_max = 10.0        # maximum time (s)
dt = 0.01           # time step (s)

# Initial conditions
theta = theta0
omega = omega0
t = 0.0

# Lists to store the results
time = []
angles = []
angular_velocities = []

# Euler method integration
while t <= t_max:
    # Append current state to the lists
    time.append(t)
    angles.append(theta)
    angular_velocities.append(omega)
    
    # Update angular velocity and angle
    alpha = -(g / L) * np.sin(theta)  # angular acceleration
    omega += alpha * dt
    theta += omega * dt
    
    # Update time
    t += dt

# Convert lists to numpy arrays for easier manipulation
time = np.array(time)
angles = np.array(angles)
angular_velocities = np.array(angular_velocities)

# Plot the results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, angles, label='Angle (rad)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, angular_velocities, label='Angular Velocity (rad/s)', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
