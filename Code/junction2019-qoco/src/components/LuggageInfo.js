import React, { Component } from 'react';
import '../App.css';

class LuggageInfo extends Component {
  render() {
    return (
      <div>

        <div style={{ backgroundColor: '#f0f4f7', paddingTop: '30px', paddingBottom: '30px' }}>
          <div className="container">
            <div className="main-nav-options">
              <a style={{ backgroundColor: '#ffffff', borderBottomColor: '#ffffff', zIndex: 3 }} href="#">LUGGAGE INFO FOR ID: 562542562</a>
            </div>
          </div>
          <div className="book-flights-option clearfix">
            <div className="row">
              <div className="column-50">
                <p>REF: 56F6D</p>
                <p>FLIGHT: AY5678</p>
                <p>DATE: 21.11.2019</p>
                <p>ORIGIN: Helsinki-Vantaa Airport</p>
                <p>DESTINATION: Munich International Airport</p>
                <p>PICTURE:</p>
                <img src="https://i.dailymail.co.uk/i/pix/2013/12/23/article-2528042-1A45D5FA00000578-698_964x631.jpg" style={{ width: '350px' }} />
              </div>

            </div>
            <div className="row">
              <div className="column-50">
                <p className="passenger-text">STATUS: IN STORAGE AT AIRPORT</p>
              </div>
              <div className="column-50">

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

export default LuggageInfo;
