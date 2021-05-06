import React, { useEffect, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import FileMenu from './FileMenu';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import ExpandLessIcon from '@material-ui/icons/ExpandLess';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Collapse from '@material-ui/core/Collapse';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
  },
  nested: {
    paddingLeft: theme.spacing(4),
    width: '95%',
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
  keywords: {
    maxHeight: 200,
    width: '100%',
    overflow: 'auto',
  },
}));

export default function File(props) {
  const classes = useStyles();
  const [open, setOpen] = useState(false);
  const file = props.file_info;

  const handleOpen = () => {
    setOpen(!open);
  };

  return(
    <div className={classes.root}>
      <Divider />
      <ListItem>
        <ListItemText button primary={file.file_name} onClick={handleOpen}/>
        {open ? <ExpandLessIcon /> : <ExpandMoreIcon />}
        <FileMenu file_info={file} file_id={props.file_id} refreshFiles={props.refreshFiles}/>
      </ListItem>
      <Collapse in={open} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>

          <Accordion className={classes.nested}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography className={classes.heading}>Transcript</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <p>{file.file_content}</p>
            </AccordionDetails>
          </Accordion>

          <Accordion className={classes.nested}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography className={classes.heading}>Keywords</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <List className={classes.keywords}>
                {file.file_keywords.map(keyword => (
                  <ListItem>
                    <ListItemText primary={keyword} />
                  </ListItem>
                ))}
              </List>
            </AccordionDetails>
          </Accordion>

          <Accordion className={classes.nested}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography className={classes.heading}>Sentiment</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <p>{file.file_sentiment}</p>
            </AccordionDetails>
          </Accordion>

        </List>
      </Collapse>

    </div>
  )
}
