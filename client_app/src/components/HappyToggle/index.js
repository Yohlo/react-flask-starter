/*

    Component that toggles happy/sad when you click it.

*/
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { toggleHappiness } from '../../actions';
import './styles.css';

const HappyToggle = () => {
    const dispatch = useDispatch();
    const isHappy = useSelector(state => state.user.is_happy);

    // when the button is click, dispatch the toggle action!
    const handleClick = () => dispatch(toggleHappiness());

    return <div className="happy-toggle-container">
        <button  className={`happy-toggle ${isHappy ? "happy" : "sad"}`}
            onClick={handleClick} />
        <p>click to toggle</p>
    </div>
}

export default HappyToggle;