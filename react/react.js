// npm install react
// npm  install react-dom
// npm install prop-types

import React from ‘react’
import ReactDOM from ‘react-dom’
import {PropTypes} from ‘prop-types’


const title = React.createElement(‘h1’ ,{ } , ‘First React Element’ );
ReactDOM.render()

//var props = { foo: 'default' };
//var component = <Component {...props} foo={'override'} />;
//console.log(component.props.foo); // 'override'

// Validating of types

//Person.propTypes = {
//	name: PropTypes.string,
//	age: PropTypes.number
//};
