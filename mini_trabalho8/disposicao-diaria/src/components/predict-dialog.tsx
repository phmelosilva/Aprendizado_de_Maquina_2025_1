import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import type { StudentDispositionResponse } from "@/types/student-disposition.type";

type PredictResultDialogProps = {
  response: StudentDispositionResponse;
  isOpen: boolean;
  onOpenChange: (open: boolean) => void;
  onClose?: () => void;
};

export function PredictResultDialog({
  response,
  isOpen,
  onOpenChange,
  onClose,
}: PredictResultDialogProps) {
  return (
    <Dialog open={isOpen} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-[500px]">
        <DialogHeader>
          <DialogTitle>Resultado da Predição</DialogTitle>
          <DialogDescription>
            Veja abaixo o resultado da predição do seu estado atual.
          </DialogDescription>
        </DialogHeader>
        <div className="space-y-4">
          <div className="p-4 rounded-md bg-gray-100 dark:bg-gray-800">
            <div className="text-sm text-muted-foreground">Classe Predita</div>
            <div className="text-lg font-semibold">
              {response.predicted_meaning}
            </div>
          </div>
          <div>
            <div className="mb-2 font-medium">Probabilidades por classe:</div>
            <ul className="space-y-2">
              {response.classes.map((c) => (
                <li
                  key={c.class}
                  className={`flex items-center justify-between p-2 rounded ${
                    c.class === response.predicted_class
                      ? "bg-green-100 dark:bg-green-900 font-bold"
                      : "bg-muted"
                  }`}
                >
                  <span>{c.meaning}</span>
                  <span>{c.probability_percent.toFixed(1)}%</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <DialogFooter>
          <DialogClose asChild>
            <Button
              className="cursor-pointer"
              variant="outline"
              onClick={onClose}
            >
              Fechar
            </Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
