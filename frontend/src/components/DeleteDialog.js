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
  deleteButton: {
    color: "#FF4747",
    textTransform: 'none',
  },
  cancelButton: {
    color: "#4E4B61",
    textTransform: 'none',
  },
}));

export default function DeleteDialog(props) {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();
  const { state } = React.useContext(AuthContext);
  const [file, setFile] = useState(props.file_info);

  const handleDelete = (file) => {
    const req_url = "http://54.91.38.146:7070/users/" + state.user.email + "/files/" + props.file_id;
    axios.delete(req_url)
      .then((res) => {
        console.log(res);
        enqueueSnackbar("Successfully deleted file.", {variant: 'success'});
        props.refreshFiles(true);
      })
      .catch((err) => {
        console.log(err);
        enqueueSnackbar("Error deleting file. Please try again later", {variant: 'error'});
      })
    props.handleClose();
  };

   return(
     <div>
       <Dialog
         open={props.open}
         onClose={props.handleClose}
         aria-labelledby="delete-dialog-title"
         aria-describedby="delete-dialog-description"
         scroll='paper'
       >
        <DialogTitle id="delete-dialog-title">{"Delete File"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="delete-dialog-description">
            Are you sure you want to delete this file?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} autoFocus className={classes.cancelButton}>
            Cancel
          </Button>
          <Button onClick={() => handleDelete(file)} className={classes.deleteButton}>
            Delete
          </Button>
        </DialogActions>
       </Dialog>
     </div>
   );
 }
