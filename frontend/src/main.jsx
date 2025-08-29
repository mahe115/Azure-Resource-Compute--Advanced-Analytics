import { StrictMode, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Home from './pages/Home/Home'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navigation from './components/Navigation/Navigation';
import DataPage from './pages/DataPage/DataPage';

const Main = () => {
  useEffect(() => {
    document.body.setAttribute("data-theme", "dark");
  }, []);

  return (
    <>
      <Navigation />   
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/data" element={<DataPage />} />
      </Routes>
    </>
  );
};


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Main/>
    </BrowserRouter>
  </StrictMode>
)
