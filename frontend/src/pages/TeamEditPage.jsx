import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import TeamService from "../services/teamService";
import GameService from "../services/gameService";

const TeamEditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [games, setGames] = useState([]);
  const [formData, setFormData] = useState({
    name: "",
    game_id: "",
    icon: null,
  });

  useEffect(() => {
    GameService.getGames().then(setGames);

    TeamService.getAllTeams().then((teams) => {
      const team = teams.find((t) => t.id === parseInt(id));
      if (team) {
        setFormData({
          name: team.name,
          game_id: team.game?.id || "",
          icon: null, // не подгружаем файл, только новое значение
        });
      }
    });
  }, [id]);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    if (files) {
      setFormData({ ...formData, [name]: files[0] });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append("name", formData.name);
    data.append("game_id", formData.game_id);
    if (formData.icon) {
      data.append("icon", formData.icon);
    }

    await TeamService.updateTeam(id, data);
    navigate("/admin/teams");
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-semibold mb-4">Редактирование команды</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Название команды"
          required
          className="border p-2 w-full"
        />
        <select
          name="game_id"
          value={formData.game_id}
          onChange={handleChange}
          required
          className="border p-2 w-full"
        >
          <option value="">Выберите игру</option>
          {games.map((game) => (
            <option key={game.id} value={game.id}>
              {game.name}
            </option>
          ))}
        </select>
        <input
          type="file"
          name="icon"
          accept="image/*"
          onChange={handleChange}
          className="w-full"
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2">
          Сохранить изменения
        </button>
      </form>
    </div>
  );
};

export default TeamEditPage;
