import React, { useState, useEffect } from "react";
import "./DataPage.css";
import { fetchData, endpoints } from "../../services/api";

const DataPage = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadData = async () => {
    try {
      setLoading(true);
      const api = endpoints.RawData;
      const results = await fetchData(api);  
      setData(results);
    } catch (error) {
      console.error("Failed to load raw data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  if (loading) return <div className="DataPage">Loading...</div>;
  if (!data || data.length === 0) return <div className="DataPage">No data available</div>;

  const headers = Object.keys(data[0]);

  return (
    <div className="DataPage">
      <h2>Raw Data</h2>
      <table className="data-table">
        <thead>
          <tr>
            {headers.map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {headers.map((key) => (
                <td key={key}>{row[key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataPage;
