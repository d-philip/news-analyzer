import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import { GoogleLogout } from 'react-google-login';

const clientId = '184252370004-1ue8k5g34tf7t55q85vq66rkdj8369uj.apps.googleusercontent.com'

const useStyles = makeStyles((theme) => ({
  button: {
    color: 'white',
  },
}));

export default function Logout() {
  const { state, dispatch } = React.useContext(AuthContext);
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const classes = useStyles();

  const handleLogout = (res) => {
    console.log('Logout success', res);
    dispatch({ type: "logout" });
    enqueueSnackbar('Logged out successfully.', {variant: 'success'});
  }

  return(
    <GoogleLogout
      clientId={clientId}
      render={renderProps => (
        <Button variant="text" className={classes.button} onClick={renderProps.onClick}>Logout</Button>
      )}
      onLogoutSuccess={handleLogout}
      cookiePolicy={'single_host_origin'}
    >
    </GoogleLogout>
  );
}
