/*

    Simple 'user info' component that shows the user's profile picture
    and username in the top-right corner.

*/
import React from 'react';
import { useSelector } from 'react-redux';
import './styles.css';

const UserInfo = () => {

    const { login, avatar_url, name } = useSelector(state => state.user);

    return <div className="user-card">
        <img src={avatar_url} alt="GitHub Avatar" />
        <div className="user-card-body">
            <h5 className="name">{name}</h5>
            <p className="login">{login}</p>
        </div>
    </div>
}

export default UserInfo;