import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {
  const { store, actions } = useContext(Context);

  return (
    <nav className="navbar navbar-dark bg-dark">
      <div className="container">
        <Link to="/">
          <span className="navbar-brand mb-0 h1">React Boilerplate</span>
        </Link>
        {store.token ? (
          <div>
            <Link to="/">
              <span className="navbar-brand mb-0 h1">Home</span>
            </Link>
            <Link to="/hello">
              <span className="navbar-brand mb-0 h1">Private</span>
            </Link>
          </div>
        ) : (
          <Link to="/">
            <span className="navbar-brand mb-0 h1">Home</span>
          </Link>
        )}

        <div className="ml-auto">
          {!store.token ? (
            <div>
              <Link to="/login">
                <span className="navbar-brand mb-0 h1">Login</span>
              </Link>
              <Link to="/signup">
                <span className="navbar-brand mb-0 h1">Sign up</span>
              </Link>
            </div>
          ) : (
            <Link to="/login">
              <button
                onClick={() => actions.logout()}
                className="btn btn-primary"
              >
                Logout
              </button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};
