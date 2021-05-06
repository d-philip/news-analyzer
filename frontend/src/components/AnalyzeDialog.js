import React, { useEffect, useState } from 'react';
import { AuthContext } from "../pages/App";
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { useSnackbar } from 'notistack';

const useStyles = makeStyles((theme) => ({
  analyzeButton: {
    color: "black",
    textTransform: 'none',
  },
  cancelButton: {
    color: "#4E4B61",
    textTransform: 'none',
  },
}));

export default function AnalyzeDialog(props) {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();
  const { state } = React.useContext(AuthContext);
  const [file, setFile] = useState(props.file_info);

  const handleAnalysis = (file) => {
    const req_url = "http://54.91.38.146:6060/";
    let req_data = new FormData();
    req_data.append("email", state.user.email);
    req_data.append("file_id", props.file_id);

    axios.post(req_url+"analyzeSentiment", req_data, {headers: {'Content-Type': 'multipart/form-data'}})
      .then((res) => {
        enqueueSnackbar(res.data.response, {variant: 'success'});
        props.refreshFiles(true);
      })
      .catch((err) => {
        console.log(err);
        enqueueSnackbar("Error analyzing file sentiment. Please try again later", {variant: 'error'});
      })

      axios.post(req_url+"generateKeywords", req_data, {headers: {'Content-Type': 'multipart/form-data'}})
        .then((res) => {
          enqueueSnackbar(res.data.response, {variant: 'success'});
          props.refreshFiles(true);
        })
        .catch((err) => {
          console.log(err);
          enqueueSnackbar("Error generatin file keywords. Please try again later", {variant: 'error'});
        })
    props.handleClose();
  };

   return(
     <div>
       <Dialog
         open={props.open}
         onClose={props.handleClose}
         aria-labelledby="analyze-dialog-title"
         aria-describedby="analyze-dialog-description"
         scroll='paper'
       >
        <DialogTitle id="analyze-dialog-title">{"Analyze File"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="analyze-dialog-description">
            Would you like to perform text analysis on this file?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} autoFocus className={classes.cancelButton}>
            Cancel
          </Button>
          <Button onClick={() => handleAnalysis(file)} className={classes.analyzeButton}>
            Analyze
          </Button>
        </DialogActions>
       </Dialog>
     </div>
   );
 }
