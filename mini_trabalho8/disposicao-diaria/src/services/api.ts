import axios from "axios";

const studentDispositionApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

type StudentDispositionData = {
  Study_Hours_Per_Day: number;
  Extracurricular_Hours_Per_Day: number;
  Sleep_Hours_Per_Day: number;
  Social_Hours_Per_Day: number;
  Physical_Activity_Hours_Per_Day: number;
};

export default function getStudentDisposition(data: StudentDispositionData) {
  return studentDispositionApi
    .post("/predict", data)
    .then((response) => response.data)
    .catch((error) => {
      console.error("Error fetching student disposition:", error);
      throw error;
    });
}
