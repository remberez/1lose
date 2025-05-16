import { observer } from "mobx-react-lite";
import { userStore } from "../stores/authStore";

const ProfilePage = observer(() => {
  const user = userStore.user;

  if (!user) {
    return <div>Загрузка данных...</div>;
  }

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded shadow">
      <h2 className="text-2xl font-semibold mb-4">Профиль пользователя</h2>
      <div className="mb-2">
        <span className="font-medium">Email:</span> {user.email}
      </div>
      <div className="mb-2">
        <span className="font-medium">Активен:</span> {user.is_active ? "Да" : "Нет"}
      </div>
      <div className="mb-2">
        <span className="font-medium">Баланс:</span> {user.balance} ₽
      </div>
    </div>
  );
});

export default ProfilePage;
