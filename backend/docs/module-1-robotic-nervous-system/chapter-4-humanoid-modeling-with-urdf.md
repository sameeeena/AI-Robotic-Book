# Chapter 4: Humanoid Modeling with URDF

To effectively control and simulate humanoid robots, it is essential to have an accurate and detailed digital representation of their physical structure. This is where the Unified Robot Description Format (URDF) comes into play. URDF is an XML-based file format used in ROS to describe all aspects of a robot, from its kinematics and dynamics to its visual appearance and collision properties. This chapter will introduce you to URDF and demonstrate its importance in the context of humanoid robotics.

## Introduction to URDF (Unified Robot Description Format)

**URDF** stands for **Unified Robot Description Format**. It is an XML-based file format used to describe all aspects of a robot's physical model. Developed specifically for ROS, URDF allows you to define the geometric and kinematic properties of a robot, which are crucial for:

*   **Simulation**: Accurately simulating the robot's behavior in physics engines (e.g., Gazebo, Isaac Sim).
*   **Visualization**: Displaying the robot's model in tools like `rviz2`.
*   **Motion Planning**: Generating collision-free paths for the robot's limbs.
*   **Control**: Implementing inverse kinematics and dynamics for precise manipulation and locomotion.

For humanoid robots, URDF is indispensable. A humanoid robot's complex structure, with numerous joints and links mimicking the human body, demands a precise description for any meaningful control or simulation task.

## Importance of accurate robot models for simulation and control

An accurate URDF model is the foundation for almost any advanced robotic application.

**For Simulation:**
*   **Realistic Physics**: Simulators rely on the URDF's mass, inertia, and joint properties to accurately calculate forces, torques, and collisions.
*   **Sensor Simulation**: The relative positions of simulated sensors (cameras, LiDAR) defined in the URDF are used to generate realistic sensor data.
*   **Behavioral Testing**: Allows for testing complex behaviors (e.g., walking, grasping) in a safe, repeatable, and accelerated virtual environment before deployment on real hardware.

**For Control:**
*   **Kinematics**: Calculating the position and orientation of end-effectors (e.g., hands, feet) given joint angles (forward kinematics), or determining joint angles required to reach a target pose (inverse kinematics).
*   **Dynamics**: Understanding how forces and torques affect the robot's motion, essential for stable locomotion and manipulation.
*   **Collision Detection**: Identifying potential collisions between robot parts or with the environment, vital for safe operation.

Without an accurate URDF, simulations would be unrealistic, and control algorithms would be ineffective or even dangerous.

## Anatomy of a URDF file: links, joints, properties

A URDF file primarily consists of `<link>` and `<joint>` elements, defining the robot's body segments and their connections.

*   **`<link>`**: Represents a rigid body segment of the robot.
    *   **`inertial`**: Defines the mass, center of mass, and inertia tensor. Critical for physics simulation.
    *   **`visual`**: Describes the appearance of the link (e.g., shape, color, mesh file). Used for visualization.
    *   **`collision`**: Defines the collision geometry of the link. Used for collision detection in simulations and motion planning. This can be simpler than the visual geometry to save computational resources.

*   **`<joint>`**: Describes the connection between two links.
    *   **`name`**: Unique identifier for the joint.
    *   **`type`**: Specifies the joint's degrees of freedom (e.g., `revolute`, `continuous`, `prismatic`, `fixed`, `floating`, `planar`). For humanoid robots, `revolute` (rotating joints like knees, elbows) and `fixed` (rigid connections) are common.
    *   **`parent`**: The name of the link closer to the robot's base.
    *   **`child`**: The name of the link further from the robot's base.
    *   **`origin`**: Defines the joint's position and orientation relative to the parent link.
    *   **`axis`**: For revolute/prismatic joints, specifies the axis of rotation or translation.
    *   **`limit`**: Defines the upper and lower limits of joint movement, velocity, and effort.

### Example: A Simple Humanoid Leg Segment

Let's illustrate with a simplified URDF snippet for a hip-to-knee segment:

```xml
<?xml version="1.0"?>
<robot name="simple_humanoid_leg">

  <link name="base_link"/>

  <joint name="hip_joint" type="revolute">
    <parent link="base_link"/>
    <child link="thigh_link"/>
    <origin xyz="0 0 0"/>
    <axis xyz="0 1 0"/> <!-- Rotation around Y-axis -->
    <limit lower="-1.57" upper="1.57" effort="100" velocity="1.0"/>
  </joint>

  <link name="thigh_link">
    <visual>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <geometry>
        <box size="0.05 0.05 0.5"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 0.8 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <geometry>
        <box size="0.05 0.05 0.5"/>
      </geometry>
    </collision>
    <inertial>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <mass value="1.0"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <joint name="knee_joint" type="revolute">
    <parent link="thigh_link"/>
    <child link="shin_link"/>
    <origin xyz="0 0 -0.5"/> <!-- At the end of the thigh_link -->
    <axis xyz="0 1 0"/>
    <limit lower="0.0" upper="2.0" effort="100" velocity="1.0"/>
  </joint>

  <link name="shin_link">
    <visual>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <geometry>
        <box size="0.04 0.04 0.5"/>
      </geometry>
      <material name="red">
        <color rgba="0.8 0 0 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <geometry>
        <box size="0.04 0.04 0.5"/>
      </geometry>
    </collision>
    <inertial>
      <origin xyz="0 0 -0.25" rpy="0 0 0"/>
      <mass value="0.8"/>
      <inertia ixx="0.008" ixy="0.0" ixz="0.0" iyy="0.008" iyz="0.0" izz="0.008"/>
    </inertial>
  </link>

</robot>
```

This snippet defines a `base_link` (often a fixed reference), a `thigh_link` connected by a `hip_joint`, and a `shin_link` connected to the `thigh_link` by a `knee_joint`. Each link has visual, collision, and inertial properties.

## Using Xacro for modular and readable URDF files

As robots become more complex, especially humanoids, URDF files can grow very large and become difficult to manage. **Xacro** (XML Macros) is an XML macro language that allows you to use macros, properties, and arithmetic operations within your URDF files, making them more modular, readable, and reusable.

**Benefits of Xacro:**
*   **Modularity**: Define common components (e.g., a standard joint, a sensor) once and reuse them throughout the robot description.
*   **Parameterization**: Use variables to define dimensions, masses, or other properties, making it easy to adjust the robot's characteristics without manually editing every value.
*   **Readability**: Breaks down complex robot descriptions into smaller, more manageable files.

**Example Xacro snippet:**
Instead of hardcoding dimensions, you can use properties:

```xml
<?xml version="1.0"?>
<robot name="my_humanoid" xmlns:xacro="http://ros.org/xacro">

  <xacro:property name="thigh_length" value="0.5"/>
  <xacro:property name="thigh_radius" value="0.025"/>
  <xacro:property name="thigh_mass" value="1.0"/>

  <link name="thigh_link">
    <visual>
      <geometry>
        <cylinder length="${thigh_length}" radius="${thigh_radius}"/>
      </geometry>
    </visual>
    <inertial>
      <mass value="${thigh_mass}"/>
      <!-- ... inertia calculation based on geometry ... -->
    </inertial>
  </link>

</robot>
```
Xacro files (`.urdf.xacro`) are processed into standard `.urdf` files before being used by ROS 2 tools.

## Visualizing URDF models in `rviz2`

`rviz2` is the primary 3D visualization tool in ROS 2. It can load URDF models and display them, along with sensor data, robot poses, and more. Visualizing your robot model is crucial during development to ensure its geometry, joint limits, and coordinate frames are correctly defined.

**Steps to visualize a URDF in `rviz2`:**
1.  Launch `rviz2`: `ros2 run rviz2 rviz2`
2.  In the `Displays` panel, click `Add`.
3.  Choose `RobotModel` and click `OK`.
4.  In the `RobotModel` properties, ensure the `Description Source` is set to `Robot Description` and `Description Topic` points to `/robot_description` (or the parameter name where your URDF is loaded).
5.  Load your URDF file into the `robot_description` parameter. This is typically done via a ROS 2 launch file that uses `robot_state_publisher`.

## Integrating URDF models into ROS 2

To make a URDF model available to ROS 2, it needs to be parsed and published on the `/robot_description` topic. This is handled by the `robot_state_publisher` node.

**`robot_state_publisher`:**
This node reads the URDF from the `robot_description` parameter and, based on the current joint states (published on `/joint_states` topic), calculates the 3D poses of all links and publishes them as `tf2` transformations. These transformations are used by `rviz2` and other ROS 2 components to understand the robot's current configuration.

A typical launch file to bring up your robot model in ROS 2 might look like this (conceptual `my_robot.launch.py`):

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Path to your URDF file
    urdf_file_name = 'humanoid.urdf' # Or 'humanoid.urdf.xacro'
    urdf_path = os.path.join(
        get_package_share_directory('my_humanoid_description'),
        'urdf',
        urdf_file_name)

    # If using Xacro, process it
    # from xacro import process_file
    # doc = process_file(urdf_path)
    # robot_desc = doc.toprettyxml(indent='  ')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}] # Use processed Xacro or raw URDF
        ),
        Node(
            package='joint_state_publisher_gui', # For manually controlling joints with a GUI slider
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        # Node for Rviz2 visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('my_humanoid_description'), 'rviz', 'config.rviz')]
        )
    ])
```
This setup allows you to visualize your humanoid robot, manipulate its joints (via `joint_state_publisher_gui`), and see the resulting transformations in `rviz2`.

## Key Takeaways

*   **URDF** is an XML-based format for describing robot kinematics, dynamics, visual, and collision properties.
*   Accurate URDF models are critical for **realistic simulation**, **motion planning**, and **precise control** of complex robots like humanoids.
*   URDF files are structured with **`<link>`** elements (rigid bodies with inertial, visual, collision properties) and **`<joint>`** elements (connections between links with type, parent/child, origin, axis, and limits).
*   **Xacro** simplifies complex URDFs through modularity, parameterization, and improved readability.
*   **`rviz2`** is the primary tool for visualizing URDF models and verifying their correct definition.
*   **`robot_state_publisher`** integrates URDF models into ROS 2 by publishing link transformations based on joint states.