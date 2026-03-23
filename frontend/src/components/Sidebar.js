import React from "react";
import { uploadCSV } from "../api";

const Sidebar = ({ chats }) => {

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const res = await uploadCSV(file);
    alert("Uploaded: " + res.data.dataset);
  };

  return (
    <div className="sidebar">
      <h2>Upload CSV</h2>
      <input type="file" accept=".csv" onChange={handleUpload} />

      <h3>History</h3>
      {chats.map((c, i) => <div key={i}>{c}</div>)}
    </div>
  );
};

export default Sidebar;