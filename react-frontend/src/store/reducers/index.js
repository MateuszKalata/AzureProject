import {combineReducers} from "redux";

import searchReducer from './search'

const allReducers = combineReducers({
    searches: searchReducer,
});

export default allReducers;