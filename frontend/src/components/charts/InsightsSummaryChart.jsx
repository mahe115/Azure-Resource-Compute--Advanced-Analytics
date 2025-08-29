import React from "react";
import "./InsightsSummaryChart.css";

const InsightsSummaryChart = ({ data, resource }) => {
  if (!data) {
    return <div className="summary-loading">Loading summary...</div>;
  }

  const { avg_cpu_usage, avg_storage_usage, peak_usage, total_records, top_region } = data;

  return (
    <div className="insights-summary-grid">
      <div className="summary-card">
        {resource == "CPU" && (
          <span className="summary-value">{avg_cpu_usage}%</span>
        )}
        {resource == "Storage" && (
          <span className="summary-value">{avg_storage_usage} GB</span>
        )}
        <span className="summary-label">Avg CPU Usage</span>
      </div>
      <div className="summary-card">
        <span className="summary-value">{peak_usage}%</span>
        <span className="summary-label">Peak CPU Usage</span>
      </div>
      <div className="summary-card">
        <span className="summary-value">{total_records}</span>
        <span className="summary-label">Total Records</span>
      </div>
      <div className="summary-card">
        <span className="summary-value">{top_region}</span>
        <span className="summary-label">Top Region</span>
      </div>
    </div>
  );
};

export default InsightsSummaryChart;
