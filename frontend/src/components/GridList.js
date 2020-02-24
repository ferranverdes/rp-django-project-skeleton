import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";

import useResourceList from "../hooks/useResourceList";
import { COURSES_URL } from "../constants/";

import SimpleCard from "./SimpleCard";

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    backgroundColor: theme.palette.background.paper
  },
	// Overriding tile style class
  tile: {
    padding: 20,
    height: "auto"
  }
}));

export default function MyGridList(props) {
  const classes = useStyles();
  const items = useResourceList(COURSES_URL);

  return (
    <div className={classes.root}>
      <GridList>
        {items.map(course => (
          <GridListTile
            key={course.url}
            classes={{ tile: classes.tile }}
            style={{ height: "inherit" }}
          >
            <SimpleCard
              description={course.subtitle}
              imageUrl={course.preview_image}
              title={course.title}
              url={course.url}
            />
          </GridListTile>
        ))}
      </GridList>
    </div>
  );
}
