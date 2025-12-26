import React, { useState, useEffect, useRef } from 'react';
import styles from './styles.module.css';

// Allow setting API URL through window object for flexibility in different environments
const API_BASE_URL = process.env.NODE_ENV === 'production' ? '/api' : 'http://localhost:8000';

const Chatbot = ({ isOpen, onClose }) => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (isOpen) {
        scrollToBottom();
    }
  }, [messages, isOpen]);

  if (!isOpen) return null;

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim()) return;

    const userMessage = inputMessage;
    setMessages(prev => [...prev, { sender: 'user', text: userMessage }]);
    setInputMessage('');
    setIsLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_message: userMessage }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setMessages(prev => [...prev, { sender: 'bot', text: data.response }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, {
        sender: 'bot',
        text: "Sorry, I couldn't get a response. Please try again later."
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.chatbotOverlay}>
        <div className={styles.chatbotContainer}>
            <div className={styles.chatbotHeader}>
                <h3 style={{ color: 'white', margin: 0 }}>AI Assistant</h3>
                <button className={styles.closeButton} onClick={onClose} style={{ cursor: 'pointer' }}>&times;</button>
            </div>
            <div className={styles.messagesContainer}>
                {messages.length === 0 && (
                    <div className={styles.welcomeMessage}>
                        Hello! Ask me anything about the book.
                    </div>
                )}
                {messages.map((msg, index) => (
                <div key={index} className={`${styles.message} ${styles[msg.sender]}`}>
                    {msg.text}
                </div>
                ))}
                {isLoading && (
                <div className={`${styles.message} ${styles.bot}`}>
                    ...
                </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            <form onSubmit={handleSendMessage} className={styles.inputContainer}>
                <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Type a message..."
                className={styles.messageInput}
                disabled={isLoading}
                />
                <button type="submit" className={styles.sendButton} disabled={isLoading}>
                Send
                </button>
            </form>
        </div>
    </div>
  );
};

export default Chatbot;
