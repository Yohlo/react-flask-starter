export const storeAccessToken = (access_token) => ({
    type: 'STORE_ACCESS_TOKEN',
    access_token
});

export const getUser = (create=false) => ({
    type: 'GET_USER',
    create
});

export const toggleHappiness = () => ({
    type: 'TOGGLE_HAPPY'
});