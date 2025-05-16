import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import matchService from "../services/matchService";
import tournamentService from "../services/tournamentService";
import teamService from "../services/teamService";

const MatchEditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [bestOf, setBestOf] = useState(1);
  const [dateStart, setDateStart] = useState("");
  const [dateEnd, setDateEnd] = useState("");
  const [tournamentId, setTournamentId] = useState("");
  const [firstTeamId, setFirstTeamId] = useState("");
  const [secondTeamId, setSecondTeamId] = useState("");
  const [score, setScore] = useState(["0"]); // строка для удобства редактирования
  const [winEventId, setWinEventId] = useState("");

  const [tournaments, setTournaments] = useState([]);
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const match = await matchService.getMatch(id);
        setBestOf(match.best_of);
        setDateStart(match.date_start.slice(0, 16));
        setDateEnd(match.date_end ? match.date_end.slice(0, 16) : "");
        setTournamentId(match.tournament_id || match.tournament?.id);
        setFirstTeamId(match.first_team_id || match.first_team?.id);
        setSecondTeamId(match.second_team_id || match.second_team?.id);
        setScore(match.score ? match.score.map(String) : ["0"]);
        setWinEventId(match.win_event_id || "");

        const tournamentsData = await tournamentService.getAllTournaments();
        setTournaments(tournamentsData);

        const teamsData = await teamService.getAllTeams();
        setTeams(teamsData);
      } catch (error) {
        console.error("Ошибка загрузки данных матча", error);
      }
    }

    fetchData();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (firstTeamId === secondTeamId) {
      alert("Нельзя выбрать одну и ту же команду для обеих сторон.");
      return;
    }

    const scoreNumbers = score.map((s) => Number(s));

    const data = {
      best_of: bestOf,
      date_start: dateStart,
      date_end: dateEnd || dateStart,
      tournament_id: tournamentId,
      first_team_id: firstTeamId,
      second_team_id: secondTeamId,
      score: scoreNumbers,
      win_event_id: winEventId || null,
    };

    try {
      await matchService.updateMatch(id, data);
      navigate("/admin/matches");
    } catch (error) {
      console.error("Ошибка при обновлении матча:", error);
      alert("Ошибка при обновлении матча.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-md mx-auto p-4 border rounded">
      <h2 className="text-xl font-semibold mb-4">Редактировать матч</h2>

      <label>
        Best Of:
        <input
          type="number"
          min="1"
          value={bestOf}
          onChange={(e) => setBestOf(Number(e.target.value))}
          required
          className="w-full border p-2 rounded mt-1"
        />
      </label>

      <label>
        Дата начала:
        <input
          type="datetime-local"
          value={dateStart}
          onChange={(e) => setDateStart(e.target.value)}
          required
          className="w-full border p-2 rounded mt-1"
        />
      </label>

      <label>
        Дата окончания:
        <input
          type="datetime-local"
          value={dateEnd}
          onChange={(e) => setDateEnd(e.target.value)}
          className="w-full border p-2 rounded mt-1"
        />
      </label>

      <label>
        Турнир:
        <select
          value={tournamentId}
          onChange={(e) => setTournamentId(e.target.value)}
          required
          className="w-full border p-2 rounded mt-1"
        >
          <option value="">Выберите турнир</option>
          {tournaments.map((t) => (
            <option key={t.id} value={t.id}>
              {t.name}
            </option>
          ))}
        </select>
      </label>

      <label>
        Команда 1:
        <select
          value={firstTeamId}
          onChange={(e) => setFirstTeamId(e.target.value)}
          required
          className="w-full border p-2 rounded mt-1"
        >
          <option value="">Выберите команду</option>
          {teams.map((team) => (
            <option key={team.id} value={team.id}>
              {team.name}
            </option>
          ))}
        </select>
      </label>

      <label>
        Команда 2:
        <select
          value={secondTeamId}
          onChange={(e) => setSecondTeamId(e.target.value)}
          required
          className="w-full border p-2 rounded mt-1"
        >
          <option value="">Выберите команду</option>
          {teams.map((team) => (
            <option key={team.id} value={team.id}>
              {team.name}
            </option>
          ))}
        </select>
      </label>

      <label>
        Счёт (через двоеточие, например 2:1):
        <input
          type="text"
          value={score.join(":")}
          onChange={(e) => setScore(e.target.value.split(":"))}
          className="w-full border p-2 rounded mt-1"
        />
      </label>

      <label>
        ID события победы (win_event_id):
        <input
          type="number"
          value={winEventId}
          onChange={(e) => setWinEventId(e.target.value)}
          className="w-full border p-2 rounded mt-1"
          min="0"
        />
      </label>

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Сохранить изменения
      </button>
    </form>
  );
};

export default MatchEditPage;
