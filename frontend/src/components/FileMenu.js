import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import IconButton from '@material-ui/core/IconButton';
import MoreHorizIcon from '@material-ui/icons/MoreHoriz';
import DeleteDialog from './DeleteDialog';
import AnalyzeDialog from './AnalyzeDialog';

const useStyles = makeStyles((theme) =>  ({

}));

export default function FileMenu(props) {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [analyzeDialogOpen, setAnalyzeDialogOpen] = useState(false);
  const [renameDialogOpen, setRenameDialogOpen] = useState(false);
  const file = props.file_info;

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleDeleteOpen = () => {
    setDeleteDialogOpen(true);
  }

  const handleDeleteClose = () => {
    setDeleteDialogOpen(false);
    handleClose();
  };

  const handleAnalyzeOpen = () => {
    setAnalyzeDialogOpen(true);
  }

  const handleAnalyzeClose = () => {
    setAnalyzeDialogOpen(false);
    handleClose();
  }

  const handleRenameOpen = () => {
    setRenameDialogOpen(true);
  }

  const handleRenameClose = () => {
    setRenameDialogOpen(false);
    handleClose();
  }

  return(
    <div>
      <DeleteDialog
        open={deleteDialogOpen}
        handleClose={handleDeleteClose}
        file_info={file}
        file_id={props.file_id}
        refreshFiles={props.refreshFiles}
      />
      <AnalyzeDialog
        open={analyzeDialogOpen}
        handleClose={handleAnalyzeClose}
        file_info={file}
        file_id={props.file_id}
        refreshFiles={props.refreshFiles}
      />


      <IconButton className={classes.moreIcon} onClick={(e) => handleClick(e)}>
        <MoreHorizIcon />
      </IconButton>
      <Menu
        anchorEl={anchorEl}
        keepMounted
        className={classes.menu}
        open={anchorEl !== null}
        onClose={handleClose}
        autoFocus={false}
      >
        <MenuItem onClick={() => handleAnalyzeOpen()}>Analyze</MenuItem>
        <MenuItem onClick={() => handleDeleteOpen()}>Delete</MenuItem>
        <MenuItem onClick={() => handleRenameOpen()}>Rename</MenuItem>
      </Menu>
    </div>
  )
}
