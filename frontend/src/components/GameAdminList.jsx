import AdminList from "./AdminList";
import gameService from "../services/gameService";
import { Link } from "react-router-dom"


const GameAdminList = ({games, onGameDelete}) => {
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
            <Link className="text-blue-600 hover:underline" to={row.id}>✏️</Link>
            <button className="text-red-600 hover:underline" onClick={() => onGameDelete(row.id)}>🗑</button>
          </div>
        ),
      },
    ];
  
    return (
        <AdminList data={games} columns={columns} />
    )
}

export default GameAdminList;
