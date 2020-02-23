import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
  card: {
    height: "100%",
    display: "flex",
    flexDirection: "column",
    overflow: "visible"
  },
  cardMedia: {
    paddingTop: "56.25%" // 16:9
  },
  cardContent: {
    flexGrow: 1
  },
  cardActions: {
    display: "flex",
    justifyContent: "flex-end"
  }
}));

export default function CourseCard(props) {
  const classes = useStyles();
	const { course } = props;

  return (
    <Card key={course.url} className={classes.card} elevation={6}>
      <CardMedia
        className={classes.cardMedia}
        image={course.preview_image}
        title={course.title}
      />
      <CardContent className={classes.cardContent}>
        <Typography gutterBottom variant="h5" component="h2">
          {course.title}
        </Typography>
        <Typography>{course.description}</Typography>
      </CardContent>
      <CardActions className={classes.cardActions}>
        <Button variant="contained" color="primary">
          More info
        </Button>
      </CardActions>
    </Card>
  );
}
