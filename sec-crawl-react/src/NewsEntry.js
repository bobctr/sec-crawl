import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import classnames from 'classnames';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';

const styles = theme => ({
    card: {
        width: '50%',
        marginTop: '1%',
        marginLeft: '25%',
    },
    media: {
        height: 0,
        paddingTop: '56.25%', // 16:9
    },
    actions: {
        display: 'flex',
    },
    expand: {
        transform: 'rotate(0deg)',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
});

class NewsEntry extends React.Component {
    state = { 
        expanded: false 
    };

    handleExpandClick = () => {
        this.setState(state => ({ expanded: !state.expanded }));
    };

    render() {
        const { classes } = this.props;
        return (
            <Card className={classes.card}>
                <CardHeader
                    className={classes.cardheader}
                    action={
                        <IconButton>
                            <MoreVertIcon />
                        </IconButton>
                    }
                    title={this.props.newsInfo['title']}
                    subheader={
                        <span>
                            {this.props.newsInfo['website']}
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            {this.props.newsInfo['date']}
                        </span>
                    }
                />
                <CardMedia
                    className={classes.media}
                    image={this.props.newsInfo['image']}
                />
                <CardContent>
                    <Typography component="p">
                        <a href={this.props.newsInfo['_id']}>Go to Article</a>
                    </Typography>
                </CardContent>
                <CardActions className={classes.actions} disableActionSpacing>
                    <Typography>
                        Preview: 
                    </Typography>
                    <IconButton
                        className={classnames(classes.expand, {
                            [classes.expandOpen]: this.state.expanded,
                        })}
                        onClick={this.handleExpandClick}
                        aria-expanded={this.state.expanded}
                        aria-label="Show more"
                    >
                        <ExpandMoreIcon />
                    </IconButton>
                </CardActions>
                <Collapse in={this.state.expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                        <Typography>
                            {this.props.newsInfo['text']}
                        </Typography>
                    </CardContent>
                </Collapse>
            </Card>
        );
    }
}

NewsEntry.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(NewsEntry);
