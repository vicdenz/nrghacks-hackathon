import React, { useState, useEffect } from "react";
import Header from "../components/Header";

import image1 from "../assets/images/title1.jpeg";
import image2 from "../assets/images/title2.jpeg";
import image3 from "../assets/images/title3.jpeg";
import image4 from "../assets/images/title4.jpeg";

const HomePage = () => {
	return (
        <>
            <div className="column1">
                <Header />
                
            </div>
            <div className="column2">
                <div className="header-images">
                    <img src={image1} alt="Child Learning Image One" />
                    <img src={image2} alt="Child Learning Image Two" />
                    <img src={image3} alt="Child Learning Image Three" />
                    <img src={image4} alt="Child Learning Image Four" />
                </div>
            </div>
        </>
	);
};

export default HomePage;
