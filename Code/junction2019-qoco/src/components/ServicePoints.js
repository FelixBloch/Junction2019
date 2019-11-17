import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom';
import '../App.css';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const mapStyles = {
  position: 'relative',
  width: '72.6%',
  height: '95%'
};

export class ServicePoints extends Component {
  constructor(props) {
    super(props);

    // const { lat, lng } = this.props.initialCenter;
    // this.state = {
    //     currentLocation: {
    //         lat: 60.185652700000006,
    //         lng: 24.825037899999998
    //     }
    // };

    this.state = {
      stores: [
        { lat: 60.1699, lng: 24.9384 },
        { latitude: 60.1699, longitude: 24.9384, txt: '' },
        { latitude: 60.171231, longitude: 24.941445, txt: '' }, //
        { latitude: 60.198854, longitude: 24.933297, txt: '' }, //
        { latitude: 60.251319, longitude: 25.011208, txt: '' }, //
        { latitude: 60.169461, longitude: 24.933939, txt: '' }, //
        { latitude: 60.185119, longitude: 24.823014, txt: 'Your location' }, //
        { latitude: 60.164612, longitude: 24.928973, txt: 'Abrahaminkatu 6-4, 00180 Helsinki' }, //Abrahaminkatu 6-4, 00180 Helsinki
        { latitude: 60.172194, longitude: 24.957422, txt: 'Vironkatu 4, 00170 Helsinki' }, //Vironkatu 4, 00170 Helsinki
        { latitude: 60.19075, longitude: 24.951674, txt: '' }, //Aleksis Kiven katu 11-15
        { latitude: 60.213181, longitude: 24.946905, txt: '' }, //Osmontie 23, 00610 Helsinki
        { latitude: 60.255721, longitude: 24.931231, txt: '' }, //Kuusmiehentie 38-34, Helsinki
        { latitude: 60.316415, longitude: 60.316415, txt: '' }, //Airport
        { latitude: 60.218711, longitude: 24.868416, txt: '' }, //Strömbergintie 5, 00380 Helsinki
        { latitude: 60.206811, longitude: 24.821241, txt: '' }, //Ruukinrannantie 10, 02600 Espoo
        { latitude: 60.196301, longitude: 25.06079, txt: '' }, //Herttoniemi, 00820 Helsinki
        { latitude: 60.258852, longitude: 25.011701, txt: '' }, //Vainiotie 1-3, 00700 Helsinki
        { latitude: 60.233146, longitude: 25.114725, txt: '' }, //Länsimäentie 00970 Helsinki
      ]
    }
  }

  displayMarkers = () => {
    return this.state.stores.map((store, index) => {
      return <Marker key={index} id={index} position={{
        lat: store.latitude,
        lng: store.longitude,
        title: store.txt,
        label: { color: '#00aaff', fontWeight: 'bold', fontSize: '14px', text: store.txt },
      }}
        onClick={() => console.log("You clicked me!")} />
    })
  }

  // componentDidMount() {
  //     if (this.props.centerAroundCurrentLocation) {
  //         if (navigator && navigator.geolocation) {
  //             navigator.geolocation.getCurrentPosition(pos => {
  //                 const coords = pos.coords;
  //                 this.setState({
  //                     currentLocation: {
  //                         lat: coords.latitude,
  //                         lng: coords.longitude
  //                     }
  //                 });
  //             });
  //         }
  //     }
  //     this.loadMap();
  // }

  // componentDidUpdate(prevProps, prevState) {
  //     if (prevProps.google !== this.props.google) {
  //         this.loadMap();
  //     }
  //     if (prevState.currentLocation !== this.state.currentLocation) {
  //         this.recenterMap();
  //     }
  // }

  // loadMap() {
  //     if (this.props && this.props.google) {
  //         const { google } = this.props;
  //         const maps = google.maps;

  //         const mapRef = this.refs.map;

  //         const node = ReactDOM.findDOMNode(mapRef);

  //         let { zoom } = this.props;
  //         const { lat, lng } = this.state.currentLocation;
  //         const center = new maps.LatLng(lat, lng);
  //         const mapConfig = Object.assign(
  //             {},
  //             {
  //                 center: center,
  //                 zoom: zoom
  //             }
  //         );
  //         this.map = new maps.Map(node, mapConfig);
  //     }
  // }

  // recenterMap() {
  //     const map = this.map;
  //     const current = this.state.currentLocation;

  //     const google = this.props.google;
  //     const maps = google.maps;

  //     if (map) {
  //         let center = new maps.LatLng(current.lat, current.lng);
  //         map.panTo(center);
  //     }
  // }

  // renderChildren() {
  //     const { children } = this.props;

  //     if (!children) return;

  //     return React.Children.map(children, c => {
  //         if (!c) return;
  //         return React.cloneElement(c, {
  //             map: this.map,
  //             google: this.props.google,
  //             mapCenter: this.state.currentLocation
  //         });
  //     });
  // }

  // state = {
  //     showingInfoWindow: false,
  //     activeMarker: {},
  //     selectedPlace: {}
  // };

  // onMarkerClick = (props, marker, e) =>
  //     this.setState({
  //         selectedPlace: props,
  //         activeMarker: marker,
  //         showingInfoWindow: true
  //     });

  // onClose = props => {
  //     if (this.state.showingInfoWindow) {
  //         this.setState({
  //             showingInfoWindow: false,
  //             activeMarker: null
  //         });
  //     }
  // };

  render() {
    return (
      <div>

        <div style={{ backgroundColor: '#f0f4f7', paddingTop: '30px', paddingBottom: '30px' }}>
          <div className="container" >
            <div className="main-nav-options">
              <a style={{ backgroundColor: '#ffffff', borderBottomColor: '#ffffff', zIndex: 3 }} href="#">FIND CLOSEST BAGGAGE DROP</a>
            </div>
          </div>
          <div className="book-flights-option clearfix" style={{ height: "579px" }}>
            <div>
              <Map
                google={this.props.google}
                zoom={14}
                style={mapStyles}
                initialCenter={{ lat: 60.1857079, lng: 24.824989499999997 }}
              >
                {this.displayMarkers()}
              </Map>
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

// export default ServicePoints;

export default GoogleApiWrapper({
  apiKey: 'AIzaSyCNr8r-DGOr1NAsSSywe2QUuEBXQ9ktZB8'
})(ServicePoints);
