import { useEffect, useState } from "react";
import eventService from "../services/eventService";
import matchService from "../services/matchService";
import EventAdminList from "../components/EventAdminList";
import EventCreate from "../components/EventCreate";

const EventAdminPage = () => {
  const [events, setEvents] = useState([]);
  const [matches, setMatches] = useState([]);
  const [selectedMatchId, setSelectedMatchId] = useState("");

  useEffect(() => {
    fetchMatches();
    fetchEvents(); // без фильтра — все
  }, []);

  useEffect(() => {
    fetchEvents(selectedMatchId);
  }, [selectedMatchId]);

  async function fetchMatches() {
    try {
      const data = await matchService.getAllMatches({});
      setMatches(data);
    } catch (error) {
      console.error("Ошибка при загрузке матчей:", error);
    }
  }

  async function fetchEvents(match_id = "") {
    try {
      const data = await eventService.getEvents(match_id ? { match_id } : {});
      setEvents(data);
    } catch (error) {
      console.error("Ошибка при загрузке событий:", error);
    }
  }

  async function onEventDelete(eventId) {
    const status = await eventService.deleteEvent(eventId);

    if (status === 200) {
      fetchEvents();
    } else {
      alert("ERROR");
    }
  }

  return (
    <div className="flex flex-col gap-y-4">
      <h2 className="text-xl font-bold">События</h2>
        <EventCreate afterSubmit={fetchEvents}/>
      <div>
        <label className="mr-2 font-medium">Фильтр по матчу:</label>
        <select
          className="border rounded p-1"
          value={selectedMatchId}
          onChange={(e) => setSelectedMatchId(e.target.value)}
        >
          <option value="">Все матчи</option>
          {matches.map((match) => (
            <option key={match.id} value={match.id}>
              #{match.id}: {match?.first_team?.name} - {match?.second_team?.name}
            </option>
          ))}
        </select>
      </div>

      <EventAdminList events={events} onEventDelete={onEventDelete}/>
    </div>
  );
};

export default EventAdminPage;
