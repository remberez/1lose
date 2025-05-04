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
}

export default new MatchService();
