import React from 'react';
import { Bar } from 'react-chartjs-2';

const RegionalComparisonChart = ({ data }) => {
  if (!data?.length) return <div>No data available</div>;

  const chartData = {
    labels: data.map(d => d.region),
    datasets: [
      {
        label: 'CPU Mean',
        data: data.map(d => d.usage_cpu_mean),
        backgroundColor: '#00C49F'
      },
      {
        label: 'Storage Mean',
        data: data.map(d => d.usage_storage_mean),
        backgroundColor: '#0088FE'
      },
      {
        label: 'Users Mean',
        data: data.map(d => d.users_active_mean),
        backgroundColor: '#FFBB28'
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' }
    }
  };

  return <Bar data={chartData} options={options} />;
};

export default RegionalComparisonChart;
