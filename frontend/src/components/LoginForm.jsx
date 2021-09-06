import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import '../styles/signUpForm.less'
import TextInput from './UI/TextInput/TextInput';
import SubmitButton from './UI/SubmitButton/SubmitButton';
import { setUsername, setEmail, setPassword} from '../reducers/auth';
import { loginWithUsername } from '../actions/auth'

const SignUpForm = () => {

    const dispatch = useDispatch();

    const username = useSelector(state => state.auth.credentials.username);
    // const email = useSelector(state => state.auth.credentials.email);
    const password = useSelector(state => state.auth.credentials.password);

    const handleUsername = (e) => {
        dispatch(setUsername(e.target.value));
    };

    // const handleEmail = (e) => {
    //     dispatch(setEmail(e.target.value));
    // };

    const handlePassword = (e) => {
        dispatch(setPassword(e.target.value));
    };

    const loginUser = (e) => {
        e.preventDefault();
        dispatch(loginWithUsername(username, password));
    }

    return (
        <form 
            className="login__form"
            onSubmit={loginUser}
        >
            <label htmlFor="username">Имя пользователя</label>
            <TextInput 
                value={username}
                onChange={handleUsername}
                type="text" 
                placeholder="Введите имя пользователя" 
                id="username"
                className="login__input"
            />
            {/* <label htmlFor="email">Email</label>
            <TextInput 
                value={email}
                onChange={handleEmail}
                type="text" 
                placeholder="Введите email" 
                id="email"
                className="singUp__input"
            /> */}
            <label htmlFor="password">Пароль</label>
            <TextInput 
                value={password}
                onChange={handlePassword}
                type="password" 
                placeholder="Введите пароль" 
                id="password"
                className="login__input"
            />

            <SubmitButton className="login__btn">Войти</SubmitButton>    
        </form>
    )
}

export default SignUpForm;