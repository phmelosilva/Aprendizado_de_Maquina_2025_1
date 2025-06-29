export type StudentDispositionData = {
  Study_Hours_Per_Day: number;
  Extracurricular_Hours_Per_Day: number;
  Sleep_Hours_Per_Day: number;
  Social_Hours_Per_Day: number;
  Physical_Activity_Hours_Per_Day: number;
};

export type PredictApiClass = {
  class: number;
  meaning: string;
  probability_percent: number;
};

export type StudentDispositionResponse = {
  predicted_class: number;
  predicted_meaning: string;
  classes: PredictApiClass[];
};
