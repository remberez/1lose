import { Link } from "react-router-dom";
import AdminList from "./AdminList";

const TournamentAdminList = ({ tournaments, onDeleteClick }) => {
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
          <Link className="text-blue-600 hover:underline" to={`${row.id}`}>✏️</Link>
          <button className="text-red-600 hover:underline" onClick={() => onDeleteClick(row.id)}>🗑</button>
        </div>
      ),
    },
  ];

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 font-inter">Турниры</h2>
      <AdminList columns={columns} data={tournaments} />
    </div>
  );
};

export default TournamentAdminList;
