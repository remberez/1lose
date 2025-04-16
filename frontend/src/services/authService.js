import { api } from "./api";

class AuthService {
    async login(username, password) {
        try {
            const formData = new URLSearchParams();
            formData.append("username", username);
            formData.append("password", password);

            const response = await api.post("/auth/login/", formData, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            });
            
            return response.data;
        } catch (e) {
            console.error(e);
        }
    }

    async register(email, password) {
        try {
            const formData = new URLSearchParams();
            formData.append("email", email);
            formData.append("password", password);

            const response = await api.post("/auth/register", formData, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            });

            return response.data;
        } catch (e) {
            console.error(e);
        }
    }

    async logout() {
        try {
            const response = await api.post("/auth/logout/");
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    async register(email, password) {
        try {
            const response = await api.post("/auth/register", {email, password});
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }
}

const authService = new AuthService();
export default authService;
