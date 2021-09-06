import '../styles/header.less'
import React from 'react';
import { useDispatch } from 'react-redux';

import { logout } from '../actions/auth'
import NavBar from './UI/NavBar/NavBar';
import SubmitButton from './UI/SubmitButton/SubmitButton';
import { getCookie } from '../_helpers';

const Header = () => {

    const dispatch = useDispatch()
    const isToken = getCookie('access_token');
    const isCSRFToken = getCookie('csrf_access_token')

    const logoutUser = (e) => {
        e.preventDefault();
        dispatch(logout())
    }

    return (
        <div className="header">
            <NavBar/>
            {isCSRFToken && 
                <SubmitButton className="btn__logout" onClick={logoutUser}>Выйти</SubmitButton>
            }
            
        </div>
    )
}

export default Header;


