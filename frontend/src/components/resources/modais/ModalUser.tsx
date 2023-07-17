/* eslint-disable react/react-in-jsx-scope */

import styled from "styled-components";
import { AnimationSlideIn } from "../../../styles/animation/AnimtionSlideIn";
import { GlobalThemeProps } from "../../../styles/GolbalStyle";

const Container = styled.div`
  background: ${({ theme }: GlobalThemeProps) => theme.background};
  width: 200px;
  height: 300px;
  position: absolute;
  /* border: 1px solid #ccc; */
  -webkit-box-shadow: rgb(0, 0, 0) 0px 10px 13px -7px,
    rgba(0, 0, 0, 0) 5px 5px 15px 5px;
  box-shadow: rgb(0, 0, 0) 0px 10px 13px -7px, rgba(0, 0, 0, 0) 5px 5px 15px 5px;
  top: 2px;
  right: -83px;
  border-radius: 3px;

  p {
    text-align: center;
  }
`;

const ModalUser = () => {
  return (
    <AnimationSlideIn>
      <Container>
        <p>minha conta</p>
      </Container>
    </AnimationSlideIn>
  );
};

export default ModalUser;
