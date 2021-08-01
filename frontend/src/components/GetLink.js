import React from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { Link } from "react-router-dom";

class GetLink extends React.Component {
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
					this.setState({
						fullURL: data.fullURL
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
				<h2>Get Link</h2>
				<Form>
					<Form.Group className="mb-3">
						<Form.Label>Link to Retrieve: </Form.Label>
						<Form.Control type="url" onChange={this.onInput} placeholder="Enter link.." />
					</Form.Group>
					<Button variant="primary" type="button" onClick={this.handleSubmit}>
						Get Full Link!
					</Button>
				</Form>
				<Link to={{ pathname: this.state.fullURL.startsWith("http://") || this.state.fullURL.startsWith("https://") ? this.state.fullURL : `//${this.state.fullURL}` }} target="_blank">
					{this.state.fullURL}
				</Link>
			</>
    );
  }
}

export default GetLink;