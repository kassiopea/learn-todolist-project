import {combineReducers} from 'redux';
import {createStore, applyMiddleware} from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';

import Auth from './auth';
import Main from './main';

const rootReducer = combineReducers({
    auth: Auth,
    main: Main
});

export const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)));