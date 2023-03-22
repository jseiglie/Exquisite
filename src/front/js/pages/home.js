import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import Login from "../component/login";
import { useNavigate } from "react-router-dom";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const navigate = useNavigate();

  useEffect(() => {
    localStorage.getItem("token") ? navigate("/dashboard") : "";
  }, []);

  return (
    <div className="text-center">
      <Login />
    </div>
  );
};
