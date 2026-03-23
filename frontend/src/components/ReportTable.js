import React from "react";

const ReportTable = ({ data }) => {
  if (!data || data.length === 0) return null;

  const keys = Object.keys(data[0]);

  return (
    <div style={{ marginTop: "10px" }}>
      <table>
        <thead>
          <tr>
            {keys.map(k => <th key={k}>{k}</th>)}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {keys.map(k => <td key={k}>{row[k]}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ReportTable;