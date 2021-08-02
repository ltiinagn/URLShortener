import React from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { Link } from "react-router-dom";

class Home extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      url: "",
			shortenedURL: ""
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
		var headers = {
			"Content-Type": "application/json"
		};
		const requestOptions = {
			mode: 'cors',
			method: 'POST',
			headers: headers,
			body: JSON.stringify({
        url: this.state.url
      })
		};
		var url = new URL(`http://127.0.0.1:8000/shorten/`)
		fetch(url, requestOptions)
			.then(async response => {
				const data = await response.json();
				if (response.ok) {
					this.setState({
						shortenedURL: data.shortenedURL
					})
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

  render() {
    return (
      <>
				<h2>Home</h2>
				<Form>
					<Form.Group className="mb-3">
						<Form.Label>Link to Shorten: </Form.Label>
						<Form.Control type="url" onChange={this.onInput} placeholder="Enter link.." />
					</Form.Group>
					<Button variant="primary" type="button" onClick={this.handleSubmit}>
						Shorten!
					</Button>
				</Form>
				<Link to={this.state.shortenedURL !== "" ? `go/${this.state.shortenedURL}` : "#"}>
					{this.state.shortenedURL !== "" ? `go/${this.state.shortenedURL}` : ""}
				</Link>
			</>
    );
  }
}

export default Home;