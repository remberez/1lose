import { api } from "./api";

class BetService {
    async createBet({ event_id, outcome_id, amount }) {
        const response = await api.post("/bets", {event_id, outcome_id, amount});
        return response;
    }

    async getMyBets() {
        const response = await api.get("/bets");
        return response.data;
    }
}

export default new BetService();