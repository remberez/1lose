import { api } from "./api";

class UserService {
    async getMe() {
        try {
            const reponse = await api.get("/auth/me");
            return reponse.data;
        } catch (error) {
            console.error(error);
        }
    }
}

export default new UserService();