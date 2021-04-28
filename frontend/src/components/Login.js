import React, { useEffect, useState } from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import GoogleLogin from 'react-google-login';
import axios from 'axios';

const clientId = '184252370004-1ue8k5g34tf7t55q85vq66rkdj8369uj.apps.googleusercontent.com'

const useStyles = makeStyles((theme) => ({
  button: {
    color: 'white',
  },
}));

export default function Login() {
  const { state, dispatch } = React.useContext(AuthContext);
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const classes = useStyles();
  const [loginStatus, setLoginStatus] = useState(null);

  const handleLogin = () => {
    const req_url = "http://54.91.38.146:8080/users/" + state.user.email;
    axios.get(req_url)
      .then((res) => {
        console.log(res);
        enqueueSnackbar('Logged in successfully.', {variant: 'success'});
        dispatch({type: "auth"});
      })
      .catch((err) => {
        if (err.response.data.error === "User could not be found."){
          console.log("Registering user");
          registerUser();
        }
      })
  };

  const registerUser = () => {
    const req_url = "http://54.91.38.146:8080/users/";
    const user = {
        email: state.user.email,
        first_name: state.user.givenName,
        last_name: state.user.familyName,
        occupation: "",
    }
    axios.post(req_url, user)
      .then((res) => {
        console.log(res);
        enqueueSnackbar('User registered successfully.', {variant: 'success'});
        dispatch({type: "auth"});
      })
      .catch((err) => {
        console.log(err.data);
      })
  };

  const onLoginSuccess = (res) => {
    console.log('Login success', res.profileObj);
    dispatch({ type: "login", payload: res.profileObj });
    setLoginStatus("ready");
  };

  const onLoginFailure = (res) => {
    enqueueSnackbar('Login failed. Please try again later.', {variant: 'error'});
    console.log('Login failed: ', res);
  };

  useEffect(() => {
    if (loginStatus === "ready"){
      handleLogin();
    };
  })

  return(
    <GoogleLogin
      clientId={clientId}
      render={renderProps => (
        <Button variant="text" className={classes.button} onClick={renderProps.onClick}>Login</Button>
      )}
      onSuccess={onLoginSuccess}
      onFailure={onLoginFailure}
      cookiePolicy={'single_host_origin'}
    />
  );
}
