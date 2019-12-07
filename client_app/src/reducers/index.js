import { combineReducers } from 'redux';
import access_token from './access_token';
import user from './user';

const rootReducer = combineReducers({
    access_token,
    user
});

export default rootReducer;