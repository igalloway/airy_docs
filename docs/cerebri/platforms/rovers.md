# Rovers Overview

CogniPilot Airy currently supports rovers navigating in 2D environments. The B3RB and the ELM4 are the rovers supported for this release. We will focus on the nodes that compose the B3RB.
The [app/b3rb](https://github.com/CogniPilot/cerebri/tree/25497bf9960c6ca74e98c1709d34c756ac4395a9/app/b3rb) folder contains all nodes.


## B3RB

### Nodes

* **estimate.c**: The estimation node uses 2D odometry and is meant to be integrated with a 2D LiDAR on the companion computer. It uses the wheel odometry and the z-axis gyroscope to predict the vehicle position. Using the z-axis gyro and integrating this means that the vehicle must be calibrated to achieve best performance, or angular drift will occur. This estimator does not include an online gyro bias estimation. The system automatically calibrates at boot, but if you have bumped the system, this can degrade performance. It is always best to calibrate before starting the advanced navigation stack on the onboard computer.
* **fsm.c**: The Finite State Machine (FSM) node, manages the logic for arming and switching modes. It also publishes the vehicle status message that includes these modes and other important information regarding the vehicle fuel level (battery state), and the status of the safety switch.
* **lighting.c**: The lighting node listens to the status messages published by the FSM and publishes an LED message to drive the lights.
* **manual.c**: The manual node listens to the user joy input, through the ethernet link and publishes a corresponding synapse\_msgs\_Twist message.
* **position.c**: The position node will publish a /cmd\_vel synapse\_msgs\_Twist message.
* **velocity.c**: The velocity node listens to /cmd\_vel "Twist" message and sends commands to the motor and steering servo on the rover.

## Other Source Code
* **main.c**: At boot displays the version and CogniPilot logo.
* **mixing.c**: Mixing from /cmd\_vel to Ackermann steering.

## ELM4

The ELM4 is similar to the B3RB but instead of using Ackermann steering, it uses differential drive to steer.
The ELM4 nodes are similar to the B3RB nodes. We will highlight any differences here.

* **mixing.c**: Mixing from /cmd\_vel to differential drive steering.
