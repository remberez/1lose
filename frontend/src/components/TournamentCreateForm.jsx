import { useEffect, useState } from "react";
import tournamentService from "../services/tournamentService";
import gameService from "../services/gameService";

const TournamentCreateForm = ({ onSuccess }) => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [gameId, setGameId] = useState("");
  const [games, setGames] = useState([]);

  useEffect(() => {
    gameService.getGames().then(setGames);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await tournamentService.createTournament({ name, description, game_id: gameId });
    onSuccess?.();
    setName("");
    setDescription("");
    setGameId("");
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 mb-6">
      <h3 className="text-lg font-semibold">Создание турнира</h3>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Название"
        className="w-full border p-2 rounded"
        required
      />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Описание"
        className="w-full border p-2 rounded"
        required
      />
      <select
        value={gameId}
        onChange={(e) => setGameId(e.target.value)}
        className="w-full border p-2 rounded"
        required
      >
        <option value="">Выберите игру</option>
        {games.map((game) => (
          <option key={game.id} value={game.id}>{game.name}</option>
        ))}
      </select>
      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Создать</button>
    </form>
  );
};

export default TournamentCreateForm;
