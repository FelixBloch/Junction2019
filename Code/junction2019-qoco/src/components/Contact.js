import React, { Component } from 'react';
import '../App.css';

class Contact extends Component {
    render() {
        return (
            <div>
                
                <div style={{ backgroundColor: '#f0f4f7', paddingTop: '30px', paddingBottom: '30px' }}>
                    <div className="container">
                        <div className="main-nav-options">
                            <a style={{ backgroundColor: '#ffffff', borderBottomColor: '#ffffff', zIndex: 3 }} href="#">BOOK</a>
                            <a href="#">MANAGE BOOKING</a>
                            <a href="#">CHECK-IN</a>
                        </div>
                    </div>
                    <div className="book-flights-option clearfix">
                        <div className="row">
                            <div className="column-100">
                                <ul className="path-options">
                                    <li>
                                        <input type="radio" id="round-trip" name="round-trip" />
                                        <label htmlFor="round-trip">RETURN</label>
                                    </li>
                                    <li>
                                        <input type="radio" id="one-way" name="one-way" />
                                        <label htmlFor="one-way">ONE WAY</label>
                                    </li>
                                    <li>
                                        <input type="radio" id="stopover" name="stopover" />
                                        <label htmlFor="stopover">OTHER OPTIONS</label>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-from" placeholder="FROM" size={30} />
                            </div>
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-to" placeholder="TO" size={30} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-departure" placeholder="DEPARATURE" size={30} />
                            </div>
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-return" placeholder="RETURN" size={30} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <p className="passenger-text">PASSENGERS</p>
                            </div>
                            <div className="column-50">
                                <p className="passenger-text">TRAVEL CLASS</p>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-passengers" placeholder="1 ADULT" size={30} />
                            </div>
                            <div className="column-50">
                                <input className="airport-field" type="text" name="airport-travel-class" placeholder="ECONOMY" size={30} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-50">
                                <input type="checkbox" name="flexible-for" />
                                <label style={{ fontSize: '12px', color: '#464646' }} htmlFor="flexible-for">FLEXIBLE FOR +/- 3 DAYS</label>
                            </div>
                            <div className="column-50">
                                <input type="checkbox" name="finnait-plus" />
                                <label htmlFor="finnait-plus">THIS IS A FINNAIR PLUS AWARD FLIGHT </label>
                            </div>
                        </div>
                        <div className="row">
                            <div className="column-100">
                                <div className="find-flights-button">
                                    <p>FIND FLIGHTS
                  </p></div>
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
                        <a href="#">
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

export default Contact;