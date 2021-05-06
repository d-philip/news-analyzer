import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { AuthContext } from "../pages/App";
import axios from 'axios';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';

const useStyles = makeStyles((theme) => ({
  uploadButton: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    textTransform: 'none',
    color: '#F8F7FF',
    backgroundColor: '#B8B8FF',
    '&:hover': {
      backgroundColor: '#9785FF',
    },
  },
}));

export default function Upload(props){
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();
  const fileTypes = ['application/pdf'];

  const handleFileSelection = (event) => {
    let file;
    if (event.target.files.length > 1) {
      enqueueSnackbar('Please only choose one file.', {variant: 'error'});
      return;
    }
    else {
      file = event.target.files[0];
    }

    if (fileTypes.includes(file.type)) {
      uploadFile(file);
    }
    else {
      enqueueSnackbar('Unsupported file type.', {variant: 'error'});
      return;
    }
  }

  const uploadFile = (file) => {
    const req_url = "http://54.91.38.146:7070/users/" + state.user.email + "/files/";
    let req_data = new FormData();
    req_data.append("file", file);
    req_data.append("source", (null, 'disk'));

    axios.post(req_url, req_data, {headers: {'Content-Type': 'multipart/form-data'}})
      .then((res) => {
        console.log(res);
        enqueueSnackbar(res.data.response, {variant: 'success'});
        props.refreshFiles(true);
      })
      .catch((err) => {
        console.log(err);
        enqueueSnackbar("Error uploading file. Please try again later.", {variant: 'error'})
      });
  };

  return(
    <div>
      <Button
        size="large"
        startIcon={<CloudUploadIcon />}
        variant="contained"
        className={classes.uploadButton}
        component="label"
      >
        Upload Files
        <input type="file" onChange={(e) => handleFileSelection(e)} hidden/>
      </Button>
    < /div>
  )
}
