import React from 'react';
import { NavLink } from 'react-router-dom';
import { getCookie } from '../../../_helpers';
import './navbar.less'

const NavBar = () => {
    const isToken = getCookie('access_token');
    const isCSRFToken = getCookie('csrf_access_token');

    return (


        <nav className="navbar">
            {isCSRFToken 
                ?
                <>
                <NavLink to="/home" activeClassName="active" className="nav__item">Главная</NavLink> 
                {/* <NavLink to="/profile" activeClassName="active" className="nav__item">Профиль</NavLink>
                <NavLink to="/tasks" activeClassName="active" className="nav__item">Задачи</NavLink> */}
                </>
                :
                <>
                <NavLink to="/" activeClassName="active" className="nav__item">Главная</NavLink>
                <NavLink to="/login" activeClassName="active" className="nav__item">Войти</NavLink>
                <NavLink to="/sign-up" activeClassName="active" className="nav__item">Зарегистрироваться</NavLink>
                </>
            }
            {/* <Link to="/profile">Профиль</Link>
            <Link to="/todo-list">Список задач</Link>
            <Link to="/login">Войти</Link> */}
            {/* <Link to="/logout">Выйти</Link> */}
        </nav>
    )
}

export default NavBar;