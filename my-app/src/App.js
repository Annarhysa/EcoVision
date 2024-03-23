import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  // State variables to store data fetched from the backend
  const [deforestationData, setDeforestationData] = useState(null);
  const [climateChangeData, setClimateChangeData] = useState(null);

  // Fetch deforestation data from the backend
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/deforestation-data') // Replace with the correct URL of your Flask server
      .then(response => {
        setDeforestationData(response.data);
      })
      .catch(error => {
        console.error('Error fetching deforestation data:', error);
      });
  }, []);

  // Fetch climate change data from the backend
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/climate-change-data') // Replace with the correct URL of your Flask server
      .then(response => {
        setClimateChangeData(response.data);
      })
      .catch(error => {
        console.error('Error fetching climate change data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Deforestation Data</h1>
      {deforestationData && (
        <div>
          <p>Region: {deforestationData.region}</p>
          <p>Deforestation Rate: {deforestationData.deforestation_rate}</p>
          <p>Year: {deforestationData.year}</p>
        </div>
      )}

      <h1>Climate Change Data</h1>
      {climateChangeData && (
        <div>
          <p>Region: {climateChangeData.region}</p>
          <p>Temperature Anomaly: {climateChangeData.temperature_anomaly}</p>
          <p>Year: {climateChangeData.year}</p>
        </div>
      )}
    </div>
  );
}

export default App;
