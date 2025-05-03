import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import tournamentService from "../services/tournamentService";

const columns = [
  { key: "id", title: "ID" },
  { key: "name", title: "Название турнира" },
  { key: "description", title: "Описание" },
  {
    key: "game",
    title: "Игра",
    render: (value) => value?.name || "—",
  },
  {
    key: "actions",
    title: "Действия",
    render: (_, row) => (
      <div className="flex gap-2">
        <button className="text-blue-600 hover:underline">✏️</button>
        <button className="text-red-600 hover:underline">🗑</button>
      </div>
    ),
  },
];

const TournamentAdminList = () => {
  const [tournaments, setTournaments] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const data = await tournamentService.getAllTournaments();
      setTournaments(data);
    }

    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 font-inter">Турниры</h2>
      <AdminList columns={columns} data={tournaments} />
    </div>
  );
};

export default TournamentAdminList;
