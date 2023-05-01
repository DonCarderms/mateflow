/* eslint-disable quotes */
import styled from "styled-components";

export const Container = styled.div`
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
`;

export const LoginContainer = styled.div`
  font-family: Arial, sans-serif;
  background-color: #fff;
  padding: 2rem;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;

  h1 {
    text-align: center;
    margin-bottom: 1.5rem;
  }

  a {
    color: #3f51b5;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  button {
    width: 315px;
    padding: 0.5rem;
    background-color: #3f51b5;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }

  input {
    display: block;
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 3px;
    outline: 0;
  }

  input:focus {
    border-color: #3f51b5;
    box-shadow: 0 0 5px rgba(63, 81, 181, 0.5);
  }
  input,
  button {
    transition: all 0.3s ease;
  }
  button:hover {
    background-color: #283593;
  }
`;

export const Links = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
`;
