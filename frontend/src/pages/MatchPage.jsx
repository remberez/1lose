import React, { useEffect, useState } from "react";
import MatchHeader from "../components/MatchHeader";
import ExpandableBlock from "../components/CoefficientBlock";
import { useParams } from "react-router-dom";
import eventService from "../services/eventService";
import matchService from "../services/matchService";

const MatchPage = () => {
    const { id } = useParams();
    const [events, setEvents] = useState([]);
    const [match, setMatch] = useState({});

    useEffect(() => {
        async function fetchData() {
            const eventsData = await eventService.getEvents({match_id: id});
            setEvents(eventsData);

            const matchData = await matchService.getMatch(id);
            setMatch(matchData);
        }
        fetchData();
    }, [])

    return (
        <div className="bg-oneWinBlue-600 text-white font-inter p-6 flex-1">
            <div className="max-w-7xl mx-auto">
                <MatchHeader matchData={match}/>
                <div className="flex flex-col mt-4 gap-y-2">
                    {
                        events.map(value => (
                            <ExpandableBlock eventData={value}/>
                        ))
                    }
                </div>
            </div>
        </div>
    );
};

export default MatchPage;
