import React, { useEffect, useState } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { ChatProvider, useChat } from './ChatContext';
import Chatbot from '@site/src/components/Chatbot';

function ChatWrapper({ children }) {
  const { isChatOpen, closeChat, toggleChat } = useChat();

  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.toggleDocusaurusChatbot = (e) => {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        toggleChat();
      };
      
      const handleNavbarClick = (e) => {
        if (e.target.id === 'chatbot-nav-link' || e.target.closest('#chatbot-nav-link')) {
          e.preventDefault();
          e.stopPropagation();
          toggleChat();
        }
      };

      document.addEventListener('click', handleNavbarClick, true);
      return () => {
        document.removeEventListener('click', handleNavbarClick, true);
        delete window.toggleDocusaurusChatbot;
      };
    }
  }, [toggleChat]);

  return (
    <>
      {children}
      <Chatbot isOpen={isChatOpen} onClose={closeChat} />
      {!isChatOpen && (
        <button 
          onClick={toggleChat}
          style={{
            position: 'fixed', bottom: '20px', right: '20px',
            width: '60px', height: '60px', borderRadius: '50%',
            backgroundColor: '#2563eb', color: 'white', border: 'none',
            boxShadow: '0 4px 12px rgba(0,0,0,0.2)', cursor: 'pointer',
            zIndex: 9999, fontSize: '24px'
          }}
        >
          💬
        </button>
      )}
    </>
  );
}

export default function Root({ children }) {
  return (
    <BrowserOnly fallback={<div>{children}</div>}>
      {() => (
        <ChatProvider>
          <ChatWrapper>{children}</ChatWrapper>
        </ChatProvider>
      )}
    </BrowserOnly>
  );
}
