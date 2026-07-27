import axios from "axios";

const API_URL = "";

export const getDashboardData = async () => {
    const response = await axios.get(
        `${API_URL}/dashboard`
    );

    return response.data;
};


export const getTelemetry = async () => {
    const response = await axios.get(
        `${API_URL}/telemetry`
    );

    return response.data;
};


export const getLatestReadings = async () => {
    const response = await axios.get(
        `${API_URL}/latest`
    );

    return response.data;
};


export const getDevices = async () => {
    const response = await axios.get(
        `${API_URL}/devices`
    );

    return response.data;
};


export const getAlerts = async () => {
    const response = await axios.get(
        `${API_URL}/alerts`
    );

    return response.data;
};