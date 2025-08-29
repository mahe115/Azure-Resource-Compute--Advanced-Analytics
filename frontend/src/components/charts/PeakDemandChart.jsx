import React from 'react';
import { Bar } from 'react-chartjs-2';

const PeakDemandChart = ({ data ,resource }) => {
  if (!data?.length) return <div>No data available</div>;

  const isStorage = resource === "Storage";


  const chartData = {
    labels: data.map(d => d.month),
    datasets: [
      {
        label:isStorage ? 'Peak Storage Usage' : 'Peak CPU Usage',
        data:isStorage?data.map(d => d.usage_storage) :data.map(d => d.usage_cpu),
        backgroundColor: '#FF6384'
      }
    ]
  };

  return <Bar data={chartData} />;
};

export default PeakDemandChart;
