import React, { createContext, useState, useContext } from 'react';

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [isChatOpen, setIsChatOpen] = useState(false);

  const toggleChat = () => setIsChatOpen(!isChatOpen);
  const closeChat = () => setIsChatOpen(false);
  const openChat = () => setIsChatOpen(true);

  return (
    <ChatContext.Provider value={{ isChatOpen, toggleChat, closeChat, openChat }}>
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
