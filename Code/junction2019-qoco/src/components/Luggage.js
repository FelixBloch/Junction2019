import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import '../App.css';

function onClick1(){
    window.location.href="./ServicePoints.js";
};

function onClick2(){
    window.location.href="./LuggageInfo.js";
};

class Luggage extends Component {
    render() {
        return (
            <div>
                
                <div style={{ backgroundColor: '#f0f4f7', paddingTop: '30px', paddingBottom: '30px' }}>
                    <div className="container">
                        <div className="main-nav-options">
                            <a style={{ backgroundColor: '#ffffff', borderBottomColor: '#ffffff', zIndex: 3 }} href="#">LUGGAGE INFO FOR BOOKED FLIGHTS</a>
                        </div>
                    </div>
                    <div className="book-flights-option clearfix">
                        <div className="row">
                            <div className="column-100">

                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <p className="passenger-text">BOOKING REF: 56F6D</p>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                            <p className="bordered">AY1234: HEL-ARL | 22/11/2019</p>
                            <p className="bordered">STATUS: DROP OFF AVAILABLE</p>
                            </div>
                            <div className="column-50">
                            <Link to="/servicepoints">FIND DROP OFF POINT</Link>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <p className="passenger-text">BOOKING REF: 6A84X</p>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                            <p className="bordered">AY5678: HEL-MUC | 20/11/2019</p>
                            <p className="bordered">STATUS: IN STORAGE AT AIRPORT</p>
                            </div>
                            <div className="column-50">
                            <Link to="/luggageinfo">DETAILS</Link>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-100">
                                <div style={{ width: '30%', margin: '0 auto' }}>
                                    <a href="#" style={{ fontSize: '11px', color: '#737373' }}>View our Baggage and Optional Service Charges</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div style={{ backgroundColor: '#ffffff', paddingTop: '30px', paddingBottom: '30px' }}>
                    <div className="container clearfix">
                        <div className="row">
                            <div className="column-50">
                                <h1>
                                    <a className="blue-berry-heading" href="#">
                                        CELEBRATE CHRISTMAS WITH OUR SPECIAL OFFERS</a>
                                </h1>
                                <a className="blue-button clearfix">
                                    BOOK BY 21 DECEMBER</a>
                                <div className="blue-deal clearfix">
                                    <h3>HONG KONG</h3>
                                    <p>RETURN FLIGHTS FROM</p>
                                    <h4>€665</h4>
                                </div>
                            </div>
                            <div className="column-50">
                                <a href="#">
                                    <img style={{ height: '420px' }} src="images/photos/city_photo.jpg" />
                                </a></div><a href="#">
                            </a></div><a href="#">
                        </a><div className="row"><a href="#">
                        </a><div className="column-100"><a href="#">
                        </a><ul className="main-icon-list"><a href="#">
                        </a><li><a href="#">
                        </a><a href="#">
                                        </a><div><a href="./Luggage.js">
                                            <img src="/images/icons/baggage.jpg" />
                                        </a><a href="#">Baggage Information</a>
                                        </div>
                                    </li>
                                    <li>
                                        <a href="#">
                                        </a><div><a href="#">
                                            <img src="/images/icons/bed.jpg" />
                                        </a><a href="#">Hotels</a>
                                        </div>
                                    </li>
                                    <li>
                                        <a href="#">
                                        </a><div><a href="#">
                                            <img src="/images/icons/calendar.jpg" />
                                        </a><a href="#">Holiday Offers</a>
                                        </div>
                                    </li>
                                    <li>
                                        <a href="#">
                                        </a><div><a href="#">
                                            <img src="/images/icons/plane.jpg" />
                                        </a><a href="#">Special Bookings</a>
                                        </div>
                                    </li>
                                    <li>
                                        <a href="#">
                                        </a><div><a href="./Contact.js">
                                            <img src="/images/icons/question-mark.jpg" />
                                        </a><a href="#">CONTACT</a>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        );
    }
}

export default Luggage;