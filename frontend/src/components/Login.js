import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import GoogleLogin from 'react-google-login';

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

  const onLoginSuccess = (res) => {
    console.log('Login success', res.profileObj);
    dispatch({ type: "login", payload: res.profileObj });
    enqueueSnackbar('Logged in successfully.', {variant: 'success'});
  }
  const onLoginFailure = (res) => {
    enqueueSnackbar('Login failed. Please try again later.', {variant: 'error'});
    console.log('Login failed: ', res);
  }

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
