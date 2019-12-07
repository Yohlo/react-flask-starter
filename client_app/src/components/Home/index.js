/*

    Our homepage!

*/
import React from 'react';
import { useSelector } from 'react-redux';
import HappyToggle from '../HappyToggle';

const Home = () => {
    // selects the happiness data from our redux store
    let isHappy = useSelector(state => state.user.is_happy);
    return <div>
        <h1>React Starter</h1>
        <HappyToggle />
        <h3>I am {isHappy ? "happy" : "sad"}!</h3>
    </div>
}

export default Home;