import { FaBars } from "react-icons/fa";
import { NavLink as Link } from "react-router-dom";
import styled from "styled-components";

export const Nav = styled.nav`
  background: #f5f5f5;
  height: 85px;
  display: flex;
  justify-content: space-between;
  padding: 0 1rem;
  z-index: 12;
`;

export const NavLink = styled(Link)`
  color: #808080;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0 1rem;
  height: 100%;
  cursor: pointer;
  font-size: 16px;
  border-radius: 4px;
  &.active {
    color: #4d4dff;
  }
`;

export const Bars = styled(FaBars)`
  color: #4d4dff;
  font-size: 2rem;
  cursor: pointer;
`;

export const NavMenu = styled.div`
  display: flex;
  align-items: center;
  margin-right: -24px;
  padding: 10px 0;
  @media screen and (max-width: 768px) {
    display: none;
  }
`;