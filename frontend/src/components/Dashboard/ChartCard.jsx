import { React, useState } from "react";
import "./ChartCard.css";

const ChartCard = ({ title, children, className = "" }) => {
  const [clicked, setClicked] = useState(false);

  return (
    <>
    {clicked && <div className="overlay" onClick={() => setClicked(false)} />}
    
    <div
      className={`chart-card ${className}`}
      style={{
        position: clicked ? "fixed" : "relative",
          top: clicked ? "50%" : "auto",
          left: clicked ? "50%" : "auto",
          transform: clicked
            ? "translate(-50%, -50%) scale(1.5)"
            : "scale(1)",
          zIndex: clicked ? 1000 : 1,
          transition: "transform 0.3s ease, top 0.3s ease, left 0.3s ease",
      }}
    >
      <div className="chart-header">
        <h3 className="chart-title">{title}</h3>
        <button
          className="expand-button"
          onClick={() => setClicked(!clicked)}
        >
          {clicked? "Close" : "expand"}
        </button>
      </div>
      <div className="chart-content">{children}</div>
    </div>
    </>
  );
};

export default ChartCard;
