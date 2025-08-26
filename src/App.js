import React, { useState, useRef, useEffect } from 'react';
import './App.css';

export default function App() {
  // State for storing the chat messages
  const [messages, setMessages] = useState([
    { from: 'bot', text: "Hello there! I'm your academic assistant." },
    { from: 'bot', text: 'May I know your name, please?' }
  ]);
  
  // State for controlling input text
  const [input, setInput] = useState('');
  
  // State for controlling the loading indicator
  const [loading, setLoading] = useState(false);

  // Reference to the chat messages container for scrolling
  const messagesEndRef = useRef(null);

  // Function to handle sending a message
  const handleSend = async () => {
    // Ignore empty input
    if (input.trim() === '') return;

    setLoading(true);

    // Add the user's message to the chat immediately
    const newMessages = [...messages, { from: 'user', text: input }];
    setMessages(newMessages);

    const userMessage = input;
    setInput(''); // Clear the input field

    try {
      console.log('Sending user message:', userMessage); // Log the message being sent to the backend

      // Make a POST request to the backend
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: userMessage }),
      });

      const data = await res.json();
      console.log('Response from backend:', data); // Log the response received from backend

      // Check if the response is valid and append it to the chat messages
      if (data && data.response) {
        setMessages((prev) => [...prev, { from: 'bot', text: data.response }]);
      } else {
        console.error("Invalid response from server:", data);
        setMessages((prev) => [...prev, { from: 'bot', text: "Sorry, I couldn't understand that." }]);
      }
    } catch (err) {
      console.error('Error:', err); // Log any error that occurs
      setMessages((prev) => [
        ...prev,
        { from: 'bot', text: "Sorry, I couldn't connect to the server." }
      ]);
    } finally {
      setLoading(false);  // Stop loading when done
    }
  };

  // Function to handle "Enter" key press
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();  // Prevent default behavior
      handleSend();
    }
  };

  // Scroll to the bottom of the chat when messages change
  useEffect(() => {
    // Scroll to the bottom of the messages container
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]); // This will run every time messages change

  return (
    <div className="app-container">
      <div className="chat-screen">
        <div className="chat-header">ChatBot UI</div>
        <div className="chat-messages" style={{ overflowY: 'auto', maxHeight: '400px' }}>
          {/* Render each message in the messages array */}
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`message ${msg.from === 'user' ? 'user' : 'bot'}`}
            >
              {msg.text}
            </div>
          ))}
          {/* This div will always scroll to the bottom */}
          <div ref={messagesEndRef} />
        </div>
        <div className="chat-input">
          {/* Input field for the user */}
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type a message"
            disabled={loading}  // Disable input when loading
          />
          {/* Send button */}
          <button onClick={handleSend} disabled={loading}>
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}
