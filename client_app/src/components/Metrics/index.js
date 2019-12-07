/* 

    Component that shows the number and happy and sad people on the
    bottom of the screen.

*/
import React from 'react';
import { useSelector } from 'react-redux';
import './styles.css';

const Metrics = () => {

    // get the data from our redux store
    let numHappy = useSelector(state => state.user.num_happy)
    let numSad   = useSelector(state => state.user.num_sad)

    return <span className="metrics">there {numHappy === 1 ? "is" : "are"} {numHappy} happy {numHappy === 1 ? "person" : "people"} and {numSad} sad {numSad === 1 ? "person" : "people"}.</span>
}

export default Metrics;