import React, { Component } from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import StickedFilterGrid from "./StickedFilterGrid";

const styles = theme => ({
  root: {
    display: "flex",
    height: "100%",
    width: "100%",
    justifyContent: "center"
  }
});

class App extends Component {
  static propTypes = {
    classes: PropTypes.object.isRequired
  };

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <div style={{ width: 1000 }}>
          <StickedFilterGrid />
        </div>
      </div>
    );
  }
}

export default withStyles(styles)(App);
