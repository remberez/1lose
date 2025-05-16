import { api } from "./api";

class TeamService {
    async getAllTeams() {
        const response = await api.get("/ea-teams");
        return response.data;
    }

    async createTeam(formData) {
        const response = await api.post("/ea-teams", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
        return response.data;
    }

    async updateTeam(id, formData) {
        const response = await api.patch(`/ea-teams/${id}`, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
        return response.data;
    }
}

export default new TeamService();