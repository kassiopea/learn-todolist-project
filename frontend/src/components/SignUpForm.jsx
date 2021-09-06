import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import '../styles/signUpForm.less'
import TextInput from './UI/TextInput/TextInput';
import SubmitButton from './UI/SubmitButton/SubmitButton';
import { setUsername, setEmail, setPassword} from '../reducers/auth';
import { loginWithUsername, register } from '../actions/auth'
import { getCookie } from '../_helpers';

const SignUpForm = () => {

    const dispatch = useDispatch();

    const username = useSelector(state => state.auth.credentials.username);
    const email = useSelector(state => state.auth.credentials.email);
    const password = useSelector(state => state.auth.credentials.password);
    // const isAuth = useSelector(state => state.auth.isAuth);
    const isToken = getCookie('access_token');
    const status = useSelector(state => state.auth.status)

    const handleUsername = (e) => {
        dispatch(setUsername(e.target.value));
    };

    const handleEmail = (e) => {
        dispatch(setEmail(e.target.value));
    };

    const handlePassword = (e) => {
        dispatch(setPassword(e.target.value));
    };

    const signUpUser = (e) => {
        e.preventDefault();
        dispatch(register(username, email, password));
    }

    const getTodoList =(e) => {
        dispatch(getTodoList())
    }

    useEffect(() => {
        if(isToken && status === "registered") {
            console.log(status)
            console.log(isToken)
            dispatch(loginWithUsername(username, password));
        }
    }, [status, isToken])

    return (
        <form 
            className="signUp__form"
            onSubmit={signUpUser}
        >
            <label htmlFor="username">Имя пользователя</label>
            <TextInput 
                value={username}
                onChange={handleUsername}
                type="text" 
                placeholder="Введите имя пользователя" 
                id="username"
                className="singUp__input"
            />
            <label htmlFor="email">Email</label>
            <TextInput 
                value={email}
                onChange={handleEmail}
                type="text" 
                placeholder="Введите email" 
                id="email"
                className="singUp__input"
            />
            <label htmlFor="password">Пароль</label>
            <TextInput 
                value={password}
                onChange={handlePassword}
                type="password" 
                placeholder="Введите пароль" 
                id="password"
                className="singUp__input"
            />

            <SubmitButton className="signUp__btn">Зарегистрироваться</SubmitButton>    
        </form>
    )
}

export default SignUpForm;