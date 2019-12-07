const user = (state = {}, action) => {
    switch (action.type) {
        case 'GET_USER_RECEIVED':
            return action.data
        case 'TOGGLE_HAPPY_RECEIVED':
            return {
                ...state,
                ...action.data
            }
        case 'TOGGLE_HAPPY_ERROR':
        case 'GET_USER_ERROR':
            // check if it's an internal error (HTTP codes >= 500)
            if(action.err.response && action.err.response.status >= 500)
                // would be a good place to use an error "toast"
                console.log(`Error getting user details: ${action.err}`)
            else
                // warning "toast"
                console.log(`${action.err.response.data}`)
            return state
        default:
            return state;
    }
}
export default user;