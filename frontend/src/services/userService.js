import { api } from "./api";

class UserService {
    async getMe() {
        const reponse = await api.get("/users/me");
        return reponse.data;
    }

    async getUserList() {
        const response = await api.get("/users");
        return response.data;
    }
}

export default new UserService();