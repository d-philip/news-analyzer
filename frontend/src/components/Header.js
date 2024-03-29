import React from 'react';
import { AuthContext } from "../pages/App";
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Login from './Login';
import Logout from './Logout';

const useStyles = makeStyles((theme) => ({
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    textAlign: "center",
  },
  appbar: {
    backgroundColor: '#9381FF',
  },
}));

export default function Header(){
  const { state, dispatch } = React.useContext(AuthContext);
  const classes = useStyles();

  const authView = state.isAuthenticated ? <Logout /> : <Login /> ;

  return (
    <AppBar position="static" className={classes.appbar}>
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
