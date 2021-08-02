import React from "react";
import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from "react-router-dom";

class Go extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      url: "",
			fullURL: ""
    }
    this.handleSubmit = this.handleSubmit.bind(this);
		this.onInput = this.onInput.bind(this);
  }

	onInput(e) {
		this.setState({
			url: e.target.value
		});
	}

	handleSubmit(e) {
		if (this.state.url !== "") {
			var headers = {
				"Content-Type": "application/json"
			};
			const requestOptions = {
				mode: 'cors',
				method: 'GET',
				headers: headers,
			};
			var url = new URL(`http://127.0.0.1:8000/go/${this.state.url}`)
			fetch(url, requestOptions)
				.then(async response => {
					const data = await response.json();
					if (response.ok) {
						if (data.fullURL !==  "") {
							this.setState({
								fullURL: data.fullURL
							})
						}
						else {
							alert("Shortened URL not found!");
						}
					}
					else { // check for error response
						// get error message from body or default to response status
						const error = (data && data.message) || response.status;
						return Promise.reject(error);
					}
				})
				.catch(error => {
					console.error('There was an error!', error);
					alert(`Error: Unable to get response from backend..`)
				});
		}
		else {
			alert("Please enter a URL!");
		}
	}

	componentDidMount() {
		var url = window.location.pathname;
		if (!url.endsWith("go") && url.startsWith("/go/")) {
			this.setState({
				url: url.replace("/go/", '')
			},
			() => {
				this.handleSubmit(null);
			});
		}
	}

  render() {
    return (
      <>
				<h2>Get Link</h2>
				<Form>
					<Form.Group className="mb-3">
					<FloatingLabel controlId="floatURL" label="Link to Retrieve">
						<Form.Control type="url" onChange={this.onInput} value={this.state.url} placeholder="Enter link to retrieve.." />
					</FloatingLabel>
					</Form.Group>
					<Button variant="primary" type="button" onClick={this.handleSubmit}>
						Get Full Link!
					</Button>
				</Form>
				<br />
				{this.state.fullURL !== "" ?
					<Card>
						<Card.Header>Here is your full link!</Card.Header>
						<Card.Body>
							<Card.Text>
								<Link to={{ pathname: this.state.fullURL.startsWith("http://") || this.state.fullURL.startsWith("https://") ? this.state.fullURL : `//${this.state.fullURL}` }} target="_blank">
									{this.state.fullURL}
								</Link>
							</Card.Text>
						</Card.Body>
					</Card>
				:
					<></>
				}
			</>
    );
  }
}

export default Go;