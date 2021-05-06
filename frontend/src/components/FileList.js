import React, { useEffect, useState } from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListSubheader from '@material-ui/core/ListSubheader';
import axios from 'axios';
import { useSnackbar } from 'notistack';
import File from './File';
import Upload from './Upload';

const useStyles = makeStyles((theme) => ({
  list: {
    width: '100%',
    marginTop: 20,
  },
  fileGrid: {
    flex: 1,
    flexDirection: 'column',
    width: '95%',
  },
}));

export default function FileList() {
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const { state, dispatch } = React.useContext(AuthContext);
  const [files, setFiles] = useState([]);
  const classes = useStyles();

  const loadFiles = (refresh) => {
    const req_url = "http://54.91.38.146:7070/users/" + state.user.email + "/files/";
    axios.get(req_url)
      .then((res) => {
        console.log(res);
        const num_files = Object.keys(res.data).length;
        if (num_files > 0) {
          if (refresh) { enqueueSnackbar('Refreshed files.', {variant: 'info'}); }
          else { enqueueSnackbar(`Loaded ${num_files} files.`, {variant: 'info'}); }
          setFiles(res.data);
        }
        else {
          enqueueSnackbar(`No files stored. Upload some!`, {variant: 'info'});
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    loadFiles(false);
  }, []);

  return(
    <div>
      <Grid className={classes.fileGrid}>
        <Paper elevation={1}>
          <List
            className={classes.list}
            component="nav"
            subheader={
            <ListSubheader component="div">
              File List
            </ListSubheader>
          }>
            {Object.keys(files).map(key => (
              <File file_info={files[key]} file_id={key} refreshFiles={loadFiles}/>
            ))}
          </List>
        </Paper>
      </Grid>
      <Upload refreshFiles={loadFiles}/>
    </div>
  );
}
