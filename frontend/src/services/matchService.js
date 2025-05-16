import { api } from "./api";

class MatchService {
    async getLiveMatches() {
        try {
            const response = await api.get("/matches/", {is_live: true});
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    async getAllMatches({}) {
        const response = await api.get("/matches");
        return response.data;
    }

    async getMatch(id) {
        const response = await api.get(`/matches/${id}`);
        return response.data;
    }

    async createMatch(data) {
        const response = await api.post("/matches", data);
        return response.data;
    }

    async updateMatch(id, data) {
        const response = await api.patch(`/matches/${id}`, data);
        return response.data;
    }

    async deleteMatch(matchId) {
        const response = await api.delete(`/matches/${matchId}`);
        return response.status;
    }
}

export default new MatchService();
