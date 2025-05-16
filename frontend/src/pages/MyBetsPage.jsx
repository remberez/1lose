import { useEffect, useState } from "react";
import betService from "../services/betService";
import dayjs from "dayjs";

const MyBetsPage = () => {
  const [bets, setBets] = useState([]);
  const [loading, setLoading] = useState(true);

  async function fetchBets() {
    setLoading(true);
    try {
      const data = await betService.getMyBets();
      setBets(data);
    } catch (error) {
      console.error("Ошибка при загрузке ставок", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchBets();
  }, []);

  function handleSell(betId) {
    alert(`Продажа ставки с ID ${betId}`);
  }

  if (loading) return <div className="p-4">Загрузка...</div>;

  return (
    <div className="p-4 max-w-6xl mx-auto">
      <h2 className="text-2xl font-semibold mb-6">Мои ставки</h2>
      <div className="overflow-auto">
        <table className="w-full text-sm text-left border border-gray-200 rounded shadow-sm bg-white">
          <thead className="bg-gray-100 text-gray-700 uppercase text-xs">
            <tr>
              <th className="px-4 py-3">Дата</th>
              <th className="px-4 py-3">Время</th>
              <th className="px-4 py-3">№ Ставки</th>
              <th className="px-4 py-3">Тип</th>
              <th className="px-4 py-3">Описание</th>
              <th className="px-4 py-3">Коэф.</th>
              <th className="px-4 py-3">Результат</th>
              <th className="px-4 py-3">Сумма</th>
              <th className="px-4 py-3">Действие</th>
            </tr>
          </thead>
          <tbody>
            {bets.map((bet) => {
              const createdAt = dayjs(bet.created_at || new Date());
              const resultText =
                bet.bet_status === "win"
                  ? "Выигрыш"
                  : bet.bet_status === "lose"
                  ? "Проигрыш"
                  : "Активна";

              const resultColor =
                bet.bet_status === "win"
                  ? "text-green-600"
                  : bet.bet_status === "lose"
                  ? "text-red-600"
                  : "text-yellow-600";

              return (
                <tr key={bet.id} className="border-t">
                  <td className="px-4 py-2">{createdAt.format("DD.MM")}</td>
                  <td className="px-4 py-2">{createdAt.format("HH:mm:ss")}</td>
                  <td className="px-4 py-2">{bet.id}</td>
                  <td className="px-4 py-2">Одинар</td>
                  <td className="px-4 py-2">Баланс</td>
                  <td className="px-4 py-2">{bet.coefficient}</td>
                  <td className={`px-4 py-2 font-semibold ${resultColor}`}>
                    {resultText}
                  </td>
                  <td className="px-4 py-2">
                    {bet.possible_gain
                      ? `${bet.amount} → ${bet.possible_gain}`
                      : bet.amount}
                  </td>
                  <td className="px-4 py-2">
                    <button
                      onClick={() => handleSell(bet.id)}
                      className="text-blue-600 hover:underline text-sm"
                    >
                      Продать
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MyBetsPage;
