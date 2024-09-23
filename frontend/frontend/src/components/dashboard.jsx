// src/components/Dashboard.jsx
import React, { useEffect, useState } from 'react';
import { getSimulationResults } from '../services/api';

const Dashboard = () => {
    const [results, setResults] = useState([]);
    const metricId = 1; 

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await getSimulationResults(metricId);
                setResults(data);
            } catch (error) {
                console.error('Error fetching data', error);
            }
        };

        fetchData();
    }, [metricId]);

    return (
        <div>
            <h1>Simulation Results Dashboard</h1>
            <ul>
                {results.map(result => (
                    <li key={result.id}>
                        LLM ID: {result.llm_id} - Value: {result.value}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;
