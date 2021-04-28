import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import '../assets/styles/App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import HomePage from './HomePage';
import FilePage from './FilePage';
import Header from '../components/Header';
import { SnackbarProvider } from 'notistack';
import Grid from '@material-ui/core/Grid';

export const AuthContext = React.createContext();

const initialState = {
  isAuthenticated: false,
  user: null,
};

// in-app state management
const reducer = (state, action) => {
  switch (action.type) {
    case "auth":
    return {
      ...state,
      isAuthenticated: true,
    };
    case "login":
      localStorage.setItem("user", JSON.stringify(action.payload));
      return {
        ...state,
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

const useStyles = makeStyles((theme) => ({
  root: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
    width: '100%',
  },
}));

export default function App() {
  const [state, dispatch] = React.useReducer(reducer, initialState);
  const classes = useStyles();

  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      <SnackbarProvider maxSnack={2}>
        <Grid className={classes.root}>
          <Header />
          <Router>
            <Switch>
              <Route path="/files">
                <FilePage />
              </Route>
              <Route path="/">
                <HomePage />
              </Route>
            </Switch>
          </Router>
        </Grid>
      </SnackbarProvider>
    </AuthContext.Provider>
  );
}
