import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import { StickyContainer, Sticky } from "react-sticky";

import useResourceList from "../hooks/useResourceList";
import { COURSES_URL } from "../constants/";
import CourseCard from "./CourseCard";

const useStyles = makeStyles(theme => ({
  gridRoot: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "space-around",
    overflow: "hidden",
    backgroundColor: theme.palette.background.paper
  },
  // Overriding tile style class
  tile: {
    height: "100%",
    display: "block",
    overflow: "visible",
    position: "relative"
  },
  gridList: {
    maxWidth: 600,
    padding: "20px"
  },
  root: {
    display: "flex",
    flexDirection: "row"
  },
  categoryList: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center"
  }
}));

// <div className={classes.categoryList} style={style}>
// 	<Typography gutterBottom variant="h5" component="h2">
// 		Categories
// 	</Typography>
// 	{[0, 1, 2].map(category => (
// 		<Button
// 			variant="contained"
// 			color="primary"
// 			style={{ margin: 5 }}
// 		>
// 			More info
// 		</Button>
// 	))}
// </div>

export default function TitlebarGridList() {
  const classes = useStyles();
  const courses = useResourceList(COURSES_URL);

  return (
    <div className={classes.root}>
      <StickyContainer className="container">
        <Sticky>
          {({ style }) => (
            <div className={classes.categoryList} style={style}>
              <Typography gutterBottom variant="h5" component="h2">
                Categories
              </Typography>
              {[
                { name: "All" },
                { name: "Software Development" },
                { name: "Information Security" }
              ].map(category => (
                <Button
                  variant="contained"
                  color="primary"
                  style={{ margin: 5 }}
                >
                  {category.name}
                </Button>
              ))}
            </div>
          )}
        </Sticky>

        <div style={{ minWidth: "200px" }}></div>
      </StickyContainer>
      <div className={classes.gridRoot}>
        <GridList cellHeight={180} className={classes.gridList}>
          {courses.map(course => (
            <GridListTile
              key={course.url}
              classes={{ tile: classes.tile }}
              style={{ height: "inherit", minWidth: "250px", padding: 10 }}
            >
              <CourseCard course={course} />
            </GridListTile>
          ))}
        </GridList>
      </div>
    </div>
  );
}
