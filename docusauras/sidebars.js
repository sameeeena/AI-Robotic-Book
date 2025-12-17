// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  bookSidebar: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'module-1-robotic-nervous-system/chapter-1-introduction-to-the-robotic-nervous-system',
        'module-1-robotic-nervous-system/chapter-2-ros-2-nodes-topics-and-services',
        'module-1-robotic-nervous-system/chapter-3-bridging-ai-agents-with-ros-using-rclpy',
        'module-1-robotic-nervous-system/chapter-4-humanoid-modeling-with-urdf',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'module-2-digital-twin/chapter-5-digital-twins-in-physical-ai',
        'module-2-digital-twin/chapter-6-physics-simulation-in-gazebo',
        'module-2-digital-twin/chapter-7-human-robot-interaction-in-unity',
        'module-2-digital-twin/chapter-8-sensor-simulation-for-humanoid-robots',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      items: [
        'module-3-ai-robot-brain/chapter-9-the-ai-robot-brain',
        'module-3-ai-robot-brain/chapter-10-nvidia-isaac-sim-and-synthetic-data',
        'module-3-ai-robot-brain/chapter-11-isaac-ros-and-hardware-accelerated-vslam',
        'module-3-ai-robot-brain/chapter-12-nav2-for-bipedal-humanoid-navigation',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      items: [
        'module-4-vla/chapter-13-vision-language-action-systems-in-physical-ai',
        'module-4-vla/chapter-14-voice-to-action-using-openai-whisper',
        'module-4-vla/chapter-15-cognitive-planning-with-large-language-models',
        'module-4-vla/chapter-16-capstone-the-autonomous-humanoid',
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
