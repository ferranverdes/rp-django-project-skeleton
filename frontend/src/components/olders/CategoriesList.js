import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import useResourceList from "../hooks/useResourceList";
import { CATEGORIES_URL } from "../constants/";

const useStyles = makeStyles(theme => ({}));

export default function ResourceList(props) {
  const classes = useStyles();
  const categories = useResourceList(CATEGORIES_URL);

  return (
    <div>
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
  );
}
