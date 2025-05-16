import { useState, useEffect } from "react";
import matchService from "../services/matchService";
import tournamentService from "../services/tournamentService";
import teamService from "../services/teamService";

const MatchCreate = ({ afterSubmit }) => {
  const [bestOf, setBestOf] = useState(1);
  const [dateStart, setDateStart] = useState("");
  const [tournamentId, setTournamentId] = useState("");
  const [firstTeamId, setFirstTeamId] = useState("");
  const [secondTeamId, setSecondTeamId] = useState("");

  const [tournaments, setTournaments] = useState([]);
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const tournamentsData = await tournamentService.getAllTournaments();
      setTournaments(tournamentsData);

      const teamsData = await teamService.getAllTeams();
      setTeams(teamsData);
    }

    fetchData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (firstTeamId === secondTeamId) {
      alert("Нельзя выбрать одну и ту же команду для обеих сторон.");
      return;
    }

    const data = {
      best_of: bestOf,
      date_start: dateStart,
      tournament_id: tournamentId,
      first_team_id: firstTeamId,
      second_team_id: secondTeamId,
    };

    try {
      await matchService.createMatch(data);
      await afterSubmit();
    } catch (error) {
      console.error("Ошибка при создании матча:", error);
      alert("Ошибка при создании матча.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-6xl p-4 border rounded">
      <h2 className="text-xl font-semibold mb-4">Создать матч</h2>

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

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Создать матч
      </button>
    </form>
  );
};

export default MatchCreate;
