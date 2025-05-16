import { Link } from "react-router-dom";
import AdminList from "./AdminList";

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
        <Link className="text-blue-600 hover:underline" to={`${row.id}`}>✏️</Link>
        <button className="text-red-600 hover:underline">🗑</button>
      </div>
    ),
  },
];

const TeamAdminList = ({teams}) => {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 font-inter">Команды</h2>
      <AdminList columns={columns} data={teams} />
    </div>
  );
};

export default TeamAdminList;
