import { useEffect, useState } from "react";
import TeamService from "../services/teamService";
import GameService from "../services/gameService";

const TeamCreateForm = ({ onCreated }) => {
    const [name, setName] = useState("");
    const [gameId, setGameId] = useState("");
    const [icon, setIcon] = useState(null);
    const [games, setGames] = useState([]);

    useEffect(() => {
        GameService.getGames().then(setGames);
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append("name", name);
        formData.append("game_id", gameId);
        formData.append("icon", icon);

        try {
            await TeamService.createTeam(formData);
            setName("");
            setGameId("");
            setIcon(null);
            if (onCreated) onCreated();
        } catch (error) {
            console.error("Ошибка при создании команды:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 bg-white shadow rounded mb-4 space-y-4">
            <h2 className="text-xl font-semibold">Создание команды</h2>

            <div>
                <label className="block text-sm">Название</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full border rounded px-3 py-2"
                    required
                />
            </div>

            <div>
                <label className="block text-sm">Игра</label>
                <select
                    value={gameId}
                    onChange={(e) => setGameId(e.target.value)}
                    className="w-full border rounded px-3 py-2"
                    required
                >
                    <option value="">Выберите игру</option>
                    {games.map((game) => (
                        <option key={game.id} value={game.id}>
                            {game.name}
                        </option>
                    ))}
                </select>
            </div>

            <div>
                <label className="block text-sm">Иконка</label>
                <input
                    type="file"
                    accept="image/*"
                    onChange={(e) => setIcon(e.target.files[0])}
                    className="w-full"
                    required
                />
            </div>

            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
                Создать команду
            </button>
        </form>
    );
};

export default TeamCreateForm;
