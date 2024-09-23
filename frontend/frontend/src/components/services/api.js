// src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Change this if your API URL is different

export const getSimulationResults = async (metricId) => {
    try {
        const response = await axios.get(`${API_URL}/api/simulation-results/${metricId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching simulation results', error);
        throw error;
    }
};
