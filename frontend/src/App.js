import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import NavigationBar from "./components/NavigationBar.js";
import Home from "./components/Home.js";
import Go from "./components/Go.js";
import {
	BrowserRouter as Router,
	Switch,
	Route
} from "react-router-dom";

export default function App() {
	return (
		<>
			<Router>
				<NavigationBar />
				<Switch>
					<Route path="/go">
						<Go />
					</Route>
					<Route path="/">
						<Home />
					</Route>
				</Switch>
			</Router>
		</>
	);
}