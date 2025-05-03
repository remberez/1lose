import AdminList from "./AdminList";


const columns = [
    { key: "id", title: "ID" },
    { key: "name", title: "Имя" },
    { key: "email", title: "Email" },
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
  
  const data = [
    { id: 1, name: "Артём", email: "artem@example.com" },
    { id: 2, name: "Анна", email: "anna@example.com" },
  ];

  
const UserAdminList = () => {
    return (
        <div>
            <h2 className="text-xl font-semibold mb-4 font-inter">Пользователи</h2>
            <AdminList columns={columns} data={data} />
        </div>
    )
}

export default UserAdminList;