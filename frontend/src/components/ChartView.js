import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
  Legend
} from "recharts";

const ChartView = ({ data }) => {
  if (!data || data.length === 0) return null;

  const keys = Object.keys(data[0]);

  // 🔥 Detect fields
  const xKey = keys.find(k => typeof data[0][k] === "string") || keys[0];

  const hasMarks = keys.includes("marks");
  const hasAttendance = keys.includes("attendance");

  return (
    <div style={{ marginTop: "15px" }}>

      {/* ================= MARKS CHART ================= */}
      {hasMarks && (
        <div style={{
          width: "100%",
          height: "300px",
          background: "#2a2b32",
          padding: "15px",
          borderRadius: "12px",
          marginBottom: "15px"
        }}>
          <h4 style={{ color: "#ccc" }}>📊 Marks Distribution</h4>

          <ResponsiveContainer width="100%" height="90%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#444" />
              <XAxis dataKey={xKey} stroke="#aaa" />
              <YAxis stroke="#aaa" />
              <Tooltip />
              <Legend />
              <Bar dataKey="marks" fill="#19c37d" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}

      {/* ================= ATTENDANCE CHART ================= */}
      {hasAttendance && (
        <div style={{
          width: "100%",
          height: "300px",
          background: "#2a2b32",
          padding: "15px",
          borderRadius: "12px"
        }}>
          <h4 style={{ color: "#ccc" }}>📊 Attendance Overview</h4>

          <ResponsiveContainer width="100%" height="90%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#444" />
              <XAxis dataKey={xKey} stroke="#aaa" />
              <YAxis stroke="#aaa" />
              <Tooltip />
              <Legend />
              <Bar dataKey="attendance" fill="#4dabf7" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}

    </div>
  );
};

export default ChartView;