/*

    OAuth components that the server redirects to on either a success of error.

*/
import React from "react";
import { useDispatch } from 'react-redux';
import { storeAccessToken } from '../../actions';
import { Redirect, useLocation } from 'react-router-dom';
const queryString = require('query-string');

export const Success = () => {
    let location = useLocation();
    let dispatch = useDispatch();

    // the most important step - store the access token in the redux store
    // and redirect to the root route.
    let access_token = queryString.parse(location.search).access_token;
    dispatch(storeAccessToken(access_token));
    return <Redirect to="/" />
}

// :(
export const Error = () => {
    return <p>Erorr Authenticating!</p>;
}