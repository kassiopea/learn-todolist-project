const CHANGE_USERNAME = 'CHANGE_USERNAME';
const CHANGE_EMAIL = 'CHANGE_EMAIL';
const CHANGE_PASSWORD = 'CHANGE_PASSWORD';
const CHANGE_CREDENTIALS = 'CHANGE_CREDENTIALS';
const CHANGE_STATUS = "CHANGE_STATUS"
const ISAUTH = "ISAUTH"

const initialState = {  
    credentials: {
      username: "",
      email: "",
      password: "",
      
    },
    status: null,
    isAuth: null
  }

  export default function Auth (state = initialState, action) {
  
    switch (action.type) {

        case CHANGE_USERNAME:
        return {
          ...state,
          credentials: {
            ...state.credentials,
            username: action.payload
          } 
        }

        case CHANGE_EMAIL:
          return {
            ...state,
            credentials: {
              ...state.credentials,
              email: action.payload
            }
          }

        case CHANGE_PASSWORD:
            return {
                ...state,
                credentials: {
                ...state.credentials,
                password: action.payload
                } 
            }
        case CHANGE_CREDENTIALS:
            return {
                ...state,
                credentials: action.payload
            }
        case ISAUTH:
          return {
            ...state,
            isAuth: action.payload
          }

        case CHANGE_STATUS:
          return {
            ...state,
            status: action.payload
          }
        default:
            return state;
    }

}

export const setUsername = (username) => ({type: CHANGE_USERNAME, payload: username});
export const setEmail = (email) => ({type: CHANGE_EMAIL, payload: email});
export const setPassword = (password) => ({type: CHANGE_PASSWORD, payload: password});
export const setCredentials = (credentials) => ({type: CHANGE_CREDENTIALS, payload: credentials});
export const setIsAuth = (isAuth) => ({type: ISAUTH, payload: isAuth});
export const setStatus = (status) => ({type: CHANGE_STATUS, payload: status})