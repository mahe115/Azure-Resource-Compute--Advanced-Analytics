import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const TopRegionsChart = ({ data, resource }) => {
  if (!data?.length) return <div>No data available</div>;

    const isStorage = resource === "Storage";

  const chartData = {
    labels: data.map(d => d.region),
    datasets: [
      {
        label:isStorage ? 'Storage Usage' : 'CPU Usage',
        data: isStorage ? data.map(d => d.usage_storage) :data.map(d => d.usage_cpu),
        backgroundColor: '#0088FE'
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Top Regions by CPU Usage' }
    },
    scales: {
      y: {
        beginAtZero: false,
        min:isStorage ?325000 : 19000 , 
        ticks: {
          stepSize: 500 
        }
      }
    }
  };

  return <Bar data={chartData} options={options} />;
};

export default TopRegionsChart;
