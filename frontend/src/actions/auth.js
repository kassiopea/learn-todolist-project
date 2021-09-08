import axios from "axios";
import AuthService from "../services/AuthServices";
import { history, getCookie, delCookie } from '../_helpers';
import { API_URL } from "../http";
import { setUsername, setIsAuth, setStatus } from "../reducers/auth";
import { setIsLoading } from '../reducers/main'

export const register = (username, email, password) => (dispatch) => {
    return AuthService.register(username, email, password)
    .then(
        (response) => {
            dispatch(setUsername(response.data.data.username));
            dispatch(setIsAuth(false));
            dispatch(setStatus('registered'))
      },
    ).catch(e => {
        console.log(e);
    });
  };
  
  export const loginWithUsername = (username, password) => (dispatch) => {
      return AuthService.loginWithUsername(username, password)
      .then(
          (response) => {
            dispatch(setIsAuth(true));
            history.push('/home');
          }
      ).catch(e => {
          console.log(e)
      })
  }
  
  export const logout = () => (dispatch) => {
    return AuthService.logout()
    .then(
        (response) => {
            // dispatch(setIsLoading(true));
            // dispatch(setIsLoading(false));
            console.log(response.data)
            delCookie('csrf_access_token')
            history.push('/')
      },
    ).catch(e => {
        console.log(e);
    });
  };


//   export const checkAuth = () => (dispatch) => {
//     const refreshToken = localStorage.getItem('refresh-token');
//     const header = {
//       'Authorization': `Bearer ${refreshToken}`
//     }

//     const data = new FormData ()

//     return axios.post(`${API_URL}auth/refresh`, data, {headers: header})
//     .then(
//         (response) => {
//             localStorage.setItem('token', response.data.access_token);
//             // localStorage.setItem('refresh-token', response.data.refresh_token);
//         }
        
//     ).catch(e => {
//         console.log(e);
//         // dispatch(setMessage(message));
//     })
//   }