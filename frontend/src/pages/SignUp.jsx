import React from 'react';
import SignUpForm from '../components/SignUpForm';
import { getCookie } from '../_helpers';

const SignUp = () => {

    return (
        <main>
            <h1>Страница регистрации пользователя</h1>
            <SignUpForm/>
        </main>
    )
}

export default SignUp;