import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  container: {
    backgroundColor: '#F8F7FF',
  },
}));

export default function HomePage(){
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();

  return (
    <Grid
      container
      direction="column"
      justify="center"
      alignItems="center"
      className={classes.container}
    >
      {state.isAuthenticated ? <p>Hello, {state.user.givenName}!</p> : <Typography variant="h6">Please login.</Typography>}
    </Grid>
  )
}