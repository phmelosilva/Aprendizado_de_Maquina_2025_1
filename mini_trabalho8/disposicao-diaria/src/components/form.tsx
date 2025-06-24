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

export function Form() {
  return (
    <Card className="w-full max-w-sm">
      <CardHeader>
        <CardTitle>Prever Disposição Diária</CardTitle>
        <CardDescription>
          Informe seus hábitos diários para prever sua disposição.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form>
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
              />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="social">Horas de interação social por dia</Label>
              <Input
                id="social"
                name="Social_Hours_Per_Day"
                type="number"
                min={0}
                step={0.1}
                placeholder="Ex: 2.0"
                required
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
              />
            </div>
          </div>
        </form>
      </CardContent>
      <CardFooter>
        <Button type="submit" className="w-full">
          Prever Disposição
        </Button>
      </CardFooter>
    </Card>
  );
}
