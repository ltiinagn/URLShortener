import React from "react";
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';
import { Link } from "react-router-dom";

export default function NavigationBar() {
	return (
		<Navbar bg="dark" variant="dark" expand="lg">
			<Container>
				<Navbar.Brand href="#home">URL Shortener</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="me-auto">
					<Link to="/" className="nav-link">Home</Link>
					<Link to="/go" className="nav-link">Go</Link>
				</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	)
}