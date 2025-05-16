import GameAdminList from "../components/GameAdminList"
import GameForm from "../components/GameCreateForm";
import { useEffect, useState } from "react";
import gameService from "../services/gameService";

const GameAdminPage = () => {
  const [games, setGames] = useState([]);

  const fetchGames = async () => {
    const data = await gameService.getGames();
    setGames(data);
  };

  useEffect(() => {
    fetchGames();
  }, []);

  async function onGameDelete(gameId) {
    const response = await gameService.deleteGame(gameId);

    if (response.status === 200) {
        await fetchGames();
    } else {
        console.error(response)
    }
  }

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Создание новой игры</h2>
      <GameForm onCreated={fetchGames} />

      <h2 className="text-2xl font-bold mb-4">Список игр</h2>
      <GameAdminList games={games} onGameDelete={onGameDelete}/>
    </div>
  );
};

export default GameAdminPage;
