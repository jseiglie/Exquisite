import React, { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";
import logo from "../../../../public/src/img/exquisuite.webp";

const Login = () => {
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { actions, store } = useContext(Context);
  const navigate = useNavigate();

  const handleUser = (e) => {
    setUser(e.target.value);
  };
  const handlePassword = (e) => {
    setPassword(e.target.value);
  };
  const handleLogin = async (e) => {
    e.preventDefault();
    const result = await actions.login(user, password);
    if (result) {
      navigate("/dashboard");
    } else {
      setError("Email o contraseña incorrectos");
    }
  };

  const handleKeyDown = (e) => {
    if (e.keyCode == 13) {
      handleLogin(e);
    }
  };
  return (
    <>
      <div className="container-fluid gx-0 mt-5">
        <div className="login-banner">
          <span className="login-banner_text">
            EXQUI
            <img className="login-banner_text_logo" src={logo} />
            SUITE
          </span>
        </div>
        <div className="container login-wrapper w-75 ">
          <form onSubmit={(e) => handleLogin(e)}>
            <input
              className=" mb-4 login-input mx-auto"
              type="text"
              placeholder="user"
              name="user"
              onChange={(e) => handleUser(e)}
            ></input>
            <input
              className=" mb-4 login-input mx-auto"
              type="password"
              placeholder="password"
              name="password"
              onChange={(e) => handlePassword(e)}
              onKeyDown={(e) => handleKeyDown(e)}
            ></input>
            <input
              type="submit"
              className="mb-4 login-input mx-auto"
              value="Login"
            />
          </form>
          {error != "" ? (
            <div className="container w-50">
              <div className="card">
                <div className="card-header bg-danger d-flex justify-content-between">
                  <span className="zoom_shrink">Error</span>
                  <span
                    className="close_icon zoom_shrink"
                    onClick={() => setError("")}
                  ></span>
                </div>
                <div className="card-body">
                  <p>Error al intentar iniciar sesión.</p>
                  <p>{error}</p>
                </div>
              </div>
            </div>
          ) : (
            ""
          )}
        </div>
      </div>
    </>
  );
};

export default Login;
