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

export default function Upload(){
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();
  const [selectedFile, setSelectedFile] = useState(null);
  const fileTypes = ['application/pdf'];

  const handleFileSelection = (event) => {
    let file;
    if (event.target.files.length > 1) {
      enqueueSnackbar('Please only choose one file.', {variant: 'error'});
      return;
    }
    else {
      file = event.target.files[0];
      console.log(file);
    }

    if (fileTypes.includes(file.type)) {
      uploadFile(file);
    }
    else {
      enqueueSnackbar('Unsupported file type.', {variant: 'error'});
    }
  }

  const uploadFile = (file) => {
    enqueueSnackbar('File successfully uploaded.', {variant: 'success'});
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
        <input type="file" onChange={handleFileSelection} hidden/>
      </Button>
    < /div>
  )
}
