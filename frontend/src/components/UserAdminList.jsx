import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import userService from "../services/userService";


const columns = [
    { key: "id", title: "ID" },
    { key: "email", title: "Email" },
    { key: "balance", title: "Баланс" },
    { key: "is_active", title: "Активен?" },
    { key: "role_code", title: "Роль" },
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
    const [users, setUsers] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const usersData = await userService.getUserList();
            setUsers(usersData);
        }

        fetchData();
    }, [])

    return (
        <div>
            <h2 className="text-xl font-semibold mb-4 font-inter">Пользователи</h2>
            <AdminList columns={columns} data={users} />
        </div>
    )
}

export default UserAdminList;