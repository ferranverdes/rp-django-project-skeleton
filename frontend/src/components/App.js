import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import './App.css';

const styles = theme => ({
	root: {
		display: 'flex',
		height: '100%',
		width: '100%',
		justifyContent: 'center'
	},
	content: {
		alignSelf: 'center'
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
				<div className={classes.content}>
					<h1>Hello, World</h1>
				</div>
			</div>
		);
	}
}

export default withStyles(styles)(App);
