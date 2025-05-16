import TeamAdminList from "../components/TeamAdminList";
import { useEffect, useState } from "react";
import TeamCreateForm from "../components/TeamCreateForm";
import TeamService from "../services/teamService";

const TeamAdminPage = () => {
    const [teams, setTeams] = useState([]);

    const fetchTeams = async () => {
        try {
            const data = await TeamService.getAllTeams();
            setTeams(data);
        } catch (error) {
            console.error("Ошибка загрузки команд:", error);
        }
    };

    useEffect(() => {
        fetchTeams();
    }, []);

    return (
        <div className="p-4">
            <TeamCreateForm onCreated={fetchTeams} />
            <TeamAdminList teams={teams} />
        </div>
    );
};

export default TeamAdminPage;

