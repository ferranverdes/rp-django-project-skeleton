import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";

import StickedContainer from "./StickedContainer";
import useResourceList from "../hooks/useResourceList";
import { CATEGORIES_URL } from "../constants/";

const ALL_CATEGORY_ID = 0;

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex",
    flexDirection: "column"
  }
}));

export default function MyGridList(props) {
  const { onClick, selected } = props;
  const classes = useStyles();
  const categories = useResourceList(CATEGORIES_URL);

  return (
    <StickedContainer>
      <div className={classes.root}>
        <Button
          key={ALL_CATEGORY_ID}
          variant="contained"
          color="primary"
          size="small"
          style={{ margin: 5 }}
          disabled={ALL_CATEGORY_ID === selected}
          onClick={() => onClick(ALL_CATEGORY_ID)}
        >
          ALL
        </Button>
        {categories.map(category => (
          <Button
            key={category.id}
            variant="contained"
            color="primary"
            size="small"
            style={{ margin: 5 }}
            disabled={category.id === selected}
            onClick={() => onClick(category.id)}
          >
            {category.name}
          </Button>
        ))}
      </div>
    </StickedContainer>
  );
}
