import React from "react";
import ReportTable from "./ReportTable";
import ChartView from "./ChartView";
import { exportCSV } from "../api";

const Message = ({ msg }) => {

  const handleExport = async () => {
    try {
      const res = await exportCSV(msg.data);
      alert("✅ CSV downloaded: " + res.data.file);
    } catch (err) {
      console.error(err);
      alert("❌ Export failed");
    }
  };

  return (
    <div className={`message-row ${msg.type}`}>
      <div className="bubble">

        {/* Message Text */}
        <div className="message-text">
          {msg.text}
        </div>

        {/* 🔥 Report Rendering (SAFE + RELIABLE) */}
        {msg.type === "bot" && msg.data?.table && (
          <div className="report-card">

            {/* Header */}
            <div className="report-header">
              <span>📊 Report</span>

              <button 
                className="export-btn"
                onClick={handleExport}
              >
                ⬇ Download CSV
              </button>
            </div>

            {/* Table */}
            <ReportTable data={msg.data.table} />

            {/* Chart */}
            <ChartView data={msg.data.table} />

          </div>
        )}

      </div>
    </div>
  );
};

export default Message;