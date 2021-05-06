import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import FileList from "../components/FileList";
import Grid from '@material-ui/core/Grid';
import { useHistory } from 'react-router-dom';

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

export default function FilePage() {
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();
  const history = useHistory();

  if (!state.isAuthenticated) {
    history.push('/');
    return(<Grid />);
  }
  else{
    return (
      <Grid className={classes.root} align="center">
        <FileList />
      </Grid>
    );
  }
}
