import AdminList from "./AdminList";
import { Link } from "react-router-dom";

const MatchAdminList = ({ matches, onMatchDelete }) => {
    const cols = [
      { key: "id", title: "ID" },
      { key: "best_of", title: "Бест оф" },
      {
        key: "tournament",
        title: "Турнир",
        render: (value) => value?.name || "—",
      },
      {
        key: "tournament_game",
        title: "Игра турнира",
        render: (_, row) => row.tournament?.game?.name || "—",
      },
      {
        key: "first_team",
        title: "Команда 1",
        render: (value) => value?.name || "—",
      },
      {
        key: "second_team",
        title: "Команда 2",
        render: (value) => value?.name || "—",
      },
      {
        key: "game",
        title: "Игра",
        render: (_, row) => row.first_team?.game?.name || "—",
      },
      {
        key: "score",
        title: "Счёт карт",
        render: (value) => Array.isArray(value) ? value.join(":") : "—",
      },
      {
        key: "created_at",
        title: "Создано",
        render: (_, row) => row.win_event?.created_at?.slice(0, 10) || "—",
      },
      {
        key: "updated_at",
        title: "Обновлено",
        render: (_, row) => row.win_event?.updated_at?.slice(0, 10) || "—",
      },
      {
          key: "actions",
          title: "Действия",
          render: (_, row) => (
            <div className="flex gap-2">
              <Link className="text-blue-600 hover:underline" to={`${row.id}`}>✏️</Link>
              <button className="text-red-600 hover:underline" onClick={() => onMatchDelete(row.id)}>🗑</button>
            </div>
          ),
      },
    ];
  
    return (
        <AdminList data={matches} columns={cols}/>
    )
}

export default MatchAdminList;