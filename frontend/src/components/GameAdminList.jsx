import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import gameService from "../services/gameService";

const columns = [
    { key: "id", title: "ID" },
    { key: "name", title: "Название" },
    { key: "description", title: "Описание" },
    {
      key: "icon_path",
      title: "Иконка",
      render: (value) => (
        <img src={value} alt="Иконка" className="w-8 h-8 object-contain" />
      )
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
  

const GameAdminList = () => {
    const [games, setGames] = useState([]);
    
    useEffect(() => {
        async function fetchData() {
            const gamesData = await gameService.getGames();
            setGames(gamesData);
        }

        fetchData();
    }, [])
    return (
        <AdminList data={games} columns={columns} />
    )
}

export default GameAdminList;
