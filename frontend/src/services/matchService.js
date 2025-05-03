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
}

export default new MatchService();
