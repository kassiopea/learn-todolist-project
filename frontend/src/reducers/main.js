const IS_LOADING = "IS_LOADING"

const initialState = {  
    isLoading: false
  }

export default function Main (state = initialState, action) {

    switch (action.type) {
        case IS_LOADING:
            return {
            ...state,
            isLoading: action.payload
            }
        default:
            return state;
    }

}

export const setIsLoading = (isLoading) => ({type: IS_LOADING, payload: isLoading});