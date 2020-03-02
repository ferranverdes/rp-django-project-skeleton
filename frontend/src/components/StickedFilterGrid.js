import React, { useState } from "react";
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

const DEFAULT_SELECTED = 0;

export default function StickedFilterGrid() {
  const classes = useStyles();
  const [categorySelected, setSelectedCategory] = useState(DEFAULT_SELECTED);

  return (
    <div className={classes.root}>
      <div className={classes.firstColumn}>
        <CategoryList
          onClick={setSelectedCategory}
          selected={categorySelected}
        />
      </div>
      <div className={classes.secondColumn}>
        <GridList
          filter={
            categorySelected !== DEFAULT_SELECTED
              ? `categories__id=${categorySelected}`
              : ``
          }
        />
      </div>
    </div>
  );
}
