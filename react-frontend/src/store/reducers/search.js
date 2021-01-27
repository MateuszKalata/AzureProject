import * as actionTypes from '../actions/actionTypes';

const initState = {
    isFailure: false,
    isSuccess: false,
    isLoading: false,
    errors: {},
    elements: [],
};


const searchReducer = (state = initState, action) => {
    switch (action.type) {
        case actionTypes.SEARCH_REQUEST:
            return {
                ...state,
                isFailure: false,
                isSuccess: false,
                isLoading: true,
                elements: []
            };
        case actionTypes.SEARCH_FAILURE:
            return {
                ...state,
                isFailure: true,
                isSuccess: false,
                isLoading: false,
                errors: action.errors
            };
        case actionTypes.SEARCH_SUCCESS:
            return {
                ...state,
                isFailure: false,
                isSuccess: true,
                isLoading: false,
                elements: action.elements
            };
        default:
            return state;
    }
};

export default searchReducer;