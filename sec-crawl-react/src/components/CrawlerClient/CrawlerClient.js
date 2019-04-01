import React, { Component } from 'react';
import { REST_URL } from '../../settings.js'
import NewsEntry from '../NewsEntry/NewsEntry';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import SearchBar from '../SearchBar/SearchBar';


class CrawlerClient extends Component {
	constructor(props) {
		super(props)
		this.state = {
			data: null,
			searchQuery: ""
		}
	}

	componentDidMount(){
		fetch(REST_URL)
			.then(response => response.json())
			.then(data => {
				const { searchQuery: query } = this.state;
				this.setState({
					data: data._items,
					query
				});
			});
	};

	renderNews() {
		// filter by title
		const filteredData = this.state.data.filter(element => {
			return element.title.toLowerCase().includes(this.state.searchQuery.toLowerCase());
		});
		
		return filteredData.map((newsEntry) =>
			< NewsEntry newsInfo={newsEntry} key={newsEntry._id}/>
		);
	}

	handleSearchChange = (event) => {
		this.setState({
			searchQuery: event.target.value
		})
	}

	styles = {		
		newsListStyle: {
			marginTop: '5%',
		},
		searchBar: {
			marginLeft: '25%'
		}
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
							<div style={this.styles.searchBar}>
								<SearchBar 
									onChange={this.handleSearchChange.bind(this)}
								/>
							</div>		
						</Toolbar>					
					</AppBar>
				</div>
				<div style={this.styles.newsListStyle}>
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
