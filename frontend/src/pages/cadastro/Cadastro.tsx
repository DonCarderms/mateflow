/* eslint-disable no-unexpected-multiline */
/* eslint-disable react/react-in-jsx-scope */
import { ChangeEvent, useReducer } from "react";

import { InputProps, FormState, Action } from "../login/Forms";
import { Container, LoginContainer, Links } from "../../styles/login";
import { Link } from "react-router-dom";
import { AnimationSlideIn } from "../../styles/animation/AnimtionSlideIn";

const initialForm = {
  username: {
    label: "Username",
    value: "",
  },
  email: {
    label: "Email",
    value: "",
  },
  password: {
    label: "Password",
    value: "",
  },
};

const Input = (props: InputProps) => (
  <input
    placeholder={props.label}
    id={props.id}
    onChange={props.changed}
    value={props.value}
  />
);

const formReducer = (state: FormState, action: Action) => {
  switch (action.type) {
    case "UPDATE_FIELD":
      return {
        ...state,
        [action.field]: {
          ...state[action.field],
          value: action.value,
        },
      };
    default:
      return state;
  }
};

const Login = () => {
  const [formState, dispatch] = useReducer(formReducer, initialForm);
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { id, value } = e.target;
    dispatch({ type: "UPDATE_FIELD", field: id, value });
  };
  return (
    <AnimationSlideIn>
      <Container>
        <LoginContainer>
          <form action="">
            {Object.keys(formState).map((field) => (
              <Input
                key={field}
                id={field}
                label={formState[field].label}
                value={formState[field].value}
                changed={handleInputChange}
              />
            ))}
            <button type="submit">cadastrar-se</button>
          </form>
          <Links>
            <a href="#">Esqueceu a senha?</a>
            <Link to={"/login"}>faz login</Link>
          </Links>
        </LoginContainer>
      </Container>
    </AnimationSlideIn>
  );
};

export default Login;
