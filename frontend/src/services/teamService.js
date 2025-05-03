import { api } from "./api";

class TeamService {
    async getAllTeams() {
        const response = await api.get("/ea-teams");
        return response.data;
    }
}

export default new TeamService();