import React, { useState } from "react";
import { sendQuery } from "../api";
import Message from "./Message";
import Sidebar from "./Sidebar";
import "../styles.css";

const ChatUI = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [chats, setChats] = useState([]);
  const [theme, setTheme] = useState("dark"); // 🌙

  const session_id = "user1";

  const toggleTheme = () => {
    setTheme(prev => prev === "dark" ? "light" : "dark");
  };

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { type: "user", text: input };

    setMessages(prev => [...prev, userMsg]);
    setChats(prev => [...prev, input]);

    try {
      const res = await sendQuery(input, session_id);

      const botMsg = {
        type: "bot",
        text: "Report generated",
        data: res.data?.result
      };

      setMessages(prev => [...prev, botMsg]);

    } catch {
      setMessages(prev => [...prev, {
        type: "bot",
        text: "⚠️ Error"
      }]);
    }

    setInput("");
  };

  return (
    <div className={`app ${theme}`}>

      <Sidebar chats={chats} />

      <div className="main">

        {/* 🔥 HEADER */}
        <div className="header">
          <span>📊 Chat-Based Report Generator</span>

          <button className="theme-btn" onClick={toggleTheme}>
            {theme === "dark" ? "☀️ Light" : "🌙 Dark"}
          </button>
        </div>

        <div className="messages">
          {messages.map((m, i) => (
            <Message key={i} msg={m} />
          ))}
        </div>

        <div className="input-bar">
          <input
            value={input}
            onChange={e => setInput(e.target.value)}
            placeholder="Ask your report..."
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
          />
          <button onClick={handleSend}>Send</button>
        </div>

      </div>
    </div>
  );
};

export default ChatUI;