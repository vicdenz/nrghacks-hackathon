import React, { useState, useEffect } from "react";
import Header from "../components/Header";

const HomePage = () => {
	return (
        <>
            <div className="column1">
                <Header />
            </div>
            <div className="column2">
                <div className="header-images">
                    <img src="assets/images/child-learning-1.jpeg" alt="Child Learning" />
                    <img src="assets/images/child-learning-2.jpeg" alt="Child Learning" />
                    <img src="assets/images/child-learning-3.jpeg" alt="Child Learning" />
                </div>
            </div>
        </>
	);
};

export default HomePage;
