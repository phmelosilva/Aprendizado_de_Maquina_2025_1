import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import predictDisposition from "@/services/api";
import { useState } from "react";
import { PredictResultDialog } from "./predict-dialog";

export function Form() {
  const [studyHours, setStudyHours] = useState(0);
  const [extracurricularHours, setExtracurricularHours] = useState(0);
  const [sleepHours, setSleepHours] = useState(0);
  const [socialHours, setSocialHours] = useState(0);
  const [physicalActivityHours, setPhysicalActivityHours] = useState(0);

  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const [response, setResponse] = useState(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const data = {
      Study_Hours_Per_Day: studyHours,
      Extracurricular_Hours_Per_Day: extracurricularHours,
      Sleep_Hours_Per_Day: sleepHours,
      Social_Hours_Per_Day: socialHours,
      Physical_Activity_Hours_Per_Day: physicalActivityHours,
    };

    predictDisposition(data).then((response) => {
      setResponse(response);
      setIsDialogOpen(true);
    });
  };

  const onCloseDialog = () => {
    setIsDialogOpen(false);
    setResponse(null);
    setStudyHours(0);
    setExtracurricularHours(0);
    setSleepHours(0);
    setSocialHours(0);
    setPhysicalActivityHours(0);
  };

  return (
    <>
      <Card className="w-full max-w-sm">
        <form onSubmit={handleSubmit} className="space-y-4">
          <CardHeader>
            <CardTitle>Prever Disposição Diária</CardTitle>
            <CardDescription>
              Informe seus hábitos diários para prever sua disposição.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex flex-col gap-6">
              <div className="grid gap-2">
                <Label htmlFor="study">Horas de estudo por dia</Label>
                <Input
                  id="study"
                  name="Study_Hours_Per_Day"
                  type="number"
                  min={0}
                  step={0.1}
                  placeholder="Ex: 3.5"
                  required
                  onChange={(e) => setStudyHours(Number(e.target.value))}
                  value={studyHours.toString()}
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="extracurricular">
                  Horas de atividades extracurriculares por dia
                </Label>
                <Input
                  id="extracurricular"
                  name="Extracurricular_Hours_Per_Day"
                  type="number"
                  min={0}
                  step={0.1}
                  placeholder="Ex: 1.0"
                  required
                  onChange={(e) =>
                    setExtracurricularHours(Number(e.target.value))
                  }
                  value={extracurricularHours.toString()}
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="sleep">Horas de sono por dia</Label>
                <Input
                  id="sleep"
                  name="Sleep_Hours_Per_Day"
                  type="number"
                  min={0}
                  step={0.1}
                  placeholder="Ex: 7.5"
                  required
                  onChange={(e) => setSleepHours(Number(e.target.value))}
                  value={sleepHours.toString()}
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="social">
                  Horas de interação social por dia
                </Label>
                <Input
                  id="social"
                  name="Social_Hours_Per_Day"
                  type="number"
                  min={0}
                  step={0.1}
                  placeholder="Ex: 2.0"
                  required
                  onChange={(e) => setSocialHours(Number(e.target.value))}
                  value={socialHours.toString()}
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="physical">
                  Horas de atividade física por dia
                </Label>
                <Input
                  id="physical"
                  name="Physical_Activity_Hours_Per_Day"
                  type="number"
                  min={0}
                  step={0.1}
                  placeholder="Ex: 1.5"
                  required
                  onChange={(e) =>
                    setPhysicalActivityHours(Number(e.target.value))
                  }
                  value={physicalActivityHours.toString()}
                />
              </div>
            </div>
          </CardContent>
          <CardFooter>
            <Button
              type="submit"
              className="w-full cursor-pointer disabled:cursor-not-allowed"
            >
              Prever Disposição
            </Button>
          </CardFooter>
        </form>
      </Card>

      {response && isDialogOpen && (
        <PredictResultDialog
          response={response}
          isOpen={isDialogOpen}
          onOpenChange={setIsDialogOpen}
          onClose={onCloseDialog}
        />
      )}
    </>
  );
}
