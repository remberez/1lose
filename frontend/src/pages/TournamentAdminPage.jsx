import TournamentAdminList from "../components/TournamentAdminList";
import TournamentCreateForm from "../components/TournamentCreateForm";
import { useEffect, useState } from "react";
import tournamentService from "../services/tournamentService";

const TournamentAdminPage = () => {
  const [tournaments, setTournaments] = useState([]);

  async function fetchData() {
    const data = await tournamentService.getAllTournaments();
    setTournaments(data);
  }

  async function onDeleteClick(id) {
    const status = await tournamentService.deleteTournament(id);
    if (status === 200) {
      fetchData();
    } else {
      alert("ERROR");
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="p-4">
      <TournamentCreateForm onSuccess={fetchData} />
      <TournamentAdminList tournaments={tournaments} onDeleteClick={onDeleteClick}/>
    </div>
  );
};

export default TournamentAdminPage;

