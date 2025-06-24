import axios from "axios";

const studentDispositionApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export type StudentDispositionData = {
  Study_Hours_Per_Day: number;
  Extracurricular_Hours_Per_Day: number;
  Sleep_Hours_Per_Day: number;
  Social_Hours_Per_Day: number;
  Physical_Activity_Hours_Per_Day: number;
};

export default async function predictDisposition(
  data: StudentDispositionData
): Promise<any> {
  try {
    const response = await studentDispositionApi.post("/predict", data);
    return response.data;
  } catch (error: unknown) {
    console.error("Error fetching student disposition:", error);
    throw error;
  }
}
