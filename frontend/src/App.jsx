import './styles/app.less';
import React, { useEffect } from 'react';
import { Router } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import { getCookie, history } from './_helpers';
import AppRouter from './components/AppRouter';
import Header from './components/Header';
// import { getProfileInfo } from './actions/auth';
// import { checkAuth } from './actions/auth';

const App = () => {

    const dispatch = useDispatch()
    const isToken = getCookie('access_token');

    // useEffect(() => {
    //     if(isToken){
    //         dispatch(getProfileInfo())
    //     }
        
    // }, [])

    return (
        <Router history={history}>
            <Header/>
            <AppRouter/>
        </Router>
    )
}

export default App;