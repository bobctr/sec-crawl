import React, { Component } from 'react';
import { REST_URL } from './settings.js'
import NewsEntry from './NewsEntry';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

class CrawlerClient extends Component {
	constructor(props) {
		super(props)
		this.state = {
			data: null,
			query: "hacker",
			filteredData: null
		}
	}

	componentDidMount(){
		fetch(REST_URL)
			.then(response => response.json())
			.then(data => {
				const { query } = this.state;
				const filteredData = data['_items'].filter(element => {
					return element.title.toLowerCase().includes(query.toLowerCase());
				});

				this.setState({
					data: data['_items'],
					query,
					filteredData
				});
			});
	};

	renderNews() {
		const newsElements = this.state.data;
		const listItems = newsElements.map((newsEntry) =>
			< NewsEntry newsInfo={newsEntry} />
		);
		return (listItems);
	}



	newsListStyle = {
		marginTop: '3%',
		border: '10px solid grey',
	};

	render() {
		return (
			<div>
				<div>
					<AppBar position="fixed" color="default">
						<Toolbar>
							<Typography variant="h6" color="inherit">
								sec-crawl-news
							</Typography>
						</Toolbar>
					</AppBar>
				</div>
				<div style={this.newsListStyle}>
					{
						this.state &&
						this.state.data &&
						this.renderNews()
					}
				</div>
			</div>
		)
	}



}

export default CrawlerClient;
