import Main from '../pages/Main';
import SignUp from '../pages/SignUp';
import Login from '../pages/Login';
import Home from '../pages/Home';

export const privateRouters = [
    {path: '/home', component: Home, exact: true},
]

export const publicRouters = [
    {path: '/', component: Main, exact: true},
    {path: '/sign-up', component: SignUp, exact: true},
    {path: '/login', component: Login, exact: true}
]