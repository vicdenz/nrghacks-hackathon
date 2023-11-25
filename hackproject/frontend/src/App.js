import {
	createBrowserRouter,
	Link,
	Route,
	RouterProvider,
	Routes,
	Outlet,
	BrowserRouter,
} from "react-router-dom";

import "./App.css";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";
import ClassroomPage from "./pages/ClassroomPage";
import SignUpPage from "./pages/SignUpPage";
import LoginPage from "./pages/LoginPage";

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route element={<Layout />}>
					<Route path="/" element={<HomePage />} />
					<Route path="/classrooms/:id" element={<ClassroomPage />} />
					<Route path="/sign-up" element={<SignUpPage />} />
					<Route path="/login" element={<LoginPage />} />
				</Route>
			</Routes>
		</BrowserRouter>
	);
}

function Layout() {
	return (
	  <>
		<div className="navbar-container">
			<Navbar /> {/* This will place your Navbar at the top of the page */}
		</div>
		<div className="container">
			<Outlet />
		</div>
	  </>
	);
  }
