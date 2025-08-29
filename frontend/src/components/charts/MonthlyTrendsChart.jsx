import React from 'react';
import { Line } from 'react-chartjs-2';

const MonthlyTrendsChart = ({ data }) => {
  if (!data?.length) return <div>No data available</div>;

  const chartData = {
    labels: data.map(d => d.month),
    datasets: [
      {
        label: 'CPU Usage',
        data: data.map(d => d.usage_cpu),
        borderColor: '#00C49F',
        fill: false
      },
      {
        label: 'Storage Usage',
        data: data.map(d => d.usage_storage),
        borderColor: '#0088FE',
        fill: false
      },
      {
        label: 'Users Active',
        data: data.map(d => d.users_active),
        borderColor: '#FFBB28',
        fill: false
      }
    ]
  };

  return <Line data={chartData} />;
};

export default MonthlyTrendsChart;
