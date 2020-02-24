import React from "react";
import PropTypes from "prop-types";
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
    minHeight: 110
  },
  cardActions: {
    display: "flex",
    justifyContent: "flex-end"
  }
}));

function SimpleCard(props) {
  const { description, imageUrl, title, url } = props;
  const classes = useStyles();

  return (
    <Card key={url} className={classes.card} elevation={8}>
      <CardMedia
        className={classes.cardMedia}
        image={imageUrl}
        title={title}
      />
      <CardContent className={classes.cardContent}>
        <Typography gutterBottom variant="h5" component="h2">
          {title}
        </Typography>
        <Typography>
          {description.length < 70
            ? description
            : `${description.substring(0, 70)}...`}
        </Typography>
      </CardContent>
      <CardActions className={classes.cardActions}>
        <Button variant="contained" color="primary">
          More info
        </Button>
      </CardActions>
    </Card>
  );
}

SimpleCard.propTypes = {
  description: PropTypes.string.isRequired,
  imageUrl: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired
};

export default SimpleCard;
