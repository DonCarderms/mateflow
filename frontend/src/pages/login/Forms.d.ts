export interface InputProps{
    id: string;
    changed: ChangeEventHandler<HTMLInputElement>;
    value: string;
    label: string;
  }
  
export interface Action{
    field: string;
    type: string;
    value: string;
  }
export interface FormState {
    [key: string]: {
      label: string,
      value: string;
    };
  }