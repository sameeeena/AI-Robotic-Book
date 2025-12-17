// import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './home.module.css';
import Chatbot from '@site/src/components/Chatbot'; // Import the Chatbot component

export default function Home() {
  return (
    <Layout>
      <div className={styles.hero}>
        <div className={styles.heroContent}>
          <h1 className={styles.title}>Physical AI & Humanoid Robots</h1>
          <p className={styles.subtitle}>
            A beginner-friendly guide to the future of AI, robotics, sensors, and intelligent machines.
          </p>

          <Link className={styles.button} to="/docs/intro">
            Start Reading →
          </Link>
        </div>
      </div>

      <main className={styles.section}>
        <h2 className={styles.sectionTitle}>What You Will Learn</h2>

        <div className={styles.cards}>
          <div className={styles.card}>
            <h3>🤖 Humanoid Robotics</h3>
            <p>Understand robot anatomy, sensors, actuators, and control systems.</p>
          </div>

          <div className={styles.card}>
            <h3>🧠 Physical AI</h3>
            <p>How intelligence emerges when AI interacts with the physical world.</p>
          </div>

          <div className={styles.card}>
            <h3>🔗 RAG Chatbot Integration</h3>
            <p>Learn how AI answers questions using your book's content.</p>
          </div>
        </div>

        <section className={styles.chatbotSection}>
            <div className="container">
                <h2>Ask our AI Chatbot about the book!</h2>
                <Chatbot />
            </div>
        </section>
      </main>
    </Layout>
  );
}