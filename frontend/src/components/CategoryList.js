import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";

import StickedContainer from "./StickedContainer";
import useResourceList from "../hooks/useResourceList";
import { CATEGORIES_URL } from "../constants/";

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex",
    flexDirection: "column"
  }
}));

export default function MyGridList(props) {
  const classes = useStyles();
  const categories = useResourceList(CATEGORIES_URL);

  return (
    <StickedContainer>
      <div className={classes.root}>
        <Button
          key={0}
          variant="contained"
          color="primary"
          style={{ margin: 5 }}
        >
          ALL
        </Button>
        {categories.map(category => (
          <Button
            key={category.id}
            variant="contained"
            color="primary"
            style={{ margin: 5 }}
          >
            {category.name}
          </Button>
        ))}
      </div>
    </StickedContainer>
  );
}
