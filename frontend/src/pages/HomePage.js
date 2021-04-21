import React from 'react';
import { AuthContext } from "../pages/App";
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

export default function HomePage(){
  const { state, dispatch } = React.useContext(AuthContext);

  return (
    <Grid
      container
      direction="column"
      justify="center"
      alignItems="center"
    >
      {state.isAuthenticated ? <p>Hello, {state.user.givenName}!</p> : <Typography variant="h6">Please login.</Typography>}
    </Grid>
  )
}
