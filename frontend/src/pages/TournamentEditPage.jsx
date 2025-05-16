import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import tournamentService from "../services/tournamentService";
import gameService from "../services/gameService";

const TournamentEditPage = () => {
  const { id } = useParams(); 
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [gameId, setGameId] = useState("");
  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchTournament() {
      try {
        const tournament = await tournamentService.getTournamentById(id);
        setName(tournament.name);
        setDescription(tournament.description);
        setGameId(tournament.game?.id || "");
        setLoading(false);
      } catch (error) {
        console.error("Ошибка при загрузке турнира", error);
      }
    }

    async function fetchGames() {
      const gamesData = await gameService.getGames();
      setGames(gamesData);
    }

    fetchGames();
    fetchTournament();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await tournamentService.updateTournament(id, {
        name,
        description,
        game_id: gameId,
      });
      navigate("/admin/tournaments");
    } catch (error) {
      console.error("Ошибка при обновлении турнира", error);
    }
  };

  if (loading) return <div>Загрузка...</div>;

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-xl font-semibold mb-4">Редактирование турнира</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
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
            <option key={game.id} value={game.id}>
              {game.name}
            </option>
          ))}
        </select>
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Сохранить
        </button>
      </form>
    </div>
  );
};

export default TournamentEditPage;
