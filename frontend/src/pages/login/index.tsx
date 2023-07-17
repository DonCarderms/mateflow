/* eslint-disable no-unexpected-multiline */
/* eslint-disable react/react-in-jsx-scope */
import { ChangeEvent, useContext, useEffect, useReducer } from "react";

// import { useQuery } from "react-query";

import { InputProps, FormState, Action } from "./Forms";
import { Container, LoginContainer, Links } from "../../styles/login";
import { Link } from "react-router-dom";
import { AnimationSlideIn } from "../../styles/animation/AnimtionSlideIn";
// import { URL, USERS } from "../../Api/URLS.api";

const initialForm = {
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
            <button type="submit">logar</button>
          </form>
          <Links>
            <Link to="#">Esqueceu a senha?</Link>
            <Link to={"/cadastro"}>Cadastre-se</Link>
          </Links>
        </LoginContainer>
      </Container>
    </AnimationSlideIn>
  );
};

export default Login;
