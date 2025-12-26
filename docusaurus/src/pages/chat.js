import React from 'react';
import Layout from '@theme/Layout';
import Chatbot from '@site/src/components/Chatbot';
import styles from './chat.module.css';

export default function ChatPage() {
  return (
    <Layout title="Chat" description="Chat with our AI assistant">
      <div className={styles.chatPageContainer}>
        <h1 className={styles.chatPageTitle}>Chat with our AI assistant</h1>
        <div className={styles.chatPageComponent}>
          <Chatbot />
        </div>
      </div>
    </Layout>
  );
}