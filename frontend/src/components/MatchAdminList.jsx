import { useEffect, useState } from "react";
import AdminList from "./AdminList";
import matchService from "../services/matchService";

const cols = [
    { key: "id", title: "ID" },
    { key: "best_of", title: "Бест оф" },
    {
      key: "tournament",
      title: "Турнир",
      render: (value) => value?.name || "—",
    },
    {
      key: "tournament_game",
      title: "Игра турнира",
      render: (_, row) => row.tournament?.game?.name || "—",
    },
    {
      key: "first_team",
      title: "Команда 1",
      render: (value) => value?.name || "—",
    },
    {
      key: "second_team",
      title: "Команда 2",
      render: (value) => value?.name || "—",
    },
    {
      key: "game",
      title: "Игра",
      render: (_, row) => row.first_team?.game?.name || "—",
    },
    {
      key: "score",
      title: "Счёт карты",
      render: (value) => Array.isArray(value) ? value.join(":") : "—",
    },
    {
      key: "created_at",
      title: "Создано",
      render: (_, row) => row.win_event?.created_at?.slice(0, 10) || "—",
    },
    {
      key: "updated_at",
      title: "Обновлено",
      render: (_, row) => row.win_event?.updated_at?.slice(0, 10) || "—",
    },
];
  

const MatchAdminList = () => {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const matchesData = await matchService.getAllMatches({});
            setMatches(matchesData);
        }

        fetchData();
    }, [])

    return (
        <AdminList data={matches} columns={cols}/>
    )
}

export default MatchAdminList;