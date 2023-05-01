/* eslint-disable react/react-in-jsx-scope */
import { AnimationSlideIn } from "../resources/styles geral/animation/AnimtionSlideIn";
import Search from "../search";
import { HeaderConatiner, UserCircleIcon } from "./style";
import usercircle from "../../assets/images/user-circle-svgrepo-com.svg";
import ModalUser from "../resources/modais/ModalUser";
import { useState } from "react";

const Header = () => {
  const [modalUser, setModalUser] = useState(false);
  const showModalUser = () => setModalUser(!modalUser);

  return (
    <>
      <AnimationSlideIn>
        <HeaderConatiner>
          <Search />
          <UserCircleIcon onClick={showModalUser}>
            <img src={usercircle} alt="" />
            {modalUser ? <ModalUser /> : null}
          </UserCircleIcon>
        </HeaderConatiner>
      </AnimationSlideIn>
    </>
  );
};
export default Header;
