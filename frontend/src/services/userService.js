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

    async getUserById(id) {
        const response = await api.get(`/users/${id}`);
        return response.data;
    }

    async updateUser(id, values) {
        const response = await api.patch(`/users/${id}`, values);
        return response.data;
    }

    async updateMe(values) {
        const response = await api.patch("/users/me", values);
        return response.data;
    }
}

export default new UserService();