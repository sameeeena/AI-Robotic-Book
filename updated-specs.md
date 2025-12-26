You are updating an existing project specification file (specify.md).

Context:
- The project is a technical book built with Docusaurus.
- The project already exists; DO NOT create a new project.
- Only update the book content section.
- The tech stack, RAG chatbot, and implementation details remain unchanged.

Task:
Rewrite the "Book Content / Book Structure" section of specify.md
to accurately reflect the finalized book structure.

Constraints:
- The book has exactly 4 modules.
- Each module has exactly 4 chapters (16 chapters total).
- Content must be clearly structured module-wise.
- Do NOT invent new chapters.
- Do NOT modify implementation, chatbot, or database sections.
- Use clean, professional markdown.

Input (use exactly this structure):

Module 1: <robotic-nervous-system>
Chapters:
1. <1-introduction-to-the-robotic-nervous-system>
2. <2-ros-2-nodes-topics-and-services>
3. <3-bridging-ai-agents-with-ros-using-rclpy>
4. <4-humanoid-modeling-with-urdf>

Module 2: <digital-twin>
Chapters:
5. chapter-5-digital-twins-in-physical-ai
6. ...chapter-6-physics-simulation-in-gazebo
7. ...chapter-7-human-robot-interaction-in-unity
8. ...chapter-8-sensor-simulation-for-humanoid-robots

Module 3: <ai-robot-brain>
Chapters:
9. ...chapter-9-the-ai-robot-brain
10. ...chapter-10-nvidia-isaac-sim-and-synthetic-data
11. ...chapter-11-isaac-ros-and-hardware-accelerated-vslam
12. ...chapter-12-nav2-for-bipedal-humanoid-navigation

Module 4: <vla>
Chapters:
13. ...chapter-13-vision-language-action-systems-in-physical-ai
14. ...chapter-14-voice-to-action-using-openai-whisper
15. ...chapter-15-cognitive-planning-with-large-language-models
16. ...chapter-16-capstone-the-autonomous-humanoid

Output Requirements:
- Return ONLY the updated specify.md content.
- Include:
  - Book overview
  - Module-wise chapter listing
  - Short description for each module (learning goals + outcomes)
- Ensure alignment with a RAG-enabled technical book.