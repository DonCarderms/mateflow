/* eslint-disable react/react-in-jsx-scope */

import { useState } from "react";
import styled from "styled-components";

import search from "../../assets/images/search-outline.svg";
const InputSearch = styled.div`
  position: relative;
  input {
    // color: rgb(255, 255, 255);
    color: #383838;
    background: center;
    outline: none;
    border: 1px solid #ccc;
    padding: 10px 20px;
    padding-right: 40px;
    border-radius: 5px;
    font-size: 1em;
  }
  input:focus {
    border-color: #3f51b5;
    // caret-color: rgb(204, 204, 204);
    caret-color: #000;
  }
  input::placeholder {
    // color: rgb(204, 204, 204);
    // color: #383838;
  }
  img {
    position: absolute;
    top: 7px;
    right: 10px;
    width: 30px;
  }
`;
const Search = () => {
  const [text, setText] = useState();
  return (
    <InputSearch>
      <input placeholder="buscar por materiais" value={text} />
      <img src={search} alt="" />
    </InputSearch>
  );
};
export default Search;
