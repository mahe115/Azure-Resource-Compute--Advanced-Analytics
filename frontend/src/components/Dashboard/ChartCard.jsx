import React from 'react';
import './ChartCard.css';

const ChartCard = ({ title, children, className = '' }) => {
  return (
    <div className={`chart-card ${className}`}>
      <h3 className="chart-title">{title}</h3>
      <div className="chart-content">
        {children}
      </div>
    </div>
  );
};

export default ChartCard;
