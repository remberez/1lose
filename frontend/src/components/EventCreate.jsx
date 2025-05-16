import { useState, useEffect } from "react";
import eventService from "../services/eventService";
import matchService from "../services/matchService";

const EventCreate = ({ afterSubmit }) => {
  const [name, setName] = useState("");
  const [matchId, setMatchId] = useState("");
  const [mapId, setMapId] = useState("");
  const [firstOutcomeName, setFirstOutcomeName] = useState("");
  const [firstOutcomeCoeff, setFirstOutcomeCoeff] = useState("");
  const [secondOutcomeName, setSecondOutcomeName] = useState("");
  const [secondOutcomeCoeff, setSecondOutcomeCoeff] = useState("");
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    async function fetchMatches() {
      const data = await matchService.getAllMatches({});
      setMatches(data);
    }
    fetchMatches();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const eventData = {
      name,
      match_id: Number(matchId),
      map_id: mapId ? Number(mapId) : null,  // map_id может быть null
      first_outcome: {
        name: firstOutcomeName,
        coefficient: Number(firstOutcomeCoeff),
      },
      second_outcome: {
        name: secondOutcomeName,
        coefficient: Number(secondOutcomeCoeff),
      },
    };

    try {
      await eventService.createEvent(eventData);
      if (afterSubmit) await afterSubmit();
      // Очистка формы
      setName("");
      setMatchId("");
      setMapId("");
      setFirstOutcomeName("");
      setFirstOutcomeCoeff("");
      setSecondOutcomeName("");
      setSecondOutcomeCoeff("");
    } catch (error) {
      alert("Ошибка при создании события");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 border rounded">
      <h3 className="text-lg font-semibold">Создать событие</h3>

      <div>
        <label>Название события*</label>
        <input
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full border px-2 py-1"
        />
      </div>

      <div>
        <label>Матч*</label>
        <select
          required
          value={matchId}
          onChange={(e) => setMatchId(e.target.value)}
          className="w-full border px-2 py-1"
        >
          <option value="">Выберите матч</option>
          {matches.map((m) => (
            <option key={m.id} value={m.id}>
              {m.id} — {m.first_team?.name} vs {m.second_team?.name}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label>Карта (map_id, можно оставить пустым)</label>
        <input
          value={mapId}
          onChange={(e) => setMapId(e.target.value)}
          type="number"
          min="1"
          placeholder="ID карты"
          className="w-full border px-2 py-1"
        />
      </div>

      <div>
        <label>Первый исход - название*</label>
        <input
          required
          value={firstOutcomeName}
          onChange={(e) => setFirstOutcomeName(e.target.value)}
          className="w-full border px-2 py-1"
        />
      </div>

      <div>
        <label>Первый исход - коэффициент*</label>
        <input
          required
          value={firstOutcomeCoeff}
          onChange={(e) => setFirstOutcomeCoeff(e.target.value)}
          type="number"
          step="0.01"
          className="w-full border px-2 py-1"
        />
      </div>

      <div>
        <label>Второй исход - название*</label>
        <input
          required
          value={secondOutcomeName}
          onChange={(e) => setSecondOutcomeName(e.target.value)}
          className="w-full border px-2 py-1"
        />
      </div>

      <div>
        <label>Второй исход - коэффициент*</label>
        <input
          required
          value={secondOutcomeCoeff}
          onChange={(e) => setSecondOutcomeCoeff(e.target.value)}
          type="number"
          step="0.01"
          className="w-full border px-2 py-1"
        />
      </div>

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Создать событие
      </button>
    </form>
  );
};

export default EventCreate;
