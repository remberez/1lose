import { Link } from "react-router-dom";
import AdminList from "../components/AdminList";

const EventAdminList = ({ events, onEventDelete }) => {
  const cols = [
    { key: "id", title: "ID" },
    { key: "name", title: "Название" },
    {
      key: "map",
      title: "Карта",
      render: (map) => `ID: ${map?.id || "—"}, Счёт: ${map?.score?.join(":") || "—"}`,
    },
    {
      key: "first_outcome",
      title: "Первый исход",
      render: (outcome) =>
        outcome ? `${outcome.name} (${outcome.coefficient})` : "—",
    },
    {
      key: "second_outcome",
      title: "Второй исход",
      render: (outcome) =>
        outcome ? `${outcome.name} (${outcome.coefficient})` : "—",
    },
    {
      key: "created_at",
      title: "Создано",
      render: (value) => value?.slice(0, 10) || "—",
    },
    {
      key: "updated_at",
      title: "Обновлено",
      render: (value) => value?.slice(0, 10) || "—",
    },
    {
          key: "actions",
          title: "Действия",
          render: (_, row) => (
            <div className="flex gap-2">
              <Link className="text-blue-600 hover:underline" to={`${row.id}`}>✏️</Link>
              <button className="text-red-600 hover:underline" onClick={() => onEventDelete(row.id)}>🗑</button>
            </div>
          ),
      },
  ];

  return <AdminList data={events} columns={cols} />;
};

export default EventAdminList;
