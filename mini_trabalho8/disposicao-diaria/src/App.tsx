import { Form } from "@/components/form";
import { ToastContainer } from "react-toastify";

export default function App() {
  return (
    <div className="bg-[#EFEFEF] w-screen h-screen flex items-center justify-center">
      <Form />
      <ToastContainer />
    </div>
  );
}
