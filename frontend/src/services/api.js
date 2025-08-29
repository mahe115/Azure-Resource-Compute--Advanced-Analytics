const BASE_URL = 'http://localhost:5000/api';

export const fetchData = async (endpoint) => {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`);
    if (!response.ok) throw new Error('Network response was not ok');
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const endpoints = {
  usageTrends: 'usage-trends',
  topRegions: 'top-regions',
  peakDemand: 'peak-demand',
  regionalComparison: 'regional-comparison',
  holidayImpact: 'holiday-impact',
  monthlyTrends: 'monthly-trends',
  insights: 'insights',
  insightsStorage: 'insights-storage',
  usageTrendsStorage : 'usage-trends-storage',
  topRegionsStorage : 'top-regions-storage',
  peakDemandStorage : 'peak-demand-storage',
  RawData : "raw-data",
};
