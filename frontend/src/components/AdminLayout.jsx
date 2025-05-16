import { NavLink, Outlet } from "react-router-dom"


const SideBar = () => {
    const linkClassName = ({ isActive }) =>
        `font-inter px-4 py-2 rounded-lg hover:bg-oneWinBlue-500 transition ${
        isActive ? "bg-oneWinBlue-400 font-semibold" : ""
    }`

    return (
        <aside className="w-64 bg-oneWinBlue-600 text-white p-6 rounded-2xl shadow-lg self-start">
            <h1 className="text-2xl font-bold font-inter mb-8">Админ-панель</h1>
            <nav className="flex flex-col gap-4">
                <NavLink
                    to="/admin/users"
                    className={linkClassName}
                >
                    Пользователи
                </NavLink>
                <NavLink
                    to="/admin/business-settings"
                    className={linkClassName}
                >
                    Бизнес-настройки
                </NavLink>
                <NavLink
                    to="/admin/matches"
                    className={linkClassName}
                >
                    Матчи
                </NavLink>
                <NavLink
                    to="/admin/games"
                    className={linkClassName}
                >
                    Игры
                </NavLink>
                <NavLink
                    to="/admin/teams"
                    className={linkClassName}
                >
                    Команды
                </NavLink>
                <NavLink
                    to="/admin/tournaments"
                    className={linkClassName}
                >
                    Турниры
                </NavLink>
            </nav>
        </aside>
    );
};

const AdminLayout = () => {
  return (
    <div className="bg-oneWinBlue-300 min-h-screen">
      <div className="container mx-auto flex pt-12 px-4">
        <SideBar />
        <div className="flex-grow ml-6 bg-white rounded-2xl p-6 shadow-md">
            <Outlet/>
        </div>
      </div>
    </div>
  );
};

export default AdminLayout;
