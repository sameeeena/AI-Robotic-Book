---
sidebar_position: 6
title: Simple Programs for Humanoids
---

# Simple Programs for Humanoids

After understanding the hardware (sensors and actuators) and the AI perception mechanisms (vision and speech), the next logical step is to bring these components to life through programming. This chapter introduces fundamental concepts for writing simple programs that allow humanoids to perform basic tasks, bridging the gap between perception, cognition, and action.

## Programming Paradigms for Robotics

Robotics programming often involves a blend of:

*   **Imperative Programming:** Explicitly stating a sequence of commands for the robot to execute.
*   **Reactive Programming:** Designing the robot to respond immediately to changes in its environment (sensor inputs).
*   **Behavior-Based Robotics:** Combining simple, parallel behaviors (e.g., "avoid obstacles," "move towards goal") that emerge into complex actions.
*   **AI-driven Control:** Using machine learning models (e.g., reinforcement learning policies) to directly control robot actions.

For simple programs, we often start with imperative and reactive approaches.

## Basic Movement Commands

Let's imagine a simplified programming interface for a humanoid.

### Example 1: Moving Forward

```python
# Pseudo-code for a simple forward movement
def move_forward(distance_cm):
    # Command motors to drive wheels or take steps forward
    print(f"Robot moving forward by {distance_cm} cm.")
    # In a real robot, this would involve inverse kinematics,
    # joint trajectory planning, and motor control.
    # For a wheeled robot, it would be wheel velocity commands.
    robot.drive(linear_velocity=0.1, duration=distance_cm / 10) # conceptual
    robot.wait_until_movement_complete()

# Usage:
move_forward(50) # Move 50 centimeters forward
```

### Example 2: Turning

```python
# Pseudo-code for a simple turn
def turn(angle_degrees):
    # Command motors to rotate the robot
    print(f"Robot turning {angle_degrees} degrees.")
    robot.rotate(angular_velocity=0.5, angle=angle_degrees) # conceptual
    robot.wait_until_movement_complete()

# Usage:
turn(90) # Turn 90 degrees clockwise
```

## Integrating Sensors: Reactive Behaviors

Robots need to react to their environment. This is where sensors become critical.

### Example 3: Obstacle Avoidance

Using a proximity sensor (like an ultrasonic sensor or LiDAR), a robot can detect obstacles and react by stopping or turning.

```python
# Pseudo-code for basic obstacle avoidance
def navigate_with_avoidance():
    while True:
        distance_to_obstacle = robot.get_proximity_sensor_data()

        if distance_to_obstacle < 30: # If obstacle is closer than 30 cm
            print("Obstacle detected! Stopping and turning.")
            robot.stop_movement()
            turn(45) # Turn 45 degrees to avoid
            robot.move_forward_slowly(10) # Move a bit to clear the obstacle
        else:
            print("Path clear, moving forward.")
            robot.move_forward(10) # Keep moving forward
        
        time.sleep(0.5) # Check every half second

# Usage:
# navigate_with_avoidance() - This would run continuously
```

## Basic Manipulation: "Reaching for an Object"

Combining movement with a robotic arm to reach for an object.

### Example 4: Simple Reach Task

```python
# Pseudo-code for a simple reach to a known position
def reach_for_object(x, y, z):
    print(f"Robot arm reaching to position ({x}, {y}, {z})")
    
    # This involves inverse kinematics to calculate joint angles
    joint_angles = robot_arm.calculate_ik(x, y, z) 
    
    # Command the arm to move to these angles
    robot_arm.move_to_joint_angles(joint_angles, speed=0.5)
    robot_arm.wait_until_movement_complete()
    
    print("Reached target position.")

# Usage:
reach_for_object(0.3, 0.1, 0.2) # Reach to a point in 3D space (meters)
```

## Voice Command Integration

Connecting speech recognition to actions.

### Example 5: Voice-Controlled Movement

```python
# Pseudo-code for voice-controlled movement
def listen_for_commands():
    while True:
        spoken_command = robot.listen_for_speech() # Uses speech recognition
        
        if "move forward" in spoken_command:
            print("Command: Move forward")
            move_forward(20)
        elif "turn right" in spoken_command:
            print("Command: Turn right")
            turn(-90) # Negative for right turn
        elif "stop" in spoken_command:
            print("Command: Stop")
            robot.stop_movement()
            break # Exit loop
        else:
            print(f"Unrecognized command: '{spoken_command}'")
        
        time.sleep(1)

# Usage:
# listen_for_commands()
```

These examples demonstrate how simple programmatic instructions can be combined with sensor feedback and AI perception to create basic, yet effective, behaviors for humanoid robots. As complexity grows, these foundational blocks are extended with more sophisticated AI algorithms for learning and adaptation.
