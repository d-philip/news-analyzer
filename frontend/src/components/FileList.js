import React, { useEffect, useState } from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import axios from 'axios';
import { useSnackbar } from 'notistack';

const useStyles = makeStyles((theme) => ({
  fileGrid: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    // backgroundColor: '#E8E7FF',
    width: '95%',
  },
}));

export default function FileList() {
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const { state, dispatch } = React.useContext(AuthContext);
  const [files, setFiles] = useState([]);
  const classes = useStyles();

  const loadFiles = () => {
    const req_url = "http://54.91.38.146:7070/users/" + state.user.email + "/files/";
    axios.get(req_url)
      .then((res) => {
        console.log(res);
        const num_files = Object.keys(res.data).length;
        if (num_files > 0) {
          enqueueSnackbar(`Loaded ${num_files} files.`, {variant: 'info'});
        }
        else {
          enqueueSnackbar(`No files stored.`, {variant: 'info'});
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    loadFiles();
  });

  return(
    <Grid className={classes.fileGrid}>
      <Paper elevation={1} >
        <p>File List</p>
        <p>OOGA</p>
      </Paper>
    </Grid>
  );
}
