import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import { useHistory } from "react-router-dom";
import "../../styles/home.css";

export const Login = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();


  const handleClick = () => {
    actions.login(email, password);
  };


  return (
    <div className="text-center mt-5">
      {store.token && store.token != "" && store.token != undefined ? (
        <div>
          <h1>Welcome!</h1>
          <br/>
          <h1>You are logged in token</h1>
        </div>
      ) : (
        <div>
          <h1>Login</h1>
          <br/>
          <h3>Please enter your credentials</h3>
          <br/>
          <input
            type="text"
            placeholder="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleClick}>Login</button>
        </div>
      )}
    </div>
  );
};
