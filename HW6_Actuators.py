import numpy as np
import matplotlib.pyplot as plt

#constants
g = 9.81
mu = 0.25  # assuming acrylic vs steel
l = 0.2  
acceleration_body = 0.5  # assuming constant acceleration for the body
distance = 0.15  # distance from the pivot point to the place where force is applied
k_tau = 0.1  #motor torque constant 
R = 2  # motor resistance in Ohms

#body + arm
body_weights = np.linspace(5, 50, 100)  # in kg
Fp = ((acceleration_body + mu * g) * body_weights)
t_m = distance * Fp 

#hand
mass_hand = body_weights / 4  # assuming the hand is a quarter the weight of the body
net_force_hand = (Fp - mu * g * mass_hand) 
t_hand = (Fp / 2) * l  # torque required by the hand to grasp the rod

t_total = t_m + t_hand  # total torque required by the system
I_total = t_total / k_tau
V_required = I_total * R #assuming EMF negigleble


plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(body_weights, t_total, label='Required actuator torque')
plt.title(' Actuator torque Required vs. Robot weight')
plt.xlabel('Robot weight (kg)')
plt.ylabel('Required actuator torque (Nm)')
plt.grid(True)
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(body_weights, V_required, color='orange', label='Required voltage')
plt.title('Required voltage vs. Robot weight')
plt.xlabel('Robot weight (kg)')
plt.ylabel('Required voltage (V)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
