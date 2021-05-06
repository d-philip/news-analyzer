import React, { useEffect, useState } from 'react';
import { AuthContext } from "../pages/App";
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { useSnackbar } from 'notistack';

const useStyles = makeStyles((theme) => ({
  renameButton: {
    color: "black",
    textTransform: 'none',
  },
  cancelButton: {
    color: "#4E4B61",
    textTransform: 'none',
  },
}));

export default function RenameDialog(props) {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();
  const { state } = React.useContext(AuthContext);
  const [file, setFile] = useState(props.file_info);
  const [filename, setFilename] = useState('');

  const handleChange = (event) => {
    console.log(event.target.value);
    setFilename(event.target.value)
  };

  const handleRename = (file) => {
    const req_url = "http://54.91.38.146:7070/users/" + state.user.email + "/files/" + props.file_id;
    axios.patch(req_url, {file_name: filename})
      .then((res) => {
        console.log(res);
        enqueueSnackbar("Successfully renamed file.", {variant: 'success'});
        props.refreshFiles(true);
      })
      .catch((err) => {
        console.log(err);
        enqueueSnackbar("Error renaming file. Please try again later", {variant: 'error'});
      })
    props.handleClose();
  };

   return(
     <div>
       <Dialog
         open={props.open}
         onClose={props.handleClose}
         aria-labelledby="rename-dialog-title"
         aria-describedby="rename-dialog-description"
         scroll='paper'
       >
        <DialogTitle id="rename-dialog-title">{"Rename File"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="rename-dialog-description">
            What would you like to rename the file?
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            label="New Filename"
            fullWidth
            onChange={(e) => handleChange(e)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} autoFocus className={classes.cancelButton}>
            Cancel
          </Button>
          <Button onClick={() => handleRename(file)} className={classes.renameButton}>
            Rename
          </Button>
        </DialogActions>
       </Dialog>
     </div>
   );
 }
