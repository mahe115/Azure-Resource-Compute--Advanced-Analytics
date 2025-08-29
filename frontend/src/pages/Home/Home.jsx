import React from "react";
import Navigation from "../../components/Navigation/Navigation";
import DashboardLayout from "../../components/Dashboard/DashboardLayout";
import "./Home.css";

const Home = () => {
  return (
    <div className="home">
      <main className="main-content">
        <DashboardLayout />
      </main>
    </div>
  );
};

export default Home;
           