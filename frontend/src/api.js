import axios from "axios";

const API = "https://edwisely-0mof.onrender.com";

export const sendQuery = (query, session_id) =>
  axios.post(`${API}/query`, { query, session_id });

export const uploadCSV = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(`${API}/upload`, formData);
};

export const exportCSV = (data) =>
  axios.post(`${API}/export`, data);