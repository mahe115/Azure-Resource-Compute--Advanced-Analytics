import { React, useState } from "react";
import "./Navigation.css";
import { useNavigate } from "react-router-dom";

const Navigation = () => {
  const navigate = useNavigate();
  const [current, setCurrent] = useState("Dashboard");

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <svg className="azure-icon" viewBox="0 0 24 24" width="24" height="24">
          <path
            fill="currentColor"
            d="M13.05 4.24L6.56 18.05L2 18L7.09 9.24L13.05 4.24ZM13.75 5.33L22 18H17.35L11.77 12.38L13.75 5.33Z"
          />
        </svg>
        <h1>Azure Analytics</h1>
      </div>
      <div className="navbar-links">
        <a
          onClick={() => {
            navigate("/");
            setCurrent("Dashboard");
          }}
          className={current == "Dashboard" ? "nav-link active" : "nav-link"}
        >
          <span className="nav-icon"></span>
          Dashboard
        </a>
        <a
          onClick={() => {
            navigate("/data");
            setCurrent("Data");
          }}
          className={current == "Data" ? "nav-link active" : "nav-link"}
        >
          <span className="nav-icon"></span>
          Data
        </a>{" "}
      </div>
    </nav>
  );
};

export default Navigation;
