import React, { Component } from 'react';
import { REST_URL } from '../../settings.js'
import NewsEntry from '../NewsEntry/NewsEntry';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import SearchBar from '../SearchBar/SearchBar';
import { Grid, withStyles } from '@material-ui/core';

const styles = theme => ({
	newsList: {
		marginTop: '80px',
		marginLeft: 'auto',
		marginRight: 'auto',
	},
	appbarTitle: {
		position: 'absolute',
		[theme.breakpoints.down('sm')]: {
			display: 'none'
		},
		[theme.breakpoints.up('md')]: {
			display: 'block'
		},
	}
})

class CrawlerClient extends Component {
	constructor(props) {
		super(props)
		this.state = {
			data: null,
			searchQuery: ""
		}
		this.getData = this.getData.bind(this);
	}

	getData() {
		const xhr = new XMLHttpRequest();
		xhr.onreadystatechange = () => {
			if (xhr.readyState !== 4) return;
			if (xhr.status >= 200 && xhr.status < 300) {
				const data = JSON.parse(xhr.responseText);
				this.setState({
					data: data._items,
				});
			}
		}
		xhr.open('GET', REST_URL);
		xhr.send();
	}

	componentDidMount() {
		this.getData();
		this.interval = setInterval(this.getData, 10000);
	};

	componentWillUnmount() {
		clearInterval(this.interval);
	}

	renderNews() {
		// filter by title
		const filteredData = this.state.data.filter(element => {
			return element.title.toLowerCase().includes(this.state.searchQuery.toLowerCase());
		});

		return filteredData.map((newsEntry) =>
			< NewsEntry newsInfo={newsEntry} key={newsEntry._id} />
		);
	}

	handleSearchChange = (event) => {
		this.setState({
			searchQuery: event.target.value
		})
	}

	render() {
		const { classes } = this.props;
		return (
			<div>
				<Grid container className="mainGreed" spacing={8}>
					<Grid item>
						<AppBar position="fixed" color="default">
							<Toolbar>
								<Typography className={classes.appbarTitle} variant="h6" color="inherit">
									sec-crawl-news
								</Typography>
								<SearchBar
									id="searchbar"
									onChange={this.handleSearchChange.bind(this)}
								/>
							</Toolbar>
						</AppBar>
					</Grid>
					<Grid item className={classes.newsList}>
						{
							this.state &&
							this.state.data &&
							this.renderNews()
						}
					</Grid>
				</Grid>
			</div>
		)
	}
}

export default withStyles(styles)(CrawlerClient);
