import type {
  StudentDispositionData,
  StudentDispositionResponse,
} from "@/types/student-disposition.type";
import axios from "axios";

const studentDispositionApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

export default async function predictDisposition(
  data: StudentDispositionData
): Promise<StudentDispositionResponse> {
  try {
    const response: { data: StudentDispositionResponse } =
      await studentDispositionApi.post("/predict", data);
    return response.data;
  } catch (error: any) {
    console.error("Error fetching student disposition:", error);
    throw error;
  }
}
