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

    async createGame(data) {
        try {
            const response = await api.post("/games/", data, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            });
            return response.data;
        } catch (error) {
            console.error("Ошибка при создании игры:", error);
            throw error;
        }
    }

    async deleteGame(gameId) {
        const response = await api.delete(`/games/${gameId}`);
        return response;
    }
}

    export default new GameService();
