import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar } from 'recharts';
import { formatDate } from '../../utils/dateUtils';

const UsageChart = ({ data, metrics = ['usage_cpu'], title }) => {
  if (!data?.length) return <div>No data available</div>;

  const metricSet = new Set(metrics);
  const keys = Object.keys(data[0]);
  const xKey = keys.find(k => k === 'date') || keys.find(k => !metricSet.has(k));

  const colors = {
    usage_cpu: '#00C49F',
    usage_storage: '#0088FE',
    users_active: '#FFBB28'
  };

  const isTimeSeries = xKey === 'date';

  return (
    <ResponsiveContainer width="100%" height={300}>
      {isTimeSeries ? (
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis 
            dataKey={xKey} 
            stroke="#999"
            tickFormatter={formatDate}
          />
          <YAxis stroke="#999" />
          <Tooltip 
            contentStyle={{ backgroundColor: '#222', border: '1px solid #555', color: '#fff' }}
            labelFormatter={formatDate}
          />
          <Legend />
          {metrics.map(metric => (
            <Line 
              key={metric}
              type="monotone" 
              dataKey={metric}
              name={metric.replace(/_/g, ' ').toUpperCase()}
              stroke={colors[metric] || '#8884d8'}
              dot={false}
            />
          ))}
        </LineChart>
      ) : (
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#444" />
          <XAxis dataKey={xKey} stroke="#999" />
          <YAxis stroke="#999" />
          <Tooltip contentStyle={{ backgroundColor: '#222', border: '1px solid #555', color: '#fff' }} />
          <Legend />
          {metrics.map(metric => (
            <Bar 
              key={metric}
              dataKey={metric}
              name={metric.replace(/_/g, ' ').toUpperCase()}
              fill={colors[metric] || '#8884d8'}
            />
          ))}
        </BarChart>
      )}
    </ResponsiveContainer>
  );
};

export default UsageChart;
