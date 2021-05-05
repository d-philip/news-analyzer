import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import IconButton from '@material-ui/core/IconButton';
import MoreHorizIcon from '@material-ui/icons/MoreHoriz';

const useStyles = makeStyles((theme) =>  ({
  menu: {

  },
}));

export default function FileMenu() {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = React.useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return(
    <div>
    <IconButton className={classes.moreIcon} onClick={(e) => handleClick(e)}>
      <MoreHorizIcon />
    </IconButton>
    <Menu
      anchorEl={anchorEl}
      keepMounted
      open={anchorEl !== null}
      onClose={handleClose}
      autoFocus={false}
    >
      <MenuItem onClick={handleClose}>Analyze</MenuItem>
      <MenuItem onClick={handleClose}>Delete</MenuItem>
      <MenuItem onClick={handleClose}>Rename</MenuItem>
    </Menu>
    </div>
  )
}
