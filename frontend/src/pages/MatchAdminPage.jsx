import { useEffect, useState } from "react";
import MatchAdminList from "../components/MatchAdminList";
import MatchCreate from "../components/MatchCreate";
import matchService from "../services/matchService";

const MatchAdminPage = () => {
    const [matches, setMatches] = useState([]);
    
    async function fetchData() {
        const matchesData = await matchService.getAllMatches({});
        setMatches(matchesData);
    }

    async function onMatchDelete(matchId) {
        const status = await matchService.deleteMatch(matchId);
        
        if (status === 200) {
            fetchData();
        } else {
            alert("Error");
        }
    }

    useEffect(() => {
        fetchData();
    }, [])

    return (
        <div className="flex flex-col gap-y-4">
            <MatchCreate afterSubmit={fetchData}/>
            <MatchAdminList matches={matches} onMatchDelete={onMatchDelete}/>
        </div>
    )
}

export default MatchAdminPage;