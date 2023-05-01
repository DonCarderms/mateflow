import styled from "styled-components";

export const AnimationSlideIn = styled.div`
  animation: slideIn 0.5s ease-out forwards;
  @keyframes slideIn {
    from {
      transform: translateY(-50px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
`;
