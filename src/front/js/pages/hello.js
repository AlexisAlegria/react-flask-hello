import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Hello = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    if (store.token && store.token != "" && store.token != undefined)
      actions.getMessage();
  }, [store.token]);

  return (
    <div className="text-center mt-5">
      <div className="alert alert-info">{store.message}</div>
      <h1>Hey! This is a private page</h1>
      <br />
      <h2>If you can see this content, You are successfully logged in</h2>
    </div>
  );
};
