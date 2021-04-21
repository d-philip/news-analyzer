import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles((theme) => ({
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    textAlign: "center",
  },
}));

export default function Header(){
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();

  const authView = state.isAuthenticated ? <p>Logout</p> : <p>Login</p> ;

  return (
    <AppBar position="static">
      <Toolbar variant="dense">
        <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
          <MenuIcon />
        </IconButton>
        <Typography variant="h6" className={classes.title}>
          News Analyzer
        </Typography>
        {authView}
      </Toolbar>
    </AppBar>
  )
}
