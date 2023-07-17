/* eslint-disable react/react-in-jsx-scope */
import { AnimationSlideIn } from "../../styles/animation/AnimtionSlideIn";
import Search from "../search";
import * as S from "../../styles/header";
import usercircle from "../../assets/images/user-circle-svgrepo-com.svg";
import ModalUser from "../resources/modais/ModalUser";
import React, { MouseEventHandler, useContext, useState } from "react";
import { ThemeContext, ThemeContextType } from "../../context/ThemesContext";

type ThemeButtonChangeType = {
  onClick: MouseEventHandler;
  children: React.ReactNode;
};
const ThemeButtonChange = ({ onClick, children }: ThemeButtonChangeType) => {
  return (
    <>
      <button onClick={onClick}>{children}</button>
    </>
  );
};

const Header = () => {
  const [modalUser, setModalUser] = useState(true);
  const showModalUser = () => setModalUser(!modalUser);
  const { theme, setChangeTheme } = useContext<ThemeContextType>(ThemeContext);

  const handleChangeTheme = () => setChangeTheme && setChangeTheme();
  return (
    <>
      <AnimationSlideIn>
        <S.HeaderConatiner>
          <Search />
          <S.UserTheme>
            <S.UserCircleIcon onClick={showModalUser}>
              <img src={usercircle} alt="" />
              {modalUser || <ModalUser />}
            </S.UserCircleIcon>
            <ThemeButtonChange onClick={handleChangeTheme}>
              {theme}
            </ThemeButtonChange>
          </S.UserTheme>
        </S.HeaderConatiner>
      </AnimationSlideIn>
    </>
  );
};
export default Header;
