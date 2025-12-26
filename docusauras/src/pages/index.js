import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './home.module.css';

const FeatureList = [
  {
    title: 'Embodied AI',
    description: 'Go beyond digital brains. Learn how AI perceives and interacts with the physical world through ROS 2 and complex actuators.',
    icon: (
      <svg className={styles.featureIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="3" y="11" width="18" height="10" rx="2" />
        <circle cx="12" cy="5" r="2" />
        <path d="M12 7v4M8 11V9a4 4 0 018 0v2" />
      </svg>
    ),
  },
  {
    title: 'Digital Twins',
    description: 'Build high-fidelity simulations in Gazebo and Unity to train and validate robot behavior before physical deployment.',
    icon: (
      <svg className={styles.featureIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" />
        <path d="M3.27 6.96L12 12.01l8.73-5.05M12 22.08V12" />
      </svg>
    ),
  },
  {
    title: 'Accelerated Vision',
    description: 'Utilize NVIDIA Isaac for hardware-accelerated VSLAM, synthetic data generation, and real-time perception.',
    icon: (
      <svg className={styles.featureIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
        <circle cx="12" cy="12" r="3" />
      </svg>
    ),
  },
  {
    title: 'VLA Systems',
    description: 'Integrate Vision-Language-Action systems and LLMs to enable natural language control and cognitive planning.',
    icon: (
      <svg className={styles.featureIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" />
      </svg>
    ),
  },
];

export default function Home() {
  return (
    <Layout>
      <div className={styles.hero}>
        <div className={styles.heroContent}>
          <h1 className={styles.title}>Physical AI & Humanoid Robotics</h1>
          <p className={styles.subtitle}>
            Master the convergence of digital intelligence and physical embodiment. 
            A comprehensive guide to designing, simulating, and deploying humanoid robots.
          </p>

          <Link className={styles.button} to="/docs/module-1-robotic-nervous-system/chapter-1-introduction-to-the-robotic-nervous-system">
            Explore the Curriculum
          </Link>
        </div>
      </div>

      <main className={styles.section}>
        <div className="container">
          <h2 className={styles.sectionTitle}>Key Focus Areas</h2>
          <div className={styles.cards}>
            {FeatureList.map((props, idx) => (
              <div key={idx} className={styles.card}>
                <div className={styles.iconWrapper}>{props.icon}</div>
                <h3>{props.title}</h3>
                <p>{props.description}</p>
              </div>
            ))}
          </div>
        </div>
      </main>
    </Layout>
  );
}
