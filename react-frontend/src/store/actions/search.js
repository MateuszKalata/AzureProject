import * as actionTypes from './actionTypes';
import axios from '../axios-backend';

const requestSearch = () => {
    return {
        type: actionTypes.SEARCH_REQUEST,
    }
}

const failureSearch = (errors) => {
    return {
        type: actionTypes.SEARCH_FAILURE,
        errors: errors
    }
}

const successSearch = (elements) => {
    return {
        type: actionTypes.SEARCH_SUCCESS,
        elements: elements
    }
}

export const fetchElements = (query) => {
    return (dispatch) => {
        dispatch(requestSearch())
        axios({
			url: "/api/search?query=" + query,
			crossDomain: true,
			// withCredentials: true,
			// responseType: 'arraybuffer',
			async: true,
			method: 'GET',
			// data: {}
		})
		.then(res => {
            let v = res.data
            console.log("v = ", v[0])
			dispatch(successSearch(v));
		})
		.catch(error => {
			dispatch(failureSearch(error));
		})
    }
}