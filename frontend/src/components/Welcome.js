import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles((theme) => ({
  paper: {
    backgroundColor: '#F8F7FF',
    margin: 20,
    padding: 20,
    width: "80%",
  },
  divider: {
    marginTop: 10,
    marginBottom: 15,
  }
}));

export default function Welcome() {
  const classes = useStyles();

  return (
    <Grid align='center'>
      <Paper elevation={1} className={classes.paper}>
        <Typography variant='h4'>Welcome to the News Analyzer!</Typography>
        <Divider className={classes.divider}/>
        <Typography variant='body1'>
          This platform allows you to upload and store news articles at anytime.
          It can then extract the text from uploaded documents to generate keywords that summarize the text and analyze the text's sentiment.
        </Typography>
        <Typography variant='body1' style={{marginTop: 30}}>
          Login to start using News Analyzer today!
        </Typography>
      </Paper>
    </Grid>
  );
}
