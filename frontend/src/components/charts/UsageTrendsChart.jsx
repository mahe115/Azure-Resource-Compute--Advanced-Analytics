import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend);

const UsageTrendsChart = ({ data, resource }) => {
  if (!data?.length) return <div>No data available</div>;

  const isStorage = resource === "Storage";

  const chartData = {
    labels: data.map(d => d.region),
    datasets: [
      {
        label: isStorage ? "Storage Usage" : "CPU Usage",
        data: isStorage ? data.map(d => d.usage_storage) : data.map(d => d.usage_cpu),
        borderColor: '#00C49F',
        backgroundColor: '#00C49F',
        fill: false,
        tension: 0.3
      }
    ]
  };

  return <Line data={chartData} />;
};

export default UsageTrendsChart;
