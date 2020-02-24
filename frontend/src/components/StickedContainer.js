import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  container: {
    width: "inherit",
    position: "fixed"
  }
}));

export default function StickedContainer(props) {
  const classes = useStyles();

  return <div className={classes.container}>{props.children}</div>;
}
