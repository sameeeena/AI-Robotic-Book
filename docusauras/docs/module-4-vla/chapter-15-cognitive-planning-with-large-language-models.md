---
sidebar_position: 15
---

# Cognitive Planning with Large Language Models

## From Text to Task: The Reasoning Engine

We have successfully converted a user's voice into text ("Get me the apple from the table") and have a visual system that can see the apple and the table. Now comes the central question: how does the robot translate that high-level command into a concrete sequence of actions? This is the task of **cognitive planning**, and it's where Large Language Models (LLMs) are revolutionizing robotics.

Traditionally, robot task planning has relied on complex, hand-crafted systems like state machines or symbolic planners. These systems are powerful but brittle. They can only perform tasks for which they have been explicitly programmed and struggle with ambiguity or unexpected situations.

LLMs offer a fundamentally different approach. By leveraging their vast, pre-trained knowledge of the world, they can act as a flexible, common-sense reasoning engine, breaking down high-level goals into a series of achievable steps.

## LLMs as Task Planners

The core idea is to use an LLM as a "text-in, text-out" planner. We provide the LLM with a carefully crafted prompt that includes:

1.  **The Goal:** The user's command (e.g., "Get me the apple from the table").
2.  **The Context:** A description of the robot's current situation, including:
    *   Objects it can see (e.g., "I see an apple on the table, a chair, and a door.").
    *   Its current state (e.g., "My hand is empty.").
3.  **The Available Actions:** A list of the primitive skills or actions the robot knows how to perform (e.g., `navigate_to(object)`, `grasp(object)`, `place(object)`).

The LLM then processes this prompt and outputs a textual plan—a sequence of the available actions that will achieve the goal.

### Example Prompt:

```text
You are a helpful robot assistant. Your goal is to achieve the user's command.
You can see the following objects: apple, table, chair, user.
Your hand is currently empty.
The user's command is: "Get me the apple from the table and give it to me."

You have the following skills available:
1. navigate_to(object): Moves the robot to be near the specified object.
2. grasp(object): Grasps the specified object. Your hand must be empty.
3. give(object): Gives the object in your hand to the user.

What is the plan to achieve the goal? Output the plan as a numbered list of skills.

Plan:
```

### Expected LLM Output:

```text
1. navigate_to(table)
2. grasp(apple)
3. navigate_to(user)
4. give(apple)
```

This textual plan can then be parsed and executed by the robot's control system, which calls the corresponding low-level functions for navigation, grasping, and so on.

## The Architectural Framework

This approach creates a powerful cognitive architecture where the LLM serves as the central reasoning component.

```mermaid
graph TD
    A[User Command (Voice/Text)] --> C{Cognitive Planning Node (LLM)}
    B[Vision System (Object List)] --> C
    C -- Textual Plan --> D[Plan Execution Node]
    D -- Calls --> E(Skill Library: navigate, grasp, etc.)
    E -- Actions --> F[Robot Control System]
```

*   **Cognitive Planning Node:** This ROS 2 node is responsible for constructing the prompt, sending it to the LLM (either via an API or a locally running model), and parsing the response.
*   **Vision System:** A perception node that constantly processes camera data to identify and locate objects in the environment. It provides the "I see..." part of the prompt.
*   **Plan Execution Node:** This node receives the plan from the LLM. It acts as a sequencer, calling the robot's primitive skills one by one and monitoring their success or failure.

## Advantages of LLM-based Planning

*   **Flexibility:** The system is not limited to pre-programmed tasks. The LLM can generate plans for a vast range of commands by combining the available skills in novel ways.
*   **Common-Sense Reasoning:** LLMs can infer unstated steps. If asked to "make coffee," the model might know from its training data that this involves finding a coffee machine, a mug, and pressing a button, even if those steps aren't explicitly mentioned.
*   **Error Recovery:** If a step in the plan fails (e.g., the grasp action fails), the Plan Execution Node can report the failure back to the LLM. The LLM can then be re-prompted with the new context ("My grasp of the apple failed.") to generate a new, corrective plan (e.g., "Try grasping the apple again.").
*   **Multi-modal Integration:** This framework naturally integrates vision and language. The LLM's plan is directly grounded in what the robot currently sees, making it highly adaptive to the immediate environment.

## Prompt Engineering: The Key to Success

The performance of an LLM-based planner is highly dependent on the quality of the prompt. **Prompt engineering** is the art and science of crafting prompts that elicit the desired behavior from the LLM. For robotic planning, this involves:

*   **Clear Instructions:** Telling the LLM its role ("You are a robot assistant") and its goal.
*   **Structured Context:** Providing the world state and available actions in a clear, easy-to-parse format.
*   **Few-Shot Examples:** Including one or two examples of a command and the correct plan in the prompt can significantly improve the LLM's performance.
*   **Constraining the Output:** Explicitly asking the LLM to only use the skills provided and to output the plan in a specific format (e.g., a numbered list).

## Key Takeaways

*   **Large Language Models (LLMs)** can be used as powerful, flexible cognitive planning engines for robots.
*   By providing the LLM with a **prompt** containing the goal, context (from vision), and available actions, it can generate a textual plan to achieve the goal.
*   This approach enables **flexibility**, **common-sense reasoning**, and **error recovery** in a way that is difficult to achieve with traditional planning methods.
*   A robust cognitive architecture separates the LLM planner from the vision system and the plan execution system, often using ROS 2 to communicate between these components.
*   **Prompt engineering** is a critical skill for developing effective LLM-based planners, as the quality of the prompt directly determines the quality of the generated plan.