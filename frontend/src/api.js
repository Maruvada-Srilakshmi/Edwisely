import axios from "axios";

const API = "http://127.0.0.1:8000";

export const sendQuery = (query, session_id) =>
  axios.post(`${API}/query`, { query, session_id });

export const uploadCSV = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${API}/upload`, formData);
};

export const exportCSV = (data) =>
  axios.post(`${API}/export`, data);