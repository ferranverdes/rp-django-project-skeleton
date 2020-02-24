import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import CategoryList from "./CategoryList";
import GridList from "./GridList";

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    display: "flex",
    justifyContent: "center"
  },
  firstColumn: {
    flexBasis: "30%",
    display: "flex",
    justifyContent: "center"
  },
  secondColumn: {
    flexBasis: "60%",
    display: "flex",
    justifyContent: "center"
  }
}));

export default function StickedFilterGrid() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <div className={classes.firstColumn}>
        <CategoryList />
      </div>
      <div className={classes.secondColumn}>
        <GridList />
      </div>
    </div>
  );
}
