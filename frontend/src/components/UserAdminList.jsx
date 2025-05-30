import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import userService from "../services/userService";
import { Link } from "react-router-dom";


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
          <Link className="text-blue-600 hover:underline" to={`/admin/users/${row.id}`}>✏️</Link>
          <button className="text-red-600 hover:underline">🗑</button>
        </div>
      ),
    },
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