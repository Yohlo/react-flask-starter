/*

    Based off of Soham Kamani's excellent write-up on simplified API usage with redux [1].

    [1]: https://www.sohamkamani.com/blog/2016/06/05/redux-apis/

*/
import axios from 'axios';

const getApiGenerator = next => (route, name) =>
    axios.get(route, {
        headers: {
            'Content-Type': 'application/json',
          }})
        .then(res => {
            next({
                type: `${name}_RECEIVED`,
                data: res.data
            })
        },
        (err) => {
            console.log(err);
            return next({
                type: `${name}_ERROR`,
                err
            })
        })

const postApiGenerator = next => (route, name, data) =>
    axios.post(route, data, {
        headers: {
            'Content-Type': 'application/json',
          }})
        .then(res => {
            next({
                type: `${name}_RECEIVED`,
                data: res.data
            })
        },
        (err) => {
            console.log(err);
            return next({
                type: `${name}_ERROR`,
                err
            })
        })


const dataService = store => next => action => {
    next(action)
    var url;
    var state = store.getState();
    const getApi  = getApiGenerator(next);
    const postApi = postApiGenerator(next);

    const SERVER_URL = `${process.env.REACT_APP_SERVER_URL || ""}/api`
    
    switch (action.type) {
        case 'GET_USER':
            url = `${SERVER_URL}/user?access_token=${state.access_token}`
            getApi(url, action.type)
            break
        case 'TOGGLE_HAPPY':
            url = `${SERVER_URL}/toggleHappiness?access_token=${state.access_token}`
            postApi(url, action.type, {})
            break
        default:
            break
    }
}

export default dataService;