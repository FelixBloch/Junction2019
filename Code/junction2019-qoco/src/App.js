import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Home from './components/Home';
import Luggage from './components/Luggage';
import Contact from './components/Contact';
import ServicePoints from './components/ServicePoints';
import LuggageInfo from './components/LuggageInfo';

function App() {
  return (
    <div>

      <Router>
        <header>
          <div>
            <div className="header-1 clearfix">
              <Link to="/">
                <img src="/images/logo/Finnair_Logo.svg.png" style={{ width: '150px', float: 'left', paddingTop: '10px' }} />
              </Link>

              <div style={{ float: 'right', width: '600px' }}>
                <ul className="top-nav">
                  <li>
                    <Link to="/"> FINLAND - EN </Link>
                  </li>
                  <li>
                    <Link to="/"> CUSTOMER CARE </Link>
                  </li>
                  <li>
                    <Link to="/"> JOHN SMITH </Link>
                  </li>
                </ul>
              </div>
            </div>
            <div style={{ backgroundColor: '#0d1973' }}>
              <div className="header-2 clearfix">
                <ul className="main-nav">
                  <li>
                    <Link to="/">DESTINATIONS & OFFERS </Link>
                  </li>
                  <li>
                    <Link to="/">PREPARE </Link>
                  </li>
                  <li>
                    <Link to="/">TRAVEL & FLY </Link>
                  </li>
                  <li>
                    <Link to="/luggage">LUGGAGE</Link>
                  </li>
                  <li>
                    <Link to="/">CUSTOMER CARE </Link>
                  </li>
                  <li>
                    <Link to="/">FINNAIR PLUS</Link>
                  </li>
                  <li style={{ borderRight: '1px solid white' }}>
                    <Link to="/">BUSINESS TRAVEL</Link>
                  </li>
                </ul>
              </div>
            </div>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route path="/luggage" component={Luggage} />
              <Route path="/luggageinfo" component={LuggageInfo} />
              <Route path="/servicepoints" component={ServicePoints} />
              <Route render={() => <h1>Page not found</h1>} />
            </Switch>
          </div>
        </header>
      </Router>
    </div>
  );
}

export default App;

/*
      <Home />
      <Luggage />
      <ServicePoints />
      <LuggageInfo />
      <Contact />
*/