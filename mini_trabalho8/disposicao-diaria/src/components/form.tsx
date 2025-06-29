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
import { useForm } from "react-hook-form";
import type { StudentDispositionResponse } from "@/types/student-disposition.type";

export function Form() {
  const { register, handleSubmit } = useForm();

  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const [isLoading, setIsLoading] = useState(false);
  const [response, setResponse] = useState<StudentDispositionResponse | null>(
    null
  );

  const onSubmit = async (data: any) => {
    try {
      setIsLoading(true);

      const response: StudentDispositionResponse = await predictDisposition(
        data
      );

      setIsLoading(false);
      setResponse(response);
      setIsDialogOpen(true);
    } catch (error) {
      console.error("Erro ao prever disposição:", error);
      return;
    }
  };

  const onCloseDialog = () => {
    setIsDialogOpen(false);
    setResponse(null);
  };

  return (
    <>
      <Card className="w-full max-w-sm">
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
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
                  {...register("Study_Hours_Per_Day")}
                  type="number"
                  min={0}
                  required
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="extracurricular">
                  Horas de atividades extracurriculares por dia
                </Label>
                <Input
                  id="extracurricular"
                  {...register("Extracurricular_Hours_Per_Day")}
                  type="number"
                  min={0}
                  required
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="sleep">Horas de sono por dia</Label>
                <Input
                  id="sleep"
                  {...register("Sleep_Hours_Per_Day")}
                  type="number"
                  min={0}
                  required
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="social">
                  Horas de interação social por dia
                </Label>
                <Input
                  id="social"
                  {...register("Social_Hours_Per_Day")}
                  type="number"
                  min={0}
                  required
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="physical">
                  Horas de atividade física por dia
                </Label>
                <Input
                  id="physical"
                  {...register("Physical_Activity_Hours_Per_Day")}
                  type="number"
                  min={0}
                  required
                />
              </div>
            </div>
          </CardContent>
          <CardFooter>
            <Button
              type="submit"
              disabled={isLoading}
              className="w-full cursor-pointer"
            >
              {isLoading ? "Carregando..." : "Prever Disposição"}
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
