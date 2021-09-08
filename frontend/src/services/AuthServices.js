import $api from "../http";

const authRoute = "auth/";

export default class AuthService {

    static async register(username, email, password) {
        const authFormData = new FormData();
        authFormData.append("username", username);
        authFormData.append("email", email);
        authFormData.append("password", password);
        return $api.post(authRoute + 'register', authFormData);
    }

    static async loginWithUsername(username, password) {
        const authFormData = new FormData();
        authFormData.append("username", username);
        authFormData.append("password", password);
        return $api.post(authRoute + 'login', authFormData);    
    }

    static async logout() {
        return $api.delete(authRoute + 'logout');
    }

    //перенесте в profile
    static async getProfileInfo() {
        return $api.get('users/profile');
    }
}