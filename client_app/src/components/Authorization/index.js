/*

    Component that wraps any given component with requiring the user
    to be logged in to the OAuth service.

*/
import React, { useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { getUser } from '../../actions';

const SERVER_URL = `${process.env.REACT_APP_SERVER_URL || ""}/auth`

// Redirects away from the react app (in this case, to our server)
const RedirectOffServer = ({ target }) => {
    useEffect(() => {
        window.location.replace(target);
    }, [target])

    return <div>
        <span>Redirecting to {target}</span>
    </div>
}

/**
 * 
 * Authorization will evaluate if a user has access to the component and
 * return the component or a restricted page.
 * 
 * @param {any} Component 
 */
const Authorization = ({ Component, ...props}) => {
    const access_token = useSelector(state => state.access_token);
    const dispatch = useDispatch();
    useEffect(() => {
        // when we have the users access token, 
        // get the users data from the server.
        if(access_token) {
            dispatch(getUser());
        }
    }, [access_token, dispatch]);

    // redirect to the login service
    if (!access_token) {
        return <RedirectOffServer {...props}
            target={`${SERVER_URL}/login`}
        />
    } else {
        return <Component {...props} />;
    }
}

export default Authorization