import { NavLink, Outlet } from "react-router-dom";

const ProfileLayout = () => {
    return (
        <div className="flex flex-1">
            <aside className="w-60 bg-gray-100 border-r border-gray-300 p-4">
            <nav className="flex flex-col space-y-3">
                <NavLink
                to="/profile/deposits"
                className={({ isActive }) =>
                    "block px-3 py-2 rounded " +
                    (isActive ? "bg-blue-500 text-white" : "text-gray-700 hover:bg-gray-200")
                }
                >
                    Пополнения
                </NavLink>
                <NavLink
                    to="/profile/bets"
                    className={({ isActive }) =>
                        "block px-3 py-2 rounded " +
                        (isActive ? "bg-blue-500 text-white" : "text-gray-700 hover:bg-gray-200")
                    }
                >
                    Мои ставки
                </NavLink>
                <NavLink
                to="/profile"
                end
                className={({ isActive }) =>
                    "block px-3 py-2 rounded " +
                    (isActive ? "bg-blue-500 text-white" : "text-gray-700 hover:bg-gray-200")
                }
                >
                    Профиль
                </NavLink>
            </nav>
            </aside>

            <main className="flex-1 p-6 bg-white">
                <Outlet />
            </main>
        </div>
    )
}

export default ProfileLayout;