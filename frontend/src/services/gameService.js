import {api} from "./api";

class GameService {
    async getGames() {
        try {
            const response = await api.get("/games/");
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }
}

export default new GameService();
