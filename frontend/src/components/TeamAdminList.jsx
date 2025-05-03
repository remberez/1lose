import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import teamService from "../services/teamService";

const columns = [
  { key: "id", title: "ID" },
  { key: "name", title: "Название команды" },
  {
    key: "game",
    title: "Игра",
    render: (value) => value?.name || "—",
  },
  {
    key: "icon_path",
    title: "Иконка",
    render: (value) => (
      <img src={value} alt="Иконка команды" className="w-8 h-8 object-contain" />
    ),
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

const TeamAdminList = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const data = await teamService.getAllTeams();
      setTeams(data);
    }

    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 font-inter">Команды</h2>
      <AdminList columns={columns} data={teams} />
    </div>
  );
};

export default TeamAdminList;
