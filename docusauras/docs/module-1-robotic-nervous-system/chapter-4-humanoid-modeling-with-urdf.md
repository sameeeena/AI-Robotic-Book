---
sidebar_position: 4
---

# Humanoid Modeling with URDF

## Giving Form to the Robotic Nervous System

Before a humanoid robot can move or interact with its environment, its physical structure must be defined and understood by the robotic software. This is where the Unified Robot Description Format (URDF) comes into play. URDF is an XML format used in ROS to describe all aspects of a robot, from its visual appearance and collision properties to its kinematic and dynamic characteristics. For complex humanoid robots, a detailed and accurate URDF model is absolutely critical.

## What is URDF?

URDF describes a robot as a set of **links** and **joints**.

*   **Links:** Represent the rigid bodies of the robot (e.g., torso, upper arm, forearm, hand, thigh, calf, foot). Each link has properties like its visual representation (mesh, color), collision properties (shape, inertia), and mass.
*   **Joints:** Define the connections between links and specify the type of motion allowed between them (e.g., `revolute` for rotating joints like elbows or knees, `fixed` for rigid connections). Joints also define the limits of motion and dynamic properties like friction.

### Why URDF for Humanoid Robots?

Humanoid robots are complex systems with many degrees of freedom. A well-structured URDF model allows roboticists to:

*   **Visualize the Robot:** Render the robot in simulation environments (like Gazebo or RViz) to understand its configuration and movement.
*   **Kinematics and Dynamics:** Perform calculations related to the robot's posture (forward kinematics) and how joint movements affect the end-effectors, or how forces affect its motion (dynamics).
*   **Collision Detection:** Define collision geometries to prevent the robot from self-colliding or colliding with its environment.
*   **Control:** Map abstract commands to specific joint movements.
*   **Modularity:** Easily add or remove sensors, end-effectors, or other components by modifying the URDF.

## Anatomy of a URDF File

A URDF file is an XML document with a root `<robot>` tag. Inside, it contains multiple `<link>` and `<joint>` tags.

### Link Definition Example

```xml
<link name="torso">
  <visual>
    <geometry>
      <box size="0.2 0.3 0.5" />
    </geometry>
    <material name="blue">
      <color rgba="0 0 0.8 1" />
    </material>
  </visual>
  <collision>
    <geometry>
      <box size="0.2 0.3 0.5" />
    </geometry>
  </collision>
  <inertial>
    <mass value="10" />
    <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0" />
  </inertial>
</link>
```
*   **`name`**: Unique identifier for the link.
*   **`visual`**: Defines how the link appears. Can use `box`, `cylinder`, `sphere`, or `mesh` (for 3D models).
*   **`collision`**: Defines the geometry used for collision detection. Often simpler than the visual geometry for computational efficiency.
*   **`inertial`**: Describes the link's physical properties: `mass` and `inertia`.

### Joint Definition Example

```xml
<joint name="torso_to_head_joint" type="revolute">
  <parent link="torso"/>
  <child link="head"/>
  <origin xyz="0 0 0.25" rpy="0 0 0"/>
  <axis xyz="0 0 1"/>
  <limit lower="-1.57" upper="1.57" effort="10" velocity="0.5"/>
</joint>
```
*   **`name`**: Unique identifier for the joint.
*   **`type`**: Specifies the joint type (`revolute`, `continuous`, `prismatic`, `fixed`, `floating`, `planar`). `revolute` is a rotating joint with a limited range.
*   **`parent`** and **`child`**: Specify the links connected by the joint.
*   **`origin`**: Defines the joint's position (`xyz`) and orientation (`rpy` - roll, pitch, yaw) relative to the parent link.
*   **`axis`**: For revolute/prismatic joints, this defines the axis of rotation/translation.
*   **`limit`**: Defines the joint's motion limits (`lower`, `upper`), maximum `effort`, and `velocity`.

## Xacro: Simplifying Complex URDFs

For humanoid robots, URDF files can become extremely long and repetitive. **Xacro** (XML Macros) is an XML macro language that allows for more concise and readable robot descriptions. It enables:

*   **Constants:** Define values (e.g., link dimensions, joint limits) once and reuse them.
*   **Macros:** Create reusable blocks of XML to define common robot components (e.g., a standard leg segment) with customizable parameters.
*   **Mathematical Expressions:** Perform calculations directly within the file.

A typical workflow involves writing the robot description in Xacro and then converting it to a standard URDF file using a `ros2 launch` file.

## Visualization and Validation

ROS provides tools like `RViz` and `urdf_to_graphiz` to visualize and validate URDF models.

*   **RViz:** A 3D visualizer for ROS. It can display the robot model, sensor data, and planned paths, allowing developers to visually inspect the URDF and robot behavior.
*   **`check_urdf`:** A command-line tool to validate the syntax and structure of a URDF file.

## Key Takeaways

*   **URDF (Unified Robot Description Format)** is an XML format for describing robot kinematics, dynamics, visual, and collision properties.
*   It defines a robot as a tree structure of **links** (rigid bodies) connected by **joints** (allowing relative motion).
*   For humanoid robots, URDF is crucial for visualization, kinematics/dynamics calculations, collision detection, and control.
*   **Xacro** simplifies complex URDFs using constants, macros, and mathematical expressions.
*   Tools like `RViz` and `check_urdf` are used for visualization and validation of robot models.