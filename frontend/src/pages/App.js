import React from 'react';
import '../assets/styles/App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import HomePage from './HomePage';
import Header from '../components/Header';
import { SnackbarProvider } from 'notistack';

export const AuthContext = React.createContext();

const initialState = {
  isAuthenticated: false,
  user: null,
};

// in-app state management
const reducer = (state, action) => {
  switch (action.type) {
    case "login":
      localStorage.setItem("user", JSON.stringify(action.payload));
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload,
      };
    case "logout":
      localStorage.clear();
      return {
        ...state,
        isAuthenticated: false,
        user: null,
      };
    default:
      return state;
  }
};

export default function App() {
  const [state, dispatch] = React.useReducer(reducer, initialState);

  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      <SnackbarProvider maxSnack={2}>
        <Header />
        <Router>
          <Switch>
            <Route path="/">
              <HomePage />
            </Route>
          </Switch>
        </Router>
      </SnackbarProvider>
    </AuthContext.Provider>
  );
}
